from flask import Blueprint, abort, jsonify, redirect, render_template, request, url_for

import audit
import content as c

bp = Blueprint('site', __name__)


def _get(table, slug):
    item = table.get(slug)
    if not item:
        abort(404)
    return item


def _neighbours(items, item):
    i = items.index(item)
    return items[i - 1] if i else None, items[i + 1] if i + 1 < len(items) else None


def journey_map():
    """Project the journey stops onto a 600×420 SVG and build a curved route through them."""
    W, H, lon0, lon1, lat0, lat1 = 600, 420, 26, 80, -6, 36
    pts, seen = [], {}
    for i, s in enumerate(c.JOURNEY):
        x = round((s['lon'] - lon0) / (lon1 - lon0) * W, 1)
        y = round((lat1 - s['lat']) / (lat1 - lat0) * H, 1)
        pts.append((x, y))
        seen.setdefault(s['city'], dict(x=x, y=y, city=s['city'], k=i))
    d, lens = f'M{pts[0][0]} {pts[0][1]}', [0.0]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = x1 - x0, y1 - y0
        cx, cy = mx - dy * .22, my + dx * .22  # bow each leg to one side
        d += f' Q{cx:.1f} {cy:.1f} {x1} {y1}'
        seg, px, py = 0.0, x0, y0
        for t in [k / 24 for k in range(1, 25)]:
            qx = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
            qy = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
            seg += ((qx - px) ** 2 + (qy - py) ** 2) ** .5
            px, py = qx, qy
        lens.append(lens[-1] + seg)
    total = lens[-1] or 1
    labels = {'Ahmedabad': (14, -6), 'Surat': (14, 9), 'Mumbai': (14, 24), 'Karachi': (-14, 4, 'end'),
              'Cairo': (12, -10), 'Yemen': (14, 4), 'Nairobi': (14, 4)}
    stops = []
    for city, p in seen.items():
        lab = labels.get(city, (12, 4))
        p.update(lx=p['x'] + lab[0], ly=p['y'] + lab[1], anchor=lab[2] if len(lab) > 2 else 'start',
                 k=max(i for i, s in enumerate(c.JOURNEY) if s['city'] == city and i >= p['k']) if city != 'Cairo' else 0)
        stops.append(p)
    return dict(d=d, pts=stops, at=[round(l / total, 4) for l in lens])


HERO_SLIDES = [  # (photo, caption, endpoint, kwargs)
    ('ajsm-05baabshot2-fw', 'Bab Zuwayla · Mumbai campus', 'site.campus', dict(slug='mumbai')),
    ('ajss-00ext02-1', 'The courtyard · Surat campus', 'site.campus', dict(slug='surat')),
    ('ajsn-05baabnasr01-bl-1738-2', 'Bab al-Nasr · Nairobi campus', 'site.campus', dict(slug='nairobi')),
    ('stj05090-302x400', 'The minaret · Karachi campus', 'site.campus', dict(slug='karachi')),
    ('ajsm-03mahadshot1-3785', 'The muqarnas dome · Mahad al-Zahra', 'site.department', dict(slug='mahad-al-zahra')),
    ('ajsm-14zawiyashot1-4347', 'Qāʿat al-Zawāya · Maktabat Aljamea', 'site.facility', dict(slug='library')),
    ('ajsm-04mawaidshot3-0194', 'Al-Mawāʾid · the dining hall', 'site.facility', dict(slug='dining')),
    ('ajsn-17auditorium01-1171', 'The Auditorium · Nairobi', 'site.facility', dict(slug='auditorium')),
]


@bp.route('/')
def home():
    from flask import current_app
    slides = [dict(src=current_app.jinja_env.globals['img'](k), label=l.replace('ʿ', '‘').replace('ʾ', '’'), url=url_for(e, **kw))
              for k, l, e, kw in HERO_SLIDES]
    return render_template('home.html', slides=slides, jmap=journey_map(), journey=c.JOURNEY, stages=c.STAGES, faculties=c.FACULTIES,
                           facilities=c.FACILITIES, luminaries=c.LUMINARIES[:5], news=c.NEWS[:3], voices=c.VOICES)


@bp.route('/about/<slug>')
def page(slug):
    p = _get(c.PAGES, slug)
    return render_template('page.html', p=p, stages=c.STAGES, crumbs=[('About', url_for('site.page', slug='about'))])


@bp.route('/history')
def history():
    return render_template('history.html', timeline=c.TIMELINE, journey=c.JOURNEY, jmap=journey_map())


@bp.route('/academics')
def academics():
    return render_template('academics.html', stages=c.STAGES, faculties=c.FACULTIES, departments=c.DEPARTMENTS,
                           grades=c.GRADES)


@bp.route('/academics/faculties/<slug>')
def faculty(slug):
    f = _get(c.FACULTY, slug)
    prev, nxt = _neighbours(c.FACULTIES, f)
    p = dict(title=f"Faculty of {f['name']}", ar=f['ar'], kicker=f['native'], img=f['img'], lead=f['lead'],
             sections=f['sections'])
    return render_template('page.html', p=p, stages=c.STAGES, siblings=c.FACULTIES, sib_kind='faculty', cur=f,
                           prev=prev, nxt=nxt, crumbs=[('Academics', url_for('site.academics'))])


