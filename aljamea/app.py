"""Aljamea-tus-Saifiyah — website.

Run:  python app.py                (http://127.0.0.1:5070)
Prod: gunicorn --preload app:app
"""
import os
import re
from datetime import date, datetime, timedelta, timezone

from flask import Flask, render_template, url_for
from markupsafe import Markup, escape

import content
from hijri import hijri_parts

IST = timezone(timedelta(hours=5, minutes=30))
HONORIFICS = re.compile(r'(?<=\w)\s?\b(RA|TUS|AS|SA|SAW|QR|DM)\b')


def create_app():
    here = os.path.dirname(os.path.abspath(__file__))
    app = Flask('aljamea', root_path=here)
    app.config.update(
        SECRET_KEY=os.environ.get('ALJAMEA_SECRET', 'dev-change-me'),
        SEND_FILE_MAX_AGE_DEFAULT=60 * 60 * 24 * 30,
        HIJRI_OFFSET_DAYS=int(os.environ.get('HIJRI_OFFSET_DAYS', 0)),
    )
    if os.environ.get('BEHIND_PROXY') == '1':
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

    # DM Serif / DM Sans lack the ʿayn and hamza modifier letters; typeset them as ‘ and ’ as print editions do.
    app.jinja_env.finalize = lambda v: v.replace('ʿ', '‘').replace('ʾ', '’') if isinstance(v, str) else v

    from views.site import bp
    app.register_blueprint(bp)

    media_dir = os.path.join(app.static_folder, 'media')

    @app.context_processor
    def _inject():
        today = datetime.now(IST).date()
        return dict(inst=content.INSTITUTE, campuses=content.CAMPUSES, today=today,
                    hijri=hijri_parts(today, app.config['HIJRI_OFFSET_DAYS']),
                    years_since_founding=today.year - content.INSTITUTE['founded_ce'])

    @app.template_global()
    def asset(path):
        full = os.path.join(app.static_folder, path)
        v = int(os.path.getmtime(full)) if os.path.exists(full) else 0
        return url_for('static', filename=path, v=v)

    @app.template_global()
    def img(key, size='lg'):
        """URL for a photograph; 'sm' is 960px, 'lg' is 2560px."""
        sub = 'media/sm/' if size == 'sm' else 'media/'
        return url_for('static', filename=f'{sub}{key}.jpg')

    @app.template_global()
    def srcset(key):
        return f"{img(key, 'sm')} 960w, {img(key)} 2560w"

    @app.template_global()
    def has_img(key):
        return bool(key) and os.path.exists(os.path.join(media_dir, f'{key}.jpg'))

    @app.template_filter('hon')
    def hon(text):
        """Typeset honorifics (RA, TUS, AS…) as small raised caps, as in print."""
        return Markup(HONORIFICS.sub(lambda m: f'<span class="hon">{m.group(1)}</span>', str(escape(text))))

    @app.template_filter('ardigits')
    def ardigits(n):
        return str(n).translate(str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩'))

    @app.template_filter('nicedate')
    def nicedate(d, fmt='%-d %B %Y'):
        return d.strftime(fmt) if isinstance(d, (date, datetime)) else d

    @app.template_filter('hijri')
    def hijri_filter(d, lang='en'):
        return hijri_parts(d, app.config['HIJRI_OFFSET_DAYS'])[lang]

    @app.after_request
    def _headers(resp):
        resp.headers.setdefault('X-Content-Type-Options', 'nosniff')
        resp.headers.setdefault('Referrer-Policy', 'strict-origin-when-cross-origin')
        resp.headers.setdefault('X-Frame-Options', 'SAMEORIGIN')
        resp.headers.setdefault('Permissions-Policy', 'camera=(), microphone=(), geolocation=()')
        return resp

    @app.errorhandler(404)
    def _404(e):
        return render_template('error.html'), 404

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get('PORT', 5070)), debug=os.environ.get('FLASK_DEBUG') == '1')
