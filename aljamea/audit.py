"""Review of the current jameasaifiyah.edu, crawled 19 October 2026 (home + 36 pages).

Each finding: (severity, title, evidence, fix). Severity: critical · high · medium · low.
"""

AUDIT = [
    ('Content left unfinished on public pages', [
        ('critical', 'Template placeholder text is live',
         'The Nairobi campus and “The Realisation” pages show “About Us Copy”, “test about”, “test”, “Timeline”, '
         '“Sample”. “The Three Stages at a Glance” ends with “Accordion Item — Accordion content goes here.” '
         'The homepage has a tab labelled “Tab2”.',
         'Every block is generated from reviewed content; empty or placeholder blocks cannot render.'),
        ('critical', 'Machine-written filler on the Mumbai campus page',
         'Under “Educational Impact” and “Cultural Elements”: “The Mahad al-Zahra appears to be an educational institution…”, '
         '“The building you’re referring to seems to have a rich historical and cultural significance…”, '
         '“This design might be intended to…”. This is chatbot output, published as-is, about the institution’s own building.',
         'Removed. The Mumbai page now uses only the original architectural copy.'),
        ('critical', '“Student Life” is lorem-style filler on the homepage',
         'Three headings (“Equipping Students with Knowledge and Skills”…) share the same generic paragraph, '
         '“Transitioning to university life often brings new challenges and demands”, which has nothing to do with Aljamea.',
         'Replaced with real campus-life content: residences, the thāl, sports, library and the 11-step ladder.'),
        ('high', 'Raw page-builder shortcodes visible in articles',
         'News articles such as “UNEP Delegation Visits Nairobi Campus” and “Mourns the Loss of its Rector” print '
         '“[/fusion_text][/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]” as text: debris '
         'from an earlier Avada theme.',
         'Articles are clean structured text.'),
        ('high', 'The homepage says “five” campuses but shows four',
         '“…five state of the art campuses across the world…” Four are listed. The Instagram feed on the same page '
         'mentions “Aljamea-tus-Saifiyah, Siddhpur”, which appears nowhere else on the site.',
         'Campus count is computed from the campus list. Siddhpur only needs a data entry to appear.'),
        ('high', 'Surat, the founding campus, has no page',
         '/surat-campus/ returns “Page not found”. The menu has no Surat link. The /karachi-campus/ URL is actually a '
         '2020 news post about a flower show.',
         'Dedicated pages for all four campuses, Surat first: the mother campus since 1810.'),
        ('medium', 'Duplicated paragraphs',
         'About: the intro paragraph appears twice, as does the emblem paragraph. Nairobi: “An emphasis on plentiful '
         'landscaping…” is repeated three times in one block. Brief History repeats the Al-Azhar paragraphs. Mumbai repeats its '
         'opening paragraph word for word.',
         'Each fact appears once, where it belongs.'),
        ('medium', 'Stale and contradictory facts',
         'Library page: the Zawāya “culminate with the present age of His Holiness Syedna Mohammed Burhanuddin RA” (he passed '
         'away in 2014). Mahad al-Zahra: Mumbai’s building is “under construction” (inaugurated 2023). Al-Azhar is founded in '
         '“365/970” on one page and “365/975” on another, and the timeline has a junk entry “0970/1005”. Karachi’s Mahad building '
         'is 1429/2008 in the timeline and 1430/2009 on the Mahad page.',
         'Updated, with a single source of truth per fact. Contradictions are listed for the office to confirm.'),
        ('medium', 'News stopped in May 2024',
         'Newest post: 9 May 2024. Before that, July 2023, then 2021. Meanwhile Instagram and X are active weekly.',
         'A news model built for frequent posting; the homepage leads with the latest three.'),
        ('low', 'Spelling and typos across the site',
         '“Burhanddin”, “comtemporary”, “healty”, “Harmonius”, “feaures”, “indeginous spieces”, “ARCHITECURE”, “langauge”, '
         '“Minsiter”, “Saifyah”, “Saifuddin TUS” glued as “SaifuddinTUS”, “Safuiddin”, “HolinessRA”.',
         'Proof-read throughout. Honorifics (RA, TUS, AS, SAW, QR) are typeset automatically as small caps.'),
    ]),
    ('Navigation & structure', [
        ('high', 'Dead menu parents',
         '“Campuses & Facilities”, “Academics” and “Faculties & Departments” link to “#”. On touch devices they do nothing.',
         'Every menu heading is a real overview page (Campuses, Academics, Campus life).'),
        ('high', 'Admissions leaves the site for an old ASP.NET login',
         'The main Admissions link goes straight to jameasaifiyah.org/Admissions/Login.aspx, a different domain and design, '
         'with no explanation of programmes, eligibility or process.',
         'A proper Admissions page explaining the three programmes and the steps, then a clear hand-off to the portal.'),
        ('medium', 'No contact page',
         'Campus addresses exist only in the footer. There is no map, no directions, and no per-campus contact.',
         'A Contact page with all four campuses, maps, phone and email, plus a campus picker.'),
        ('medium', 'Menu printed three times in the HTML',
         'Header, mobile and sticky menus are three separate copies, so screen-reader and keyboard users meet the '
         'navigation three times.',
         'One semantic header navigation that adapts to mobile.'),
        ('medium', 'No site search',
         'There is no way to search the site.',
         'Instant search (⌘K or /) across pages, campuses, faculties, luminaries and news.'),
    ]),
    ('Performance', [
        ('high', 'Very heavy pages',
         'Homepage HTML alone is 476 KB; inner pages are 290–380 KB of HTML before any image. The homepage loads 23 '
         'stylesheets and 13 scripts: Oxygen builder, Revolution Slider, MetaSlider + FlexSlider, Owl Carousel, Font Awesome '
         'loaded twice (local and CDN, plus v4 shims), AOS, two social-feed plugins and jQuery.',
         'One stylesheet and one script, no frameworks. Pages are a fraction of the size and render in a single pass.'),
        ('medium', 'Live Instagram and X widgets on the homepage',
         'Third-party feeds slow the first paint, track visitors, and show whatever was last posted, including a stray '
         '“Burhanuddin Qutbi” heading in the news list.',
         'Curated, fast social links. Selected posts can be pinned as news.'),
        ('medium', 'Images not optimised',
         'Images are served as uploaded, including PNG screenshots of photographs (e.g. Sports-complex.png, Library.png) and '
         'a 2560-px “-scaled” JPEG used inside small cards. One file is named “…May-2024.jpgTuesday-7th-May-2024…jpg”.',
         'Two sizes per photo (960 px and 2560 px) with srcset, lazy loading and async decoding.'),
    ]),
    ('Accessibility', [
        ('high', 'Images without alt text',
         '50 of 67 images on the homepage have no alt text, campus photographs included.',
         'Every image has meaningful alt text.'),
        ('high', 'Multiple H1 headings per page',
         'Most pages have 2–6 <h1> elements (e.g. “The Three Stages at a Glance” has 6), so headings mislead screen readers '
         'and search engines.',
         'Exactly one H1 per page, with a logical H2/H3 outline.'),
        ('medium', 'Page titles polluted with icon names',
         'The <title> text reads “About Us - Aljamea-Tus-SaifiyahVisit our FacebookVisit our Instagram…closebarsangle-down'
         'ellipsis-v…”, because SVG icon labels leak into the title.',
         'Clean titles: “About Aljamea · Aljamea-tus-Saifiyah”.'),
        ('medium', 'No dark mode, no reduced-motion support, small low-contrast text',
         'Fixed light theme; animations run regardless of the user’s motion setting.',
         'Day / night / auto themes, prefers-reduced-motion respected, AA contrast.'),
    ]),
    ('Search engines & sharing', [
        ('high', 'No meta description on the homepage',
         'Google writes its own snippet. The Open Graph title is the generic “Home - Aljamea-Tus-Saifiyah” and there is no '
         'share image.',
         'A description and share image for every page, plus Organization / EducationalOrganization structured data.'),
        ('medium', 'URL structure',
         'Percent-encoded Unicode slugs such as /al-da%ca%bfi-al-ajal-syedna-abde%ca%bfali-saifuddin-ra/ and '
         '/idara-al-ta%ca%bedib-wa-al-riya%e1%b8%8da-…/.',
         'Short readable URLs (/luminaries/syedna-abdeali-saifuddin). Every old URL is permanently redirected, so no '
         'search ranking is lost.'),
        ('low', 'Copyright year frozen at 2024', 'Footer: “Copyright © 2024”.',
         'The year and the Misri Hijri date update automatically.'),
    ]),
    ('Brand & storytelling', [
        ('medium', 'The Arabic identity is barely present',
         'Arabic appears only in the logo. Names such as Maktabat Aljamea or Khaima al-Riyāḍa are transliterated but '
         'never shown in Arabic script.',
         'Arabic titles throughout in Kanz al-Marjaan, Hijri dates, and a Kufic-style inscription frieze.'),
        ('medium', 'The best stories are buried',
         'The 11-level step garden, the four rivers, the thāl, 2.2 million meals a year, the Radiant Axis, the 1817 map of '
         'Darse Saifee: all hidden deep in long text.',
         'These become the site’s signature moments: an interactive eleven-year ladder, a journey map from Cairo to '
         'Mumbai, a scroll-driven timeline and animated numbers.'),
    ]),
]


def counts():
    c = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
    for _, items in AUDIT:
        for sev, *_ in items:
            c[sev] += 1
    return c


# Measured on the live site vs. this build (homepage, uncompressed). Filled in from real measurements.
METRICS = [
    ('Homepage HTML', '476 KB', '58 KB'),
    ('Stylesheets', '23 files', '1 file'),
    ('Scripts', '13 files', '1 file'),
    ('Images without alt', '50 of 67', '0'),
]