@bp.route('/academics/departments/<slug>')
def department(slug):
    d = _get(c.DEPARTMENT, slug)
    p = dict(title=d['name'], ar=d['ar'], kicker=d['en'], img=d['img'], lead=d['lead'], sections=d['sections'])
    return render_template('page.html', p=p, stages=c.STAGES, siblings=c.DEPARTMENTS, sib_kind='department', cur=d,
                           crumbs=[('Academics', url_for('site.academics'))])


@bp.route('/campuses')
def campuses():
    return render_template('campuses.html', journey=c.JOURNEY, jmap=journey_map())


@bp.route('/campuses/<slug>')
def campus(slug):
    cp = _get(c.CAMPUS, slug)
    prev, nxt = _neighbours(c.CAMPUSES, cp)
    return render_template('campus.html', cp=cp, prev=prev, nxt=nxt, stages=c.STAGES)


@bp.route('/campus-life')
def life():
    return render_template('life.html', facilities=c.FACILITIES)


@bp.route('/campus-life/<slug>')
def facility(slug):
    f = _get(c.FACILITY, slug)
    prev, nxt = _neighbours(c.FACILITIES, f)
    p = dict(title=f['name'], ar=f['ar'], kicker=f['native'], img=f['img'], lead=f['lead'], sections=f['sections'])
    return render_template('page.html', p=p, stages=c.STAGES, siblings=c.FACILITIES, sib_kind='facility', cur=f,
                           prev=prev, nxt=nxt, crumbs=[('Campus life', url_for('site.life'))])


@bp.route('/luminaries')
def luminaries():
    return render_template('luminaries.html', luminaries=c.LUMINARIES)


@bp.route('/luminaries/<slug>')
def luminary(slug):
    l = _get(c.LUMINARY, slug)
    prev, nxt = _neighbours(c.LUMINARIES, l)
    return render_template('luminary.html', l=l, prev=prev, nxt=nxt, stages=c.STAGES)


@bp.route('/news')
def news():
    campus = request.args.get('campus')
    items = [n for n in c.NEWS if not campus or n['campus'] == campus]
    return render_template('news.html', items=items, campus=campus,
                           campus_names=sorted({n['campus'] for n in c.NEWS}))


@bp.route('/news/<slug>')
def article(slug):
    n = _get(c.NEWS_BY_SLUG, slug)
    more = [x for x in c.NEWS if x is not n][:3]
    return render_template('article.html', n=n, more=more)


@bp.route('/admissions')
def admissions():
    return render_template('admissions.html', programmes=c.PROGRAMMES, steps=c.ADMISSION_STEPS, stages=c.STAGES)


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/proposal')
def proposal():
    return render_template('audit.html', audit=audit.AUDIT, counts=audit.counts(), metrics=audit.METRICS)


@bp.route('/search.json')
def search_index():
    return jsonify(c.search_index(url_for))


@bp.route('/robots.txt')
def robots():
    return 'User-agent: *\nAllow: /\nDisallow: /proposal\nSitemap: ' + url_for('site.sitemap', _external=True) + '\n', \
        200, {'Content-Type': 'text/plain'}


@bp.route('/sitemap.xml')
def sitemap():
    urls = [i['u'] for i in c.search_index(url_for)]
    body = ''.join(f'<url><loc>{request.host_url.rstrip("/")}{u}</loc></url>' for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f'{body}</urlset>'), 200, {'Content-Type': 'application/xml'}


# Old WordPress URLs → new homes (301), so existing links and search rankings carry over.
@bp.route('/<path:old>/')
def legacy(old):
    old = old.strip('/')
    if old in c.LEGACY:
        endpoint, kw = c.LEGACY[old]
        return redirect(url_for(endpoint, **kw), 301)
    lum = {'al-dai-al-ajal-syedna-ismail-badruddin-ra': 'syedna-ismail-badruddin',
           'al-daʿi-al-ajal-syedna-abdeʿali-saifuddin-ra': 'syedna-abdeali-saifuddin',
           'al-dai-al-ajal-syedna-taher-saifuddin-ra': 'syedna-taher-saifuddin',
           'al-daʿi-al-ajal-syedna-mohammed-burhanuddin-ra': 'syedna-mohammed-burhanuddin',
           'al-daʿi-al-ajal-syedna-mufaddal-saifuddin-tus': 'syedna-mufaddal-saifuddin',
           'syedi-abdeʿali-ʿimaduddin-qr': 'syedi-abdeali-imaduddin',
           'dr-shahzada-yusuf-najmuddin-qr': 'dr-yusuf-najmuddin'}
    if old in lum:
        return redirect(url_for('site.luminary', slug=lum[old]), 301)
    if old.startswith('idara-al-ta'):
        return redirect(url_for('site.department', slug='tadib'), 301)
    abort(404)
