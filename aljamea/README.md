# Aljamea-tus-Saifiyah — website (Flask)

A proposed replacement for jameasaifiyah.edu. Same colours as the current site (copper `#CF8A40`,
bronze `#9F672F`, cream `#FFF9F0`, logo lapis `#1C388C`, DM Serif Display + DM Sans), with Arabic set in
Kanz al-Marjaan. The design language is the **honeycomb**: the hexagons of the Mumbai façade, the Surat
Masākin balconies and the classroom panels. Bees gather from many flowers and make one beneficial honey.

## Run

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python app.py          # http://127.0.0.1:5070
```

`FLASK_DEBUG=1` reloads templates on save. Production: `gunicorn --preload app:app` (set `BEHIND_PROXY=1`
behind a proxy, `HIJRI_OFFSET_DAYS` to nudge the Misri date).

## What's inside

- **The Hive** (home hero): a honeycomb of cells, each a window onto the same photograph. The comb ripples
  in on load, swells under the cursor, rotates through eight scenes (four campuses, Mahad al-Zahra, library,
  Mawāʾid, auditorium) with a cell-by-cell ripple, and on scroll grows until it becomes one full-screen photo.
- **Journey of knowledge**: a scroll-driven map, Cairo 970 → Yemen → Ahmedabad → Surat → Karachi → Nairobi → Mumbai.
- **Campus rail**, the **eleven-step ladder** (the 11-level step garden = 11 years, 4 stages), the
  **estuary** (Syedna Taher Saifuddin's four streams, animated), the **faculty flower** (six faculties
  around the Quran), campus-life mosaic, luminaries with hover portraits, rotating testimonials, news.
- Inner pages: About, History (scroll timeline, 31 events), Architecture, Philosophy, Examinations,
  Academics, 6 faculties, 5 departments, 4 campuses, 6 campus-life pages, 7 luminaries, news + articles,
  Admissions, Contact (maps), and `/proposal`: the review of the current site for the directors.
- ⌘K / `/` search, day/night/auto theme, Hijri (Misri) date throughout, reduced-motion support,
  sitemap.xml, robots.txt, structured data, and **301 redirects from every old WordPress URL**.

## Content

All text is in `content.py` (proof-read from the live site); the audit is in `audit.py`.
Photos are the institution's own, downloaded at full resolution into `static/media/` (2560 px) and
`static/media/sm/` (960 px), served with `srcset`. The logo is the official vector `static/img/logo.svg`
(transparent, sharp at any size), recoloured with CSS masks.

Items for the office to confirm before launch: the admissions steps, the Mahad al-Zahra Karachi date
(1429/2008 vs 1430/2009 on the current site), and whether Siddhpur should be listed as a fifth campus.
