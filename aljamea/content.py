"""All institutional text for the Aljamea-tus-Saifiyah site.

Copy is taken from jameasaifiyah.edu, proof-read (typos, duplicated paragraphs, placeholder
text and AI-generated filler removed) and restructured into pages made of typed sections:

    text    {kind, kicker?, title?, body:[para...]}
    split   {kind, kicker?, title, body:[...], img, flip?, caption?}
    quote   {kind, text, by, note?}
    facts   {kind, title?, items:[(title, body)...]}
    table   {kind, title, lead?, head:[...], rows:[[...]...]}
    list    {kind, title, items:[...]}
    gallery {kind, title?, imgs:[...]}
    stats   {kind, items:[(number, suffix, label)...]}
    stages  {kind}  (renders the eleven-year ladder)
"""
from datetime import date

INSTITUTE = dict(
    name='Aljamea-tus-Saifiyah',
    ar='الجامعة السيفية',
    tagline='The premier educational institute of the Dawoodi Bohra community',
    founded_ce=1810, founded_ah=1225,
    benefactor='His Holiness Dr Syedna Mufaddal Saifuddin TUS',
    social=dict(
        instagram='https://www.instagram.com/aljamea_tus_saifiyah/',
        x='https://twitter.com/jamea_saifiyah/',
        youtube='https://www.youtube.com/@MahadalZahraAljameatusSaifiyah',
        facebook='https://www.facebook.com/groups/aljamea.tus.saifiyah/',
    ),
    admissions_portal='https://www.jameasaifiyah.org/Admissions/Login.aspx',
)

# --------------------------------------------------------------------------- campuses
CAMPUSES = [
    dict(slug='surat', name='Surat', country='India', ar='سورت', year=1810, year_ah=1225,
         since='Darse Saifee 1225/1810 · new campus 1381/1961',
         img='ajss-00ext02-1', card='ajss-00ext02-1',
         address=['Devri Mubarak, Zampa Bazaar', 'Begampura, Surat', 'Gujarat 395003, India'],
         phone='+91 261 301 1110', email='admin.surat@jameasaifiyah.edu', lat=21.1950, lon=72.8317,
         lead='The mother campus. Darse Saifee was founded here in 1225/1810 beside the residence of '
              'the 43rd dāʿī, and rebuilt as Aljamea-tus-Saifiyah by Syedna Taher Saifuddin RA in 1381/1961.',
         sections=[
             dict(kind='split', kicker='Where it began', title='Darse Saifee, 1810',
                  body=['In 1225/1810, the 43rd dāʿī Syedna Abdeʿali Saifuddin RA built an academy in Surat with '
                        'rooms for teaching, residences for students and a masjid. He placed it beside his own '
                        'residence to show how much he valued education and those who seek it.',
                        'A British Revenue Survey plan of Surat from 1817 already marks the “mudrusa or college”: a '
                        'building of several floors around a central courtyard where 200 boys, some from as far as '
                        'Agra and Delhi, lived and studied.'],
                  img='sas-map', caption='Plan of the City of Surat, 1817 — Darse Saifee is marked no. 4.'),
             dict(kind='split', kicker='A new chapter', title='Aljamea-tus-Saifiyah, 1961', flip=True,
                  body=['In 1381/1961 Syedna Taher Saifuddin RA built a new campus in Surat. English, the sciences '
                        'and the humanities joined the curriculum, and the academy took the name Jāmiʿa, the Arabic '
                        'for university.',
                        'Its first visitor of state, on 22 June 1960, was Pandit Jawaharlal Nehru, the first Prime '
                        'Minister of India.'],
                  img='innaugaration-jamea-surat'),
             dict(kind='facts', title='On campus', items=[
                 ('Masākin Mohammediya', 'The boys’ residence, inaugurated in 1404/1983. Its balconies carry a '
                  'honeycomb pattern: students, like bees, gather from many flowers to make something beneficial.'),
                 ('Rabwat Jibla', 'The girls’ residence, inaugurated with the new īwān in 1408/1988.'),
                 ('Mahad al-Zahra', 'A dedicated building for Quranic studies since 1419/1999, with voice-training '
                  'rooms, anechoic chambers, waterfalls and indoor koi ponds.'),
                 ('Solar since the 1980s', 'Solar water heating has served the Surat dormitories since the early 1980s.'),
             ]),
             dict(kind='gallery', title='Surat in pictures', imgs=['ajss-19masakin04', 'ajss-05mahad18', 'ajss-05mahad20',
                                                                     'ajss-09antiquarian03', 'ajss-15sewingroom02', '360']),
         ]),
    dict(slug='karachi', name='Karachi', country='Pakistan', ar='كراتشي', year=1983, year_ah=1404,
         since='Classes 1385/1965 · campus 1404/1983',
         img='stj05090-302x400', card='stj05090-302x400',
         address=['St-8, Block-C, North Nazimabad', 'Karachi 74700, Pakistan'],
         phone='+92 21 3863 6600', email='admin.karachi@jameasaifiyah.edu', lat=24.9420, lon=67.0400,
         lead='Classes for years one to four began in Karachi in 1385/1965. Syedna Mohammed Burhanuddin RA '
              'laid the foundation of a dedicated campus in 1389/1969 and inaugurated it in 1404/1983.',
         sections=[
             dict(kind='split', kicker='A sister academy', title='Mirroring Surat',
                  body=['The Karachi campus mirrored the academic and architectural components of its sister academy '
                        'in Surat. At its inauguration in 1984, Syedna Burhanuddin RA said that the community’s '
                        'beliefs had been immortalised in the arches and stones of these buildings.',
                        'A second Mahad al-Zahra building was inaugurated here in 1429/2008.'],
                  img='innaugaration-jamea-karachi'),
             dict(kind='split', kicker='Gardens of knowledge', title='A Quranic garden, first in Pakistan', flip=True,
                  body=['The campus has the first Quranic garden in Pakistan. A ring of coconut palms along the sports '
                        'field prevents waterlogging on campus and in the neighbouring homes.',
                        'In February 2020 the auditorium garden won second prize in the University Gardens category '
                        'of the 69th Pakistan Annual Flower Show, presented by President Arif Alvi.'],
                  img='audi-1'),
             dict(kind='gallery', title='Karachi in pictures', imgs=['audi-2', 'mahad-al-zahra-building-karachi', 'karachi-1']),
         ]),
    dict(slug='nairobi', name='Nairobi', country='Kenya', ar='نيروبي', year=2017, year_ah=1438,
         since='Announced 1432/2011 · inaugurated 1438/2017',
         img='ajsn-09radaxis02-bl-1179', card='ajsn-05baabnasr01-bl-1738-2',
         address=['Saifee Park, Syedna Mohammed Burhanuddin Road', 'Langata, Nairobi 00100, Kenya'],
         phone='+254 20 765 0283', email='admin.nairobi@jameasaifiyah.edu', lat=-1.3330, lon=36.7650,
         lead='Announced by Syedna Mohammed Burhanuddin RA on his 100th birthday, the Nairobi campus brought a '
              'movement that began with the Fatimi imams of North Africa back to the continent it came from.',
         sections=[
             dict(kind='stats', items=[(12, ' acres', 'Campus site'), (18, '', 'Buildings'),
                                       (900, 'k ft²', 'Carpet area'), (1000, '+', 'Residential students')]),
             dict(kind='split', kicker='The competition', title='Designed by the world',
                  body=['Soon after the announcement, the rectors invited scores of international architecture firms '
                        'to a design competition. Four were shortlisted in 2012. After a final round at His Holiness’ '
                        'residence in Mumbai, a team of FXFowle, Frederic Schwartz Architects (later ROMINES '
                        'Architecture), Burhani Design-Build and consultants was chosen.',
                        'The brief: an educational campus inspired by Islamic ideals, embodying Fatimi architecture '
                        'and culture, and infused with the design and technology of the 21st century.'],
                  img='jamea-nairobi-the-begining-of-construction'),
             dict(kind='split', kicker='Built against the clock', title='From foundation to examinations', flip=True,
                  body=['Syedna Mufaddal Saifuddin TUS laid the foundation at the end of 2013 on his father’s behalf. '
                        'After the passing of Syedna Burhanuddin RA months later, he directed that construction '
                        'continue with renewed zeal, as a legacy celebrating his father’s love for Aljamea.',
                        'Phasing was abandoned for an accelerated schedule. When His Holiness asked for the campus to '
                        'host the 2016/17 annual examinations, thousands of volunteers, students and faculty among them, '
                        'cleared debris, planted trees and painted walls to finish more than a year’s work in months.'],
                  img='dji00052-2'),
             dict(kind='facts', title='Salient features', items=[
                 ('The Radiant Axis', 'A central corridor running east–west along the daily path of the sun.'),
                 ('Fatimi architecture', 'Elements, layouts and motifs from North Africa, Egypt, Yemen and India, '
                  'each recalling a period of the community’s history.'),
                 ('Inscribed walls', 'Quranic verses and Arabic prose and poetry in several scripts on the major façades.'),
                 ('A shoeless culture', 'Covered walkways, corridors and bridges let students cross the whole campus '
                  'barefoot, as at home.'),
                 ('A Jamea within a garden', 'One third of the campus is green space, with more than 250 trees, '
                  'Quranic species beside indigenous ones.'),
                 ('A breathing building', 'Passive ventilation, large-scale glazing, rainwater harvesting, composting, '
                  'solar heating and photovoltaics, built to LEED requirements.'),
                 ('Digital backbone', 'Fibre-optic network, building management system, campus-wide Wi-Fi, RFID '
                  'access control and AV broadcast in most buildings.'),
                 ('Saahat roof, 2023', 'An ETFE canopy over the central courtyard, on columns shaped like date palms, '
                  'shades the 36 palms beneath it while letting UV light through.'),
             ]),
             dict(kind='quote', text='The quality indeed that we have seen today of the physical facilities in this '
                  'complex attest to the readiness and commitment, to the vision and mission of education in Kenya.',
                  by='Mr Uhuru Kenyatta', note='President of Kenya, at the inauguration, April 2017'),
             dict(kind='gallery', title='Nairobi in pictures',
                  imgs=['ajsn-05baabnasr01-bl-1738-2', 'ajsn-08minaret03-dl-3498', 'ajsn-03mahad04-bl-7874',
                        'ajsn-02eiwan02-extrukn-1122', 'ajsn-03mahad08-hallway-0702', 'ajsn-05baabtawfeeq01-0024',
                        'ajsn-07ruwaaq01-male-0854', 'ajsn-15maktabat02-kehf-0165', 'moula-nairobi-saahat-roof-opening-02']),
         ]),
    dict(slug='mumbai', name='Mumbai', country='India', ar='ممبئ', year=2023, year_ah=1444,
         since='Announced 1434/2013 · inaugurated 10 February 2023',
         img='ajsm-05baabshot2-fw', card='ajsm-06sahatshot7-5032',
         address=['3 Bori Colony, Marol', 'Andheri East, Mumbai', 'Maharashtra 400059, India'],
         phone='+91 22 2831 7500', email='admin.marol@jameasaifiyah.edu', lat=19.1150, lon=72.8800,
         lead='The dream of Syedna Abdulqadir Najmuddin RA, realised by his descendant Syedna Mufaddal Saifuddin TUS '
              'in the city that is the administrative home of the Dawat and the largest Bohra settlement in the world.',
         sections=[
             dict(kind='split', kicker='Entrance', title='Bab Zuwayla',
                  body=['The main gate replicates Bab Zuwayla, built in 1091 CE by Badr al-Jamali, vizier of Imam '
                        'al-Mustansir bi Allah AS, and one of the four surviving gates of al-Qahira, the Fatimi '
                        'city of Cairo.',
                        'It marks the academy as a repository of the intellectual and cultural heritage of the Fatimi '
                        'imams and their duʿāt.'],
                  img='ajsm-05baabshot2-fw'),
             dict(kind='split', kicker='Prayer hall', title='Stone from Yemen, a mihrab from Cairo', flip=True,
                  body=['The prayer hall replicates al-Jāmiʿ al-Azhar: high pointed arches, decorative grilles and '
                        'the Azhar lantern motif, echoed in custom glass lanterns on the columns.',
                        'All of its stone was quarried in Yemen, the same stone as Masjid Mansoor al-Yemen in al-Hutaib '
                        'al-Mubarak. The mihrab, patterned on al-Azhar’s, is carved from white Makrana marble.'],
                  img='ajsm-01masjidshot1-0076'),
             dict(kind='split', kicker='Ceremonial hall', title='The Īwān',
                  body=['The īwān is the academy’s identity: classroom, pulpit and congregation hall. In Mumbai it '
                        'borrows from the Ujjain mausoleum of three duʿāt, with scalloped arches cascading from a '
                        'single point, like knowledge spreading outward, or a voice echoing.',
                        'Its hand-carved wooden bethak carries a grape-and-vine motif. In Fatimi thought, grapes '
                        'signify knowledge.'],
                  img='ajsm-02eiwanshot1-4235fw'),
             dict(kind='split', kicker='A beacon of Quranic learning', title='Mahad al-Zahra', flip=True,
                  body=['An octagonal building, after the verse describing the Throne borne by eight, crowned by a '
                        'dome lined entirely with muqarnas, the honeycomb vaulting the Fatimi imams brought to Egypt. '
                        'It is beautiful and it is acoustic: it carries the voices of students reciting below.',
                        'Twelve sayings of Amirul Mumineen Imam Ali AS on the Quran ring the base of the dome. '
                        'Doors and walkways join the Mahad, the īwān and the masjid into one continuous space.'],
                  img='ajsm-03mahadshot9-5834'),
             dict(kind='split', kicker='Central courtyard', title='Eleven steps, four rivers',
                  body=['The sāhat holds a step garden of eleven levels, one for each year a student may spend at the '
                        'academy, rising in knowledge and discernment.',
                        'Its water feature draws from four sources into a central pool and divides again into four '
                        'streams, illustrating Syedna Taher Saifuddin RA’s words: Aljamea is an estuary into which '
                        'the streams of knowledge and the rivers of the arts flow from every direction. The minaret is '
                        'an exact replica of the western minaret of al-Jāmiʿ al-Anwar.'],
                  img='ajsm-06sahatshot4-2713with-students'),
             dict(kind='split', kicker='Auditorium', title='A palace modelled on creation', flip=True,
                  body=['The auditorium is inspired by a parable in the Rasāʾil Ikhwān al-Safāʾ, in which a wise king '
                        'builds a palace for his children that mirrors all of creation. Its interior references minerals, '
                        'plants, animals and human beings.',
                        'Here, each year, students of year eleven defend their dissertations.'],
                  img='ajsm-audi1-7533'),
             dict(kind='split', kicker='Dining hall', title='The Mawāʾid',
                  body=['A homage to Syedna Ismaʿil Badruddin RA: carved woodwork from his surviving haveli in Jamnagar, '
                        'walls inscribed with verses on the māʾida and traditions on blessed foods.',
                        'It seats about 550, cooks lunch and dinner for as many daily, and delivers 160 meals twice a '
                        'day to faculty households.'],
                  img='ajsm-04mawaidshot2-4919'),
             dict(kind='split', kicker='Library', title='Qāʿat al-Zawāya al-Fatimiyya', flip=True,
                  body=['Three floors, each for a level of academic maturity, with online subscriptions, tablets, '
                        'discussion rooms and a digital catalogue.',
                        'Its heart is the Hall of Fatimi Corners: six corners for six eras, converging on a centre '
                        'dedicated to the Quran, the fountainhead of knowledge in every epoch.'],
                  img='ajsm-14zawiyashot1-4347'),
             dict(kind='split', kicker='Residences', title='Two towers, one bridge',
                  body=['Two eight-floor residences, for male and female students, house 260 students each. A glass '
                        'bridge on the sixth floor connects them to the academic building.',
                        'Every floor has a kitchen, where students take turns cooking breakfast for the whole floor and '
                        'handle the budget and shopping themselves. Both residences have a gym and a pool. The girls’ '
                        'rooftop pool echoes the surrounding hills; the boys’ is inspired by Juhu beach.'],
                  img='ajsm-19rabvatshot1-1177'),
             dict(kind='quote', text='Today, as the country starts its journey towards the ‘Golden Era’ of its '
                  'independence, the importance of this contribution of the Bohra community in the field of education '
                  'is all the more significant.', by='Shri Narendra Modi',
                  note='Prime Minister of India, inaugurating the Mumbai campus, 10 February 2023'),
             dict(kind='gallery', title='Mumbai in pictures',
                  imgs=['ajsm-01masjidshot4-0032-1', 'ajsm-02eiwanshot3-0021fw', 'ajsm-03mahadshot2-0427fw',
                        'ajsm-22corridorshot1-3oo6', 'ajsm-22staircaseshot3-3332', 'ajsm-detail-1893fw',
                        'ajsm-11boysclassroomshot3-0895-1', 'ajsm-13libraryshot3-0026', 'photo-2023-02-10-19-23-00']),
         ]),
]
CAMPUS = {c['slug']: c for c in CAMPUSES}

# --------------------------------------------------------------------------- the journey (map)
JOURNEY = [
    dict(city='Cairo', ar='القاهرة', year='365/970', lon=31.24, lat=30.04,
         text='Al-Imam al-Muʿizz li Deen Allah AS founds al-Azhar, among the oldest universities still teaching.'),
    dict(city='Cairo', ar='دار العلم', year='395/1005', lon=31.24, lat=30.04,
         text='Al-Imam al-Hakim bi Amr Allah AS opens the House of Knowledge, its library open to all.'),
    dict(city='Yemen', ar='اليمن', year='526/1132', lon=43.9, lat=15.35,
         text='With the seclusion of the 21st imam, the duʿāt carry the tradition of learning to Yemen.'),
    dict(city='Ahmedabad', ar='أحمد آباد', year='946/1539', lon=72.57, lat=23.02,
         text='The seat of the Dawat moves to India; learning continues, sometimes on rooftops at night.'),
    dict(city='Surat', ar='سورت', year='1225/1810', lon=72.83, lat=21.17,
         text='Syedna Abdeʿali Saifuddin RA builds Darse Saifee, the academy that becomes Aljamea.'),
    dict(city='Karachi', ar='كراتشي', year='1404/1983', lon=67.01, lat=24.86,
         text='A second campus mirrors Surat across the Arabian Sea.'),
    dict(city='Nairobi', ar='نيروبي', year='1438/2017', lon=36.82, lat=-1.29,
         text='Learning returns to Africa, the continent where it flowered under the Fatimi imams.'),
    dict(city='Mumbai', ar='ممبئ', year='1444/2023', lon=72.88, lat=19.11,
         text='The fourth campus opens in Marol, at the heart of the community.'),
]

# --------------------------------------------------------------------------- the eleven-year ladder
STAGES = [
    dict(n='1', years=(1, 4), name='Thaqāfat ʿĀmmah', en='General Culture', ar='الثقافة العامة',
         degree='Mubtaghi al-ʿIlm', degree_en='Seeker of Knowledge',
         comparable='Associate degree in Islamic & Arabic studies · SSC / GCSE',
         points=['Fatimi jurisprudence, history and literature through Syedna al-Qadi al-Nuʿman RA: Sharh al-Akhbār and Daʿāʾim al-Islam.',
                 'The natural and social sciences, read alongside the Quran and the history of scientific discovery in Islam.',
                 'Basic proficiency in Arabic and intermediate fluency in English.',
                 'Memorisation of the entire Quran, with the art of recitation and the Quranic sciences.']),
    dict(n='2a', years=(5, 7), name='al-Jāmiʿiyya al-Ūlā', en='Collegiate I', ar='الجامعية الأولى',
         degree='Al-Faqīh', degree_en='The Jurist',
         comparable='Licentiate in Islamic & Arabic studies · HSC / GCE A Level',
         points=['Further jurisprudential works of Syedna al-Qadi al-Nuʿman RA, studied in depth.',
                 'The philosophical and disputational works of Syedna Ahmed Hamiduddin al-Kirmani RA.',
                 'Critical study of primary Islamic texts.']),
    dict(n='2b', years=(8, 9), name='al-Jāmiʿiyya al-Thāniya', en='Collegiate II', ar='الجامعية الثانية',
         degree='Al-Faqīh al-Mutqin', degree_en='The Competent Jurist',
         comparable='Bachelor’s in Arabic & Islamic studies',
         points=['Specialisation in Literature, History or Jurisprudence; groundwork for the dissertation in term papers in Arabic and English.',
                 'The 800 majālis of Syedna al-Muʾayyad al-Shirazi RA: philosophy, theology and ethics in disputation.',
                 'An elective language: French, German, Sanskrit or Persian.',
                 'Training in discourse and sermon delivery; many students lead the nine sermons of ʿAshara Mubāraka.']),
    dict(n='3', years=(10, 11), name='al-Dirāsāt al-ʿUlyā wa al-Takhassus', en='Higher Studies & Specialisation',
         ar='الدراسات العليا والتخصص', degree='Al-Faqīh al-Jayyid', degree_en='The Distinguished Jurist',
         comparable='Master’s in Islamic and/or Arabic studies',
         points=['Independent research, scholarship and teaching, with higher-order critical and creative thinking.',
                 'Applying Fatimi principles to contemporary issues.',
                 'Dissertation submitted at the end of year ten and defended in open forum in year eleven.',
                 'Graduates are assigned roles in the community, careers in related fields, or further study.']),
]

GRADES = [('85 & above', 'A+'), ('70 – 84', 'A'), ('68 – 69', 'B+'), ('64 – 67', 'B'),
          ('58 – 63', 'C+'), ('48 – 57', 'C'), ('36 – 47', 'D')]

# --------------------------------------------------------------------------- faculties
FACULTIES = [
    dict(slug='philosophy', name='Philosophy', native='Hikma', ar='الحكمة', icon='star', img='ajsm-14zawiyashot1-4347',
         lead='Philosophy is one of the most important subjects at Aljamea. The fifty-two epistles of Ikhwān al-Safāʾ, '
              'composed by Imam Ahmad al-Taqi AS, form its basis and are studied throughout the last three stages.',
         sections=[
             dict(kind='text', body=['Imam Ahmad AS classified philosophy into four broad fields of knowledge: physical, '
                  'logical, empirical and spiritual. Students move through them in sequence, from the tangible to the '
                  'metaphysical.',
                  'The philosophical works of Syedna Hamiduddin al-Kirmani RA and Syedna Taher Saifuddin RA are central '
                  'to the course, read alongside other major thinkers and philosophers.']),
             dict(kind='table', title='Core topics', head=['Stage', 'Topics'], rows=[
                 ['2', 'Volume I of the Rasāʾil Ikhwān al-Safāʾ: mathematics, geometry, music, astronomy.'],
                 ['3', 'Volumes II and III: logic and an introduction to the philosophy of the empirical sciences. '
                       'Philosophical works of Syedna Hamiduddin al-Kirmani RA. Introduction to classical philosophy.'],
                 ['4', 'Volume IV: the spiritual sciences, philosophy of theology and of Islamic jurisprudence. Modern '
                       'and post-modern philosophy. The Islamic philosophical and kalām tradition. Selected treatises '
                       'of Syedna al-Kirmani RA.'],
             ]),
         ]),
    dict(slug='literature', name='Literature', native='Adab', ar='الأدب', icon='pen', img='ajsn-15maktabat11-readroom-2355',
         lead='From al-Mutanabbi to Shakespeare: students read Fatimi Arabic literature in depth, alongside the great '
              'poets of Arabic, Urdu, Lisān al-Daʿwa and English.',
         sections=[
             dict(kind='text', body=['Fatimi Arabic texts studied include the works of al-Syed al-Amīr Tamīm, Syedna '
                  'al-Muʾayyad al-Shirazi RA, Syedna Ali bin Mohammed al-Walīd RA, Syedna Taher Saifuddin RA and '
                  'Syedna Mohammed Burhanuddin RA. The literature of Lisān al-Daʿwa, including Syedi Abdeʿali '
                  'ʿImaduddin QR, Syedi Sadiqʿali Saheb QR and Syedi Luqmanjee Saheb QR, is integral to the course.',
                  'Al-Mutanabbi, Ibn Hāni al-Andalusi, al-Sharif al-Radi and Ahmed Shawqi are read with the major poets '
                  'of the English language.']),
             dict(kind='list', title='The study of literature covers', items=[
                 'Principles of literature', 'History of literature', 'Literary techniques',
                 'Introductory applied linguistics', 'Literary analysis', 'Literary genres',
                 'Composition', 'Oratory', 'Urdu literature']),
             dict(kind='table', title='Core topics by year', head=['Year', 'Topics'], rows=[
                 ['1 – 2', 'Quranic literature'],
                 ['3', 'Key literary figures'],
                 ['4', 'Shakespeare and his contemporaries · Victorian literature and culture · Critical perspectives'],
                 ['5', 'Pre-Islamic Arabic literature'],
                 ['6', 'Modern Arabic literature · Islamic Arabic literature'],
                 ['7', 'Comparative study of Urdu, Arabic and Lisān al-Daʿwa literature · The Maqāmāt genre'],
                 ['8 – 9', 'Classical literature · Romanticism · Contemporary writing'],
                 ['10 – 11', 'Modernism · Post-colonial writing · Arabic lexicology'],
             ]),
         ]),
    dict(slug='languages', name='Languages', native='Lughāt', ar='اللغات', icon='script', img='ajsm-12girlsclassroomshot1-4311',
         lead='Arabic, Lisān al-Daʿwa and English are the languages of instruction. From stage three, every student '
              'adds a fourth.',
         sections=[
             dict(kind='facts', items=[
                 ('Arabic', 'Taught through classical texts from the first day; Lisān al-Daʿwa, with its Arabic '
                  'lexicon and script, speeds acquisition. Grammar follows through al-Darīrī and Hidāyat al-Nahw, '
                  'and the final stages add Arabic linguistics, poetry and prose composition. Memorising the Quran '
                  'is itself a great teacher of Arabic.'),
                 ('English', 'An eclectic approach. Stages one and two build the four core skills toward secondary '
                  'and higher secondary certificates; stages three and four read thematic texts and the scholarly '
                  'literature of Islamic studies, most of which is published in English.'),
                 ('Elective languages', 'For research and graduate study, each student chooses French, German, Persian '
                  'or Sanskrit for the final four years. Nairobi students hold certificates in Persian from the '
                  'Ferdowsi University of Mashhad.'),
             ]),
         ]),
    dict(slug='jurisprudence', name='Jurisprudence', native='Fiqh', ar='الفقه', icon='scale', img='ajsm-11boysclassroomshot3-0895-1',
         lead='Students apply fiqh in real pastoral and leadership roles during Ramadan and Moharram, so it is studied '
              'with particular care. At higher stages it is read through historical, sociological and anthropological lenses.',
         sections=[
             dict(kind='text', title='Syedna al-Qadi al-Nuʿman RA',
                  body=['His texts form the basis of Fatimi jurisprudence and are studied within these frameworks: '
                        'the Quran and its interpretation; the pivotal role of the imam; the sources and validity of '
                        'directives; differences between the schools of Islamic law; and the significance of '
                        'jurisprudence for the social, economic and moral development of society.']),
             dict(kind='table', title='Core topics by year', head=['Year', 'Topics'], rows=[
                 ['1 – 3', 'Fundamental tenets of jurisprudence · Islamic socio-economics (3)'],
                 ['4', 'Sociological jurisprudence'],
                 ['5', 'Criminal jurisprudence'],
                 ['6', 'Marital jurisprudence · The Hanafī school'],
                 ['7', 'Economic jurisprudence · The Mālikī school'],
                 ['8 – 9', 'Theological jurisprudence · The Shāfiʿī and Jaʿfarī schools'],
                 ['10 – 11', 'Political jurisprudence · The Hanbalī school · Oriental and Occidental perspectives'],
             ]),
         ]),
    dict(slug='history', name='History', native='Akhbār', ar='الأخبار', icon='scroll', img='al-azhar-university',
         lead='The works of Syedna al-Qadi al-Nuʿman RA and Syedna Idris Imaduddin RA are the foundation, read with '
              'al-Maqrizi, Ibn Muyassar, Ibn Khallikān and Ibn Khaldūn, and with modern historians of Islam.',
         sections=[
             dict(kind='list', title='Themes across every stage', items=[
                 'The Quran as a historical text', 'Principles of historical study', 'Historiography of Islam',
                 'How historians differ in perspective and interpretation', 'Study and classification of sources',
                 'Contributions of Fatimi historians', 'Heresiographies and their impact']),
             dict(kind='table', title='Core topics by year', head=['Year', 'Topics'], rows=[
                 ['1 – 2', 'Early Islam'],
                 ['3', 'Formation of the Islamic world · The Indus Valley civilisation · South Asia and East Africa'],
                 ['4', 'Classical Islamic history: Abbasids, Umayyads, Safavids, Ottomans, Mughals · Colonial South Asia and independence'],
                 ['5', 'Duʿāt Mutlaqūn in Yemen · Duʿāt Mutlaqūn in India · Important Islamic historians'],
                 ['6', 'The Fatimi state in North Africa and Egypt'],
                 ['7', 'Modern and contemporary historians'],
                 ['8 – 9', 'Modern and post-modern history · Historical criticism'],
                 ['10 – 11', 'Orientalism and Occidentalism · Critique of historical method · Philosophy of history'],
             ]),
         ]),
    dict(slug='sciences', name='Empirical & Social Sciences', short='Sciences', native='ʿUlūm', ar='العلوم', icon='atom', img='ajsn-16labbio01-3869',
         lead='“Allah has established His religion in the image of His creation.” To understand Islam, one must '
              'understand the structures of the empirical world.',
         sections=[
             dict(kind='text', body=['The curriculum also prepares students for secondary and higher secondary '
                  'certificate examinations. The Department of External Examinations handles registration, '
                  'admission, tuition and transport for students pursuing these disciplines at other institutions.',
                  'In Nairobi, more than 30 students and faculty study business alongside Aljamea through a '
                  'collaboration with Strathmore University.']),
             dict(kind='table', title='Core topics', head=['Years', 'Topics'], rows=[
                 ['1 – 4', 'Biology · Chemistry (3) · Citizenship education · Geography · Mathematics'],
                 ['4 – 7', 'Commerce · Economics · Sociology'],
                 ['8', 'Physical and human geography of the Muslim world'],
                 ['9', 'Philosophy of Islamic architecture · Legal history of Dawat-e-Hadiyah · Major world religions'],
                 ['10', 'Applied Islamic architecture · Psychology'],
                 ['11', 'Linguistics · Political science'],
             ]),
         ]),
]
FACULTY = {f['slug']: f for f in FACULTIES}

# --------------------------------------------------------------------------- departments
DEPARTMENTS = [
    dict(slug='mahad-al-zahra', name='Mahad al-Zahra', ar='معهد الزهراء', en='Quranic studies, since 1396/1976',
         img='ajsm-03mahadshot1-3785',
         lead='Founded in 1396/1976 by Syedna Mohammed Burhanuddin RA, Mahad al-Zahra is devoted to the memorisation and '
              'study of the Quran. Students aim to memorise all of it in their first stage, together with recitation, '
              'grammar, pronunciation and exegesis.',
         sections=[
             dict(kind='split', kicker='Facilities befitting the cause', title='Waterfalls, koi and anechoic chambers',
                  body=['Every campus places Mahad al-Zahra at its heart. Surat’s building opened in 1419/1999, Karachi’s in '
                        '1430/2009, and Nairobi’s, at the very centre of the campus, in 1438/2017. Mumbai’s is the octagon '
                        'beneath a muqarnas dome.',
                        'Voice-training rooms, anechoic chambers, waterfalls, gardens and indoor koi ponds all serve one '
                        'purpose: better memorisation.'],
                  img='ajss-05mahad20'),
             dict(kind='split', kicker='Community outreach', title='From Chicago to Sanaa', flip=True,
                  body=['Instructors travel to cities from Chicago to Sanaa for 30-day Ramadan programmes. Permanent '
                        'residential and day programmes across South Asia, the Gulf, Europe, the UK, East Africa and '
                        'the USA help children memorise the Quran in four years alongside regular school.',
                        'e-Learning Quran, begun in 1425/2005, was the first of its kind: virtual classes with one-to-one '
                        'recital by video. In 1440/2019 alone, 920 people completed memorisation of the Quran.'],
                  img='online-learning-2'),
             dict(kind='split', kicker='Quranic arts', title='Funūn al-Quran',
                  body=['Calligraphy, geometric design and floral ornament derived from the words of the Quran. The '
                        'department works in Kūfī, Naskh, Thuluth, Dīwānī and Riqʿa, as well as graphic and digital media.',
                        'It is restoring roughly four thousand metres of Kufic Quranic inscription along the arcades of '
                        'al-Jāmiʿ al-Anwar in Cairo.'],
                  img='ajsm-detail-4025fw'),
             dict(kind='split', kicker='Recording & sound studio', title='Janāh al-Tarannum', flip=True,
                  body=['In Mahad al-Zahra’s basement, a studio tuned for Quranic recitation and poetry, used for voice '
                        'therapy, phonation and recording. For more than thirty years it has published Saut al-Imān, '
                        'the Voice of Belief, a series of devotional poetry.'],
                  img='ajsm-03mahadshot4-5262'),
         ]),
    dict(slug="tadib", name='Idāra al-Taʾdīb wa al-Riyāḍa', ar='إدارة التأديب والرياضة', en='Personality development',
         img='about-1',
         lead='Fatimi philosophy holds that education must instil virtue and refine character. Balancing compassion with '
              'discipline, this department helps students live by the values they learn in class.',
         sections=[
             dict(kind='facts', items=[
                 ('Mūʾaddibs', 'Senior faculty serve as counsellors to groups of about fifteen students drawn from every '
                  'stage, so seniors support juniors in study and in life.'),
                 ('Every Saturday', 'Each group meets its mūʾaddib weekly, and students may seek individual counsel at any time.'),
                 ('Twenty-three attributes', 'Sessions follow the 23 attributes of personality set out by Shahzada '
                  'Dr Yusuf Najmuddin QR: appearance, spending, demeanour, use of time, hobbies, thinking and more.'),
                 ('Beyond grades', 'Academic performance is never the only measure of a student’s progress.'),
             ]),
         ]),
    dict(slug='dissertations', name='The Department of Dissertations', ar='قسم الرسائل', en='Research & the viva voce',
         img='ajsm-audi1-7533',
         lead='Students submit their dissertations at the end of year ten and defend them in year eleven before examiners, '
              'faculty and senior students, in public.',
         sections=[
             dict(kind='text', body=['A good dissertation shows scholarly attainment, critical analysis and coherent '
                  'argument. It must engage Fatimi scholarship and evaluate relevant traditional and modern scholarship.',
                  'Unusually, the chair of each defence opens with a short discourse on the topic. The defences are a '
                  'much-anticipated public event, attended by alumni and community members and sometimes the rectors. '
                  'The department guides students from narrowing a topic to permissions, supervision and academic writing.']),
             dict(kind='table', title='Sample dissertation topics', head=['Specialisation', 'Topic'], rows=[
                 ['Jurisprudence', 'Food hygiene: comparing Islamic legal discourse with current practice in the community'],
                 ['Jurisprudence', 'The manifestations of “patience” and its virtues in Islamic law'],
                 ['Jurisprudence', 'Community marriage rituals: a sociological study'],
                 ['History', 'The Qarāmita and their origins'],
                 ['History', 'The political insight of Amir al-Mumineen Ali bin Abi Talib AS in appointing his governors'],
                 ['Literature', 'Philosophical standpoints in the poetry of early Yemeni poets'],
                 ['Literature', 'The ʿĀshura sermon: a case study of ideal oratory and practice'],
             ]),
         ]),
    dict(slug='research', name='Centre for Research', ar='مركز البحث', en='Critical editions & the Majalla',
         img='ajss-09antiquarian03',
         lead='The Centre produces scholarship in Fatimi studies that protects the sanctity of the tradition while opening '
              'its thought, philosophy and history to readers.',
         sections=[
             dict(kind='text', body=['It publishes an annual series of commentaries on the literary works of Syedna Taher '
                  'Saifuddin RA, and memoirs of Syedna Mohammed Burhanuddin RA’s historic visits to North Africa and Yemen.',
                  'Its critical editions are emended from multiple manuscripts in the academy’s collection and, in the '
                  'centuries-old tradition, are handwritten, with endnotes and indices added as study aids. Published '
                  'works include Syedna al-Qadi al-Nuʿman RA’s sixteen-volume Sharh al-Akhbār and Syedna Hamiduddin '
                  'al-Kirmani RA’s Kitāb al-Masābīh.',
                  'The Centre also edits Majallat Aljamea-tus-Saifiyah, the academy’s scholarly journal.']),
         ]),
    dict(slug='cultural-activities', name='Centre for Cultural Activities', ar='مركز النشاطات الثقافية', en='Beyond the classroom',
         img='ajss-15sewingroom02',
         lead='Tours and field trips, guest lectures, class presentations and cultural commemorations through the year.',
         sections=[
             dict(kind='text', title='Life Skills, Arts & Crafts',
                  body=['Nutrition, cooking, sewing, clothing design, health care, budgeting and home décor; sketching, '
                        'fabric and glass painting, paper craft and crochet, with platforms for students to show their work. '
                        'Vocational options include graphic design, music, programming and photography, in-house or with '
                        'partner institutions.']),
         ]),
]
DEPARTMENT = {d['slug']: d for d in DEPARTMENTS}

# --------------------------------------------------------------------------- campus life / facilities
FACILITIES = [
    dict(slug='residences', name='Student Residences', native='Masākin Mohammediya & Rabwat Jibla', ar='المساكن',
         img='ajsn-18maskan02-3694', stat=('1,000+', 'residents in Nairobi alone'),
         lead='A home away from home, where the values of the classroom are lived.',
         sections=[
             dict(kind='text', body=['Most students share rooms of three to eight; seniors have single rooms on some '
                  'campuses. Each residence has its own laundry, canteen, infirmary and common rooms.']),
             dict(kind='split', kicker='The birds’ nest', title='Many places, one home',
                  body=['For many, it is the first time living away from home. Students become independent and resourceful, '
                        'save time otherwise spent commuting, and make friends from many cities and countries.',
                        'Nairobi’s Maskan is clad in a weave of wooden planks, a bird’s nest: many backgrounds woven into '
                        'one sanctuary.'],
                  img='ajsn-19rabvat01-0795'),
             dict(kind='split', kicker='A hive of activity', title='Breakfast is on the students', flip=True,
                  body=['Students take turns cooking breakfast for their whole floor, and look after their own rooms and '
                        'hostel. Responsibilities like these build character and a sense of belonging.',
                        'In Surat, the honeycomb balconies of Masākin recall bees gathering from many flowers to make honey.'],
                  img='ajss-19masakin04'),
         ]),
    dict(slug='sports', name='Sports Complex', native='Khaima al-Riyāḍa', ar='خيمة الرياضة',
         img='ajss-22kr-football01', stat=('10', 'sports on campus'),
         lead='The Prophet Mohammed SAW encouraged teaching children swimming, horse riding and archery. Body and soul '
              'depend on each other.',
         sections=[
             dict(kind='list', title='Facilities', items=['Cricket', 'Football', 'Basketball', 'Volleyball', 'Tennis',
                  'Badminton', 'Squash', 'Table tennis', 'Swimming', 'Fitness']),
             dict(kind='text', body=['Aljamea’s cricket and volleyball teams compete successfully in domestic '
                  'tournaments. In 2020 Surat faculty member Mustafa F Shakir won three bronze medals at the 9th National '
                  'Field Indoor Archery Championship.']),
             dict(kind='gallery', imgs=['ajss-22kr-badminton01', 'ajss-22kr-swimming', 'ajss-22kr-tt01',
                                        'ajss-22kr-squash01', 'ajss-22kr-gym01', 'ajsn-18maskan13-swimmingpool-2872']),
         ]),
    dict(slug='dining', name='Dining Hall', native='Al-Mawāʾid', ar='الموائد',
         img='ajsm-04mawaidshot3-0194', stat=('2.2M', 'meals a year'),
         lead='Since the 34th dāʿī fed students in Jamnagar, the duʿāt have nourished body and soul alike.',
         sections=[
             dict(kind='stats', items=[(3000, '', 'People served daily'), (2.2, 'M', 'Meals a year'), (9, '', 'At each thāl')]),
             dict(kind='split', kicker='The thāl', title='Eight or nine around one plate',
                  body=['Meals are eaten from a thāl, a large platter shared by eight or nine. It speaks of Islam’s '
                        'egalitarianism, and the circle invites conversation.',
                        'Students in their final two years serve their colleagues, in keeping with Fatimi teaching on '
                        'gracious hosting. Menus are planned with nutritionists, and hygiene is paramount.'],
                  img='ajsn-04mawaid13-girls-5358'),
         ]),
    dict(slug='library', name='Library', native='Maktabat Aljamea', ar='مكتبة الجامعة',
         img='ajsm-14libraryshot4-4218', stat=('1,000', 'year-old manuscripts'),
         lead='Multi-level reference and circulation sections, century-old periodicals, and a rare-book collection holding '
              'manuscripts nearly a thousand years old.',
         sections=[
             dict(kind='split', kicker='The Hall of Niches', title='Qāʿat al-Zawāya al-Fatimiyya al-ʿIlmiyya',
                  body=['Sections meet in corners, as views meet in conversation. Each zāwiya holds a period of Fatimi '
                        'history, from the Prophet Mohammed SAW to the present.',
                        'The Quran’s zāwiya sits at the centre: revelation at the heart of all knowledge, and the imam or '
                        'dāʿī of every age as the pivot around which the rest revolves.'],
                  img='ajsm-14zawiyashot1-4347'),
             dict(kind='text', body=['The Rare Book Section is open to researchers from Aljamea and beyond, and holds some '
                  'of the most exquisite manuscripts of the Holy Quran.']),
         ]),
    dict(slug='computer-lab', name='Computer Lab & Language Centre', native='Al-Maʿmal', ar='المعمل',
         img='ajsn-15maktabat15-complabgirls-4910', stat=('50+', 'terminals'),
         lead='Computing for coursework and research, with training in multimedia, software, operating systems, photo '
              'editing and word processing.',
         sections=[dict(kind='text', body=['With more than fifty terminals, the lab hosts whole classes and group '
                                           'presentations while serving those who prefer to learn at their own pace.'])]),
    dict(slug='auditorium', name='The Auditorium', native='Al-Qāʿa', ar='القاعة',
         img='ajsn-17auditorium01-1171', stat=('Yr 11', 'dissertation defences'),
         lead='Lectures, symposiums and the viva voce of dissertations. Also a venue for inter-community events and outreach.',
         sections=[dict(kind='gallery', imgs=['ajsn-17auditorium03-1330', 'ajsm-audi1-7533', 'audi-1'])]),
]
FACILITY = {f['slug']: f for f in FACILITIES}

# --------------------------------------------------------------------------- luminaries
LUMINARIES = [
    dict(slug='syedna-ismail-badruddin', name='Syedna Ismaʿil Badruddin', hon='RA', title='Al-Dāʿī al-Ajal', rank='34th al-Dāʿī al-Mutlaq',
         dates='d. 1085/1674', img='jamnagar', theme='He vowed to nourish students',
         lead='After years of persecution, including the martyrdom of Syedna Qutbuddin al-Shaheed RA in 1056/1646, '
              'his tenure was one of prosperity and bounty.',
         sections=[
             dict(kind='text', body=['Having served seven of his predecessors in Ahmedabad, he vowed that if the rank of '
                  'dāʿī came to him he would feed the students of the academy every day. He kept that vow, and, despite '
                  'his age, was renowned for his devotion to prayer and to teaching.',
                  'Today the Mawāʾid’s millions of meals a year descend from that vow.']),
             dict(kind='quote', text='“I have toiled in the service [of the duʿāt] to such an extent that if the body’s '
                  'extremities were made of gold or silver, they would have worn away… If the rank of daʿwa comes to me, '
                  'I will feed the seekers of knowledge.” He did, and this tradition exists until this very day.',
                  by='Syedna Mohammed Burhanuddin RA', note='Recounting Syedna Ismaʿil Badruddin RA'),
         ]),
    dict(slug='syedna-abdeali-saifuddin', name='Syedna Abdeʿali Saifuddin', hon='RA', title='Al-Dāʿī al-Ajal', rank='43rd al-Dāʿī al-Mutlaq',
         dates='1189/1775 – 1232/1817', img='rectangle-13985-2', theme='Founder of Darse Saifee',
         lead='A scholar of such stature that he was called Muʾayyad Asghar, after Syedna al-Muʾayyad al-Shirazi RA, '
              'author of eight hundred majālis.',
         sections=[
             dict(kind='facts', items=[
                 ('Darse Saifee, 1225/1810', 'An academy in Surat with classrooms, residences and a masjid, beside his '
                  'own home, built from his own wealth.'),
                 ('Stages and standards', 'He defined clear stages of learning and set standards for the curriculum, and '
                  'personally supervised students.'),
                 ('Arabic for South Asia', 'Instead of years of grammar first, beginners met complex Arabic texts '
                  'translated and explained orally, and learned vocabulary and grammar from them.'),
                 ('Lisān al-Daʿwa', 'Teaching through the community’s own language, Gujarati in structure and Arabic in '
                  'script, made Aljamea a centre of excellence in Arabic.'),
             ]),
             dict(kind='split', kicker='1817', title='Plan of the City of Surat',
                  body=['A British Revenue Survey plan of 1817 marks Darse Saifee as no. 4: a multi-storey building around '
                        'a courtyard “appropriated chiefly for the instruction of boys of the sect who coming from a '
                        'distance are lodged and fed here; at present 200 boys are said to be taught here.”'],
                  img='sas-map'),
         ]),
    dict(slug='syedna-taher-saifuddin', name='Syedna Taher Saifuddin', hon='RA', title='Al-Dāʿī al-Ajal', rank='51st al-Dāʿī al-Mutlaq',
         dates='1305/1888 – 1385/1965', img='rectangle-13985-3', theme='He brought the modern world into Aljamea',
         lead='He became dāʿī in 1333/1915 at the age of 28, and began with the educational and spiritual renewal of his followers.',
         sections=[
             dict(kind='text', body=['He introduced the arts and sciences to produce graduates able to meet the challenges '
                  'of the age, renamed Darse Saifee as Aljamea-tus-Saifiyah, and built its new Surat campus in 1381/1961.',
                  'Over a 53-year tenure he visited and advised educational institutions constantly; some three hundred and '
                  'fifty schools, colleges and institutes bear witness to his spirit. He was Chancellor of Aligarh Muslim '
                  'University until 1965, and received its honorary doctorate in theology in 1946.']),
             dict(kind='quote', text='It has also been my effort to improve the quality, the standard and the diversity '
                  'of the knowledge imparted in this institution so as to raise it to the status of a respected academy '
                  'which would attract scholars from all places and from which would radiate rays of sober wisdom and light.',
                  by='Syedna Taher Saifuddin RA'),
         ]),
    dict(slug='syedna-mohammed-burhanuddin', name='Syedna Mohammed Burhanuddin', hon='RA', title='Al-Dāʿī al-Ajal', rank='52nd al-Dāʿī al-Mutlaq',
         dates='1333/1915 – 1435/2014', img='rectangle-13985-4', theme='A culture of continuous growth',
         lead='Personally tutored by his father, he became dāʿī in 1385/1965 and was Aljamea’s benefactor for nearly fifty years.',
         sections=[
             dict(kind='facts', items=[
                 ('Four campuses', 'Redeveloped Surat, inaugurated Karachi, and announced Nairobi and Mumbai.'),
                 ('Mahad al-Zahra', 'Founded in 1396/1976, with a language laboratory that was a first in Quranic education.'),
                 ('A scholar', 'Memorised the Quran at twenty; wrote Arabic literary works and treatises on theology and '
                  'philosophy; contributed to the study of North African Fatimi history.'),
                 ('Honours', 'Chancellor of Aligarh Muslim University (1999–2002) and honorary Doctor of Literature, '
                  'University of Karachi (2004).'),
             ]),
             dict(kind='quote', text='May young men and women come here to Surat and, upon the completion of eleven years '
                  'of care and nurturing, graduate fully prepared for service.', by='Syedna Mohammed Burhanuddin RA', note='1988'),
         ]),
    dict(slug='syedna-mufaddal-saifuddin', name='Dr Syedna Mufaddal Saifuddin', hon='TUS', title='Al-Dāʿī al-Ajal', rank='53rd al-Dāʿī al-Mutlaq',
         dates='b. 20 August 1946, Surat', img='image-107', theme='Benefactor of Aljamea today',
         lead='Born in Surat, he was tutored by both his predecessors and graduated from Aljamea with the highest honours, '
              'al-ʿĀlim al-Bāriʿ, before further study in India and Egypt.',
         sections=[
             dict(kind='text', body=['Appointed one of Aljamea’s rectors in 1987, he encouraged students to memorise the '
                  'entire Quran and to live by its precepts of tolerance, kindness and service. As dāʿī since 2014 he has '
                  'built the Nairobi and Mumbai campuses and oversees hundreds of schools worldwide, where religious '
                  'education is combined with secular studies.']),
             dict(kind='facts', title='A legacy of knowledge', items=[
                 ('Aligarh Muslim University', 'Chancellor since April 2015, like his father and grandfather before him.'),
                 ('University of Karachi', 'Doctor of Letters honoris causa, September 2015.'),
                 ('Jamia Millia Islamia', 'Unanimously elected Chancellor, 14 March 2023.'),
                 ('Beyond the community', 'A thousand computers for AMU-affiliated schools, and the restoration of the '
                  'heritage buildings of Syedna Taher Saifuddin High School, Minto Circle.'),
             ]),
             dict(kind='gallery', imgs=['sms-chancellorship-aligarh', 'chancellorship-of-jamia-millia-islamia', 'aligarh-3']),
         ]),
    dict(slug='syedi-abdeali-imaduddin', name='Syedi Abdeʿali ʿImaduddin', hon='QR', title='Past leadership', rank='Head of Darse Saifee',
         dates='d. 1271/1854', img='ajss-09antiquarian03', theme='A teacher who could not wait for dawn',
         lead='A gifted disciple of the 43rd dāʿī, he was entrusted with Darse Saifee by Syedna Abdulqadir Najmuddin RA in 1258/1842.',
         sections=[dict(kind='text', body=[
             'He would not leave a concept until it was fully clear. Once, having unravelled a difficult text, he woke a '
             'student before daybreak to share it: life is uncertain, he said, and this was a trust he must fulfil.',
             'His Arabic and Urdu poetry and prose are studied in the curriculum and recited in community gatherings.'])]),
    dict(slug='dr-yusuf-najmuddin', name='Dr Shahzada Yusuf Najmuddin', hon='QR', title='Past leadership', rank='Rector, Amirul Jamea',
         dates='1340/1922 – 1407/1987', img='rectangle-13985-6', theme='Amirul Jamea',
         lead='Rector for nearly half a century under Syedna Taher Saifuddin RA and Syedna Mohammed Burhanuddin RA.',
         sections=[dict(kind='text', body=[
             'Aljamea’s curriculum, assessments and even its timetable reflect his foresight. He set out the 23 attributes '
             'of personality that still guide the counselling of every student.',
             'A master of words, spoken and written, he showed audiences how Fatimi philosophy answers contemporary '
             'questions. Aligarh Muslim University conferred on him an honorary doctorate in 1382/1962. He passed away '
             'in Cairo in 1407/1987.'])]),
]
LUMINARY = {l['slug']: l for l in LUMINARIES}

# --------------------------------------------------------------------------- timeline
TIMELINE = [
    ('365/970', 'Cairo', 'Al-Azhar is founded by al-Imam al-Muʿizz li Deen Allah AS.', 'al-azhar-university'),
    ('395/1005', 'Cairo', 'Al-Imam al-Hakim bi Amr Allah AS establishes the House of Knowledge.', None),
    ('526/1132', 'Yemen', 'The seat of the Dawat moves to Yemen and the office of al-Dāʿī al-Mutlaq is established.', 'yemen-hutaib'),
    ('946/1539', 'India', 'The seat of the Dawat, and its centres of learning, move to India.', None),
    ('1209/1795', 'Surat', 'Syedna Yusuf Najmuddin RA makes Surat the seat of his mission.', None),
    ('1225/1810', 'Surat', 'Syedna Abdeʿali Saifuddin RA founds Darse Saifee.', 'sas-map'),
    ('1380/1960', 'Surat', 'Pandit Jawaharlal Nehru, first Prime Minister of India, visits Aljamea on 22 June.', '3130'),
    ('1381/1961', 'Surat', 'Syedna Taher Saifuddin RA inaugurates the new Surat campus.', 'innaugaration-jamea-surat'),
    ('1385/1965', 'Karachi', 'Classes for years one to four begin in Karachi. Syedna Mohammed Burhanuddin RA succeeds as benefactor.', None),
    ('1389/1969', 'Karachi', 'Aljamea is institutionalised in Karachi and its campus foundation laid.', None),
    ('1390/1970', 'Mumbai', 'Institute of Arabic and Islamic Studies with Anjuman-e-Islam; Burhani College of Commerce and Arts.', None),
    ('1395/1975', 'Surat', 'Community members join the annual examination as mustafīdīn, a practice that continues today.', None),
    ('1396/1976', 'London', 'Syedna addresses the World of Islam Festival at the Royal Albert Hall and founds Mahad al-Zahra.', 'mahad-innaugaration'),
    ('1399/1979', 'Surat', 'Al-Multaqa al-ʿIlmi al-Fatimi, the Fatimi Educational Gathering.', 'fatemi-educational-gathering'),
    ('1401/1980', 'Cairo', 'Students help restore al-Jāmiʿ al-Anwar; reconstruction of Surat’s īwān, library and Mawāʾid begins.', 'al-jaame-al-anwar-renovation'),
    ('1404/1983', 'Karachi', 'The Karachi campus and Surat’s Masākin Mohammediya are inaugurated.', 'innaugaration-jamea-karachi'),
    ('1405/1985', 'Nairobi', 'The first al-Madrasa al-Saifiya al-Burhaniya school opens.', None),
    ('1407/1987', 'Cairo', 'Rector Syedi Yusuf Najmuddin QR passes away; new rectors are appointed, Syedna Mufaddal Saifuddin TUS among them.', 'current-rectors-of-jamea'),
    ('1408/1988', 'Surat', 'Examinations return to Surat; the new īwān and Rabwat Jibla open.', 'jamea-exams'),
    ('1419/1999', 'Surat', 'A dedicated Mahad al-Zahra building.', 'new-mahad-surat'),
    ('1420/2000', 'Yemen', 'Graduates join a long-term development project in rural Yemen.', None),
    ('1425/2004', 'Karachi', 'Honorary Doctor of Literature from the University of Karachi; a gift to its Department of Genetics.', 'smb-degree-of-dr-literature'),
    ('1425/2005', 'Online', 'Mahad al-Zahra launches e-Learning Quran memorisation.', None),
    ('1427/2007', 'Houston', 'Mahad al-Zahra satellite campus in Houston, Texas.', 'mahad-al-zahra-houston-satellite-campus'),
    ('1429/2008', 'Karachi', 'A second Mahad al-Zahra building.', 'mahad-al-zahra-building-karachi'),
    ('1432/2011', 'Nairobi', 'A third campus is announced on Syedna Burhanuddin RA’s 100th birthday; classes begin 20 days later.', 'al-jamea-exams-saifee-mahal'),
    ('1434/2013', 'Mumbai', 'A fourth campus is announced in Marol.', None),
    ('1435/2014', 'Mumbai', 'Syedna Mufaddal Saifuddin TUS becomes benefactor and conducts the annual examinations.', 'smb-crowd-2'),
    ('1438/2017', 'Nairobi', 'President Uhuru Kenyatta inaugurates the Nairobi campus.', 'aljamea-nairobi-innaugaration'),
    ('1444/2023', 'Mumbai', 'Prime Minister Narendra Modi inaugurates the Mumbai campus on 10 February.', 'photo-2023-02-10-19-23-00'),
    ('1444/2023', 'Nairobi', 'Syedna inaugurates the ETFE roof over the Nairobi sāhat.', 'moula-nairobi-saahat-roof-opening-02'),
]

# --------------------------------------------------------------------------- news
NEWS = [
    dict(slug='unep-delegation-visits-nairobi-campus', date=date(2024, 5, 9), campus='Nairobi', img='un-enviromental-programme-visit-7th-may-2024-jpg',
         title='UNEP Delegation Visits Nairobi Campus',
         dek='Dr Iyad Abu Moghli of the UN Environment Programme’s Faith for Earth Coalition toured the campus and addressed students.',
         body=['On 7 May 2024, Dr Iyad Abu Moghli, founder and Director of the Faith for Earth Coalition at the United Nations '
               'Environment Programme (UNEP), visited the Nairobi campus with five colleagues from UNEP headquarters.',
               'The tour highlighted the campus’ sustainability: rainwater harvesting, passive ventilation and natural light; one '
               'third of the campus as green space with more than 250 trees; and a subsistence farm fed by compost from the '
               'kitchen and dining hall. An exhibition presented the Dawoodi Bohra community’s global work on water, zero waste, '
               'renewable energy and green cover, which Dr Iyad noted aligns with the UN Sustainable Development Goals.',
               'In the auditorium he spoke to the entire student body about Al-Mizan, a covenant calling Muslims to act for the '
               'environment, and on how even a gnat has a purpose in creation. He looked forward to continuing the dialogue with '
               'Aljamea and the community.']),
    dict(slug='aljamea-mourns-the-loss-of-its-rector', date=date(2024, 4, 25), campus='Institution-wide', img='shahzadah-kalimuddin',
         title='Aljamea-tus-Saifiyah Mourns the Loss of its Rector',
         dek='Syedi Mazoon al-Dawat Shahzadah Aliasgar Kalimuddin (1351/1933 – 1445/2024): a life led in the pursuit and service of knowledge.',
         body=['Born on 9 Zilhijja 1351 H / 4 April 1933, he was the eighth son of Syedna Taher Saifuddin RA, who described him '
               'as having a capacious memory and gave him the epithet Kalimuddin in 1367/1948.',
               'He served Alvazaratus Saifiyah, the Burhani Educational Society, MSB Educational Institute and Burhani College, '
               'among many others. Syedna Mufaddal Saifuddin TUS appointed him a rector of Aljamea in 1439/2018, and elevated him '
               'to Mukasir and then, in 1440/2019, to Mazoon.',
               'His asbāq drew people from great distances until his last days. His annual Jawahir al-Kalam al-Ghaliya collected '
               'the discourses of Syedna Burhanuddin RA and Syedna Saifuddin TUS. Even at 95, in his final Ramadan, he missed '
               'neither a namaz with Syedna nor a fast. At the viva voce, his smile and nods of encouragement steadied many a '
               'student. His paternal warmth will be deeply missed.']),
    dict(slug='syedna-inaugurates-nairobi-courtyard-roof', date=date(2023, 7, 5), campus='Nairobi', img='moula-nairobi-saahat-roof-opening-02',
         title='Syedna Inaugurates Nairobi Campus Courtyard Covering',
         dek='A permanent ETFE roof over the sāhat, held on steel date palms, with projection mapping for the inaugural show.',
         body=['On Monday 3 July, His Holiness Syedna Mufaddal Saifuddin TUS inaugurated the new roof (saqaf) over the entire '
               'central courtyard (sāhat), which he had directed after Ashara Mubaraka 2021 was hosted on campus.',
               'Built in three months from December 2022, the roof is ETFE: light, strong and transparent to UV, so the courtyard’s '
               '36 date palms keep growing. Fritted and clear panels shade and light the space at once, keep the minarets in view, '
               'and hold warmth in winter. Its columns branch like date palms.',
               'Students welcomed His Holiness with an immersive light-and-sound presentation projected on Masjid al-Zahra, a '
               'tableau of student life, recitation and a band performance.']),
    dict(slug='an-educator-and-his-passion-for-bonsai', date=date(2021, 4, 23), campus='Nairobi', img='gardening',
         title='An Educator and his Passion for Bonsai',
         dek='Nairobi faculty member Ahmedali Hebatullah on shaping trees, and young minds, with patience.',
         body=['For Ahmedali Hebatullah, an educator at Aljamea Nairobi, trees are living works of art. He has miniaturised '
               'jacaranda, jade, acacia, olive and fig, some of them fifteen years old.',
               '“Both require patience and determination,” he says of bonsai and teaching. His hobby fits the campus’ environmental '
               'campaigns, and he hopes it will inspire more people to garden and plant trees.']),
    dict(slug='online-learning', date=date(2020, 8, 5), campus='Institution-wide', img='online-learning-2',
         title='Aljamea Students and Faculty Embrace Online Learning',
         dek='Across continents and time zones, the process of enlightening minds remains undiminished.',
         body=['During the pandemic all four campuses moved online. The imams AS and their duʿāt RA taught in cellars and on '
               'rooftops when they had to; Aljamea has adapted before, relocating to Burhanpur after the 2005 Surat floods.',
               'Learning happens in the physical world, but it is ultimately a spiritual endeavour.']),
    dict(slug='karachi-auditorium-wins-at-pakistan-flower-show', date=date(2020, 5, 1), campus='Karachi', img='audi-1',
         title='Karachi Campus Auditorium Wins Second Prize at Pakistan Flower Show',
         dek='The auditorium garden placed second in the University Gardens category of the 69th Pakistan Annual Flower Show.',
         body=['President Arif Alvi presented the award on 20 February 2020 at the close of the Horticultural Society of '
               'Pakistan’s competition.',
               'In Fatimi thought gardens symbolise intellectual pursuits that delight and nourish the soul. Gardens inspired by '
               'Quranic verses and Fatimi history feature on every campus.']),
    dict(slug='persian-certification', date=date(2020, 2, 12), campus='Nairobi', img='whatsapp-image-2020-02-12-at-9-01-04-am-2',
         title='Students Receive Certification for Beginner Level Persian',
         dek='Nineteen Nairobi students certified by the Iranian Cultural Centre with Ferdowsi University of Mashhad.',
         body=['The examinations were held on 9 and 10 January 2020. At the felicitation on 7 February, faculty and students '
               'presented original Persian poetry and prose and discussed the role of language in preserving heritage.']),
    dict(slug='archery-bronze', date=date(2020, 1, 27), campus='Surat', img='archery-1',
         title='Faculty Member Takes Bronze at National Archery Competition',
         dek='Mustafa F Shakir won three bronze medals for Gujarat in the veterans’ category.',
         body=['At the 9th National Field Indoor Archery Championship in Agra, 24–26 January 2020, he won bronze for single '
               'spot, five spot and overall performance.']),
    dict(slug='strathmore-dean-visits', date=date(2020, 1, 20), campus='Nairobi', img='img-1724',
         title='Dean of Strathmore Business School Visits Aljamea Nairobi',
         dek='Dr George Njenga lectured students on the Aljamea–Strathmore business studies programme.',
         body=['More than 30 students and faculty study business at Strathmore alongside their Aljamea education. The Dean '
               'praised the community’s business ethics and Aljamea’s role in instilling them.']),
]
NEWS_BY_SLUG = {n['slug']: n for n in NEWS}

# --------------------------------------------------------------------------- generic pages
PAGES = {
    'about': dict(title='About Aljamea', ar='عن الجامعة', kicker='Our story', img='ajsm-06sahatshot7-5032',
        lead='Aljamea-tus-Saifiyah is the principal educational institute of the Dawoodi Bohra community. For over two '
             'centuries it has educated young men and women in the principles of Fatimi philosophy, alongside the best of '
             'contemporary disciplines, under the guidance of its sole benefactor, His Holiness Dr Syedna Mufaddal Saifuddin TUS.',
        sections=[
            dict(kind='text', kicker='A quest for excellence', title='Ancient yet modern. Focused yet holistic.',
                 body=['The eleven-year programme spans higher secondary, undergraduate and graduate education. Students '
                       'specialise, but are also expected to study widely across the empirical sciences, the social sciences, '
                       'the humanities and modern languages.',
                       'Education here goes beyond academics. It aims at excellence in every part of a person, moral and '
                       'intellectual, and at constant application of what is learnt.']),
            dict(kind='stages'),
            dict(kind='split', kicker='Architecture', title='Every campus centres on the masjid',
                 body=['Every building on every campus faces the Holy Kaaba, oriented to the masjid. In Karachi, Nairobi and '
                       'Mumbai the masjid stands ahead of the other buildings, as an imam stands ahead of those he leads.',
                       'Fatimi monuments are not reproduced as reminders of a former glory. They are a living source of '
                       'inspiration toward the ideals of the Fatimi tradition: āthār and maʾāthir.'],
                 img='ajsn-08minaret03-dl-3498'),
            dict(kind='split', kicker='In harmony with nature', title='Built lightly on Allah’s creation', flip=True,
                 body=['Sunlight and natural ventilation reduce dependence on electricity. Surat has used solar water heating '
                       'since the early 1980s. In Karachi, palms along the sports field prevent waterlogging for the '
                       'neighbourhood too.',
                       'Recycling, composting, motion-sensor lighting and paper reduction are campus policy. Nairobi and Mumbai '
                       'were built to LEED requirements, with photovoltaics, passive ventilation and geothermal cooling.'],
                 img='jamea-nairobi-harmony'),
        ]),
    'architecture': dict(title='Fatimi Architecture', ar='العمارة الفاطمية', kicker='Belief, in stone', img='ajsn-02eiwan02-extrukn-1122',
        lead='The art and architecture of the Fatimi imams AS is not only studied at Aljamea, it is lived in. Tradition and '
             'modernity meet in the design language of every campus.',
        sections=[
            dict(kind='split', kicker='Al-Jāmiʿ al-Aqmar', title='The Rukn Mukhallaq',
                 body=['The chamfered corner of al-Aqmar’s façade, reproduced at Aljamea, carries the verse “Indeed, Allah is '
                       'with those who are pious and those who do good.” It reminds students that knowledge must lead to both '
                       'piety and goodwill.'],
                 img='ajsn-02eiwan02-extrukn-1122'),
            dict(kind='split', kicker='Beacons', title='The minaret', flip=True,
                 body=['Between masjid and minaret lie classrooms, the library and other facilities, merging into one complex '
                       'dedicated to knowledge and character. The minarets rise above them all, beacons pointing to the '
                       'heritage of the Fatimi imams.'],
                 img='ajsn-08minaret03-dl-3498'),
            dict(kind='facts', title='Green by design', items=[
                ('LEED compliance', 'Rainwater harvesting, composting and photovoltaic panels.'),
                ('Daylight & air', 'Buildings designed for natural light and ventilation wherever possible.'),
                ('Renewable energy', 'Solar water heating in Surat since the 1980s; solar power on the newer campuses.'),
                ('Quranic gardens', 'Pakistan’s first Quranic garden in Karachi; in Nairobi, trees named in the Quran beside '
                 'indigenous species.'),
            ]),
            dict(kind='gallery', title='Details', imgs=['ajsm-detail-1893fw', 'ajsm-detail-4025fw', 'ajsm-detail-4117fw',
                                                        'ajsn-04mawaid04-detail-0720', 'ajsn-03mahad01-baab-0983', 'ajsn-03mahad11-roof-4303']),
        ]),
    'philosophy': dict(title='The Fatimi Philosophy of Education', ar='فلسفة التعليم الفاطمية', kicker='In the light of revelation',
        img='ajsn-15maktabat02-kehf-0165',
        lead='Allah is the source of all knowledge. Any knowledge that deepens one’s understanding of the Almighty, His '
             'revelation and His creation, and enables His servitude, is Fatimi in nature, whatever field it belongs to.',
        sections=[
            dict(kind='quote', text='It befits our brethren to not hate a single field of knowledge, shun a particular book, '
                 'or bear prejudice towards a certain faith. Indeed, our philosophy and our faith engulf all faiths and '
                 'encompass all knowledge.', by='Moulana al-Imam Ahmad al-Taqi AS'),
            dict(kind='split', kicker='The temporal alongside the spiritual', title='Understanding the world is worship',
                 body=['In the 11th century CE, Syedna Ahmed Hamiduddin al-Kirmani RA held that understanding the physical '
                       'and natural world is an essential part of worship. Fatimi principles and modern disciplines are not in '
                       'conflict; the philosophy requires the temporal and the spiritual to be integrated.'],
                 img='ajsn-16labbio01-3869'),
            dict(kind='split', kicker='Takāmul Shakhsī', title='A well-rounded personality', flip=True,
                 body=['Education without spirituality or moral teaching is incomplete. Fatimi education seeks academic '
                       'excellence, meaningful practice, refined character and moral virtue together.'],
                 img='about-1'),
        ]),
    'examinations': dict(title='Al-Imtihān al-Sanawī', ar='الامتحان السنوي', kicker='The annual examinations', img='rectangle-13985-7',
        lead='More than a test of learning: Aljamea’s examinations take place in the presence of His Holiness and thousands '
             'of community members, a source of pride and motivation for every student.',
        sections=[
            dict(kind='split', kicker='Zikra', title='An address by His Holiness',
                 body=['Continuing the tradition of his forefathers, His Holiness Dr Syedna Mufaddal Saifuddin TUS conducts the '
                       'examinations personally. They open with his khutba, which sets their theme and commemorates the '
                       'endeavours of Syedna Taher Saifuddin RA and Syedna Mohammed Burhanuddin RA for Aljamea.'],
                 img='smb-crowd-2'),
            dict(kind='split', kicker='Viva voce', title='Oral examinations', flip=True,
                 body=['His Holiness presides over the orals of years seven to eleven. Students are questioned on epistles of '
                       'the 51st, 52nd and 53rd duʿāt and asked to connect them with contemporary issues, modern disciplines '
                       'and the real world. Content, oratory and poise all count.',
                       'Often His Holiness poses questions himself. The audience learns from every exchange.'],
                 img='al-jamea-exams-saifee-mahal'),
            dict(kind='text', kicker='On paper', title='Written examinations',
                 body=['An introductory booklet, drawn from the Zikra, sets the theme and invites reflection. His Holiness '
                       'approves every question paper. There are nine written papers, plus one in their specialisation for '
                       'students at stage four. Questions emphasise application and critical thinking.']),
            dict(kind='table', title='Grading', lead='One credit equals forty hours of study. Students earn at least forty '
                 'credits a year in the early years, rising thereafter. For current criteria, contact the Head Office in Mumbai.',
                 head=['Percentage', 'Grade'], rows=[[a, b] for a, b in GRADES]),
        ]),
}

# --------------------------------------------------------------------------- admissions
PROGRAMMES = [
    dict(name='Aljamea-tus-Saifiyah', ar='الجامعة السيفية', length='11 years', who='Young men and women of the Dawoodi Bohra community',
         body='The full residential programme across four stages, from higher secondary to master’s level, on any of the four campuses.'),
    dict(name='Darse Burhani', ar='درس برهاني', length='Focused programmes', who='Those seeking focused religious study',
         body='Pathways designed for spiritual growth, personal development and a deeper understanding of the faith, with the '
              'flexibility to pursue other academic or personal goals.'),
    dict(name='Mahad al-Zahra', ar='معهد الزهراء', length='4-year hifz', who='Children and adults, worldwide',
         body='Residential and day programmes to memorise the Quran in four years alongside regular schooling, plus e-Learning '
              'and Ramadan programmes.'),
]

# Steps are worded generically; the admissions office should confirm the exact process before launch.
ADMISSION_STEPS = [
    ('Register', 'Sign in to the official admissions portal and register the applicant.'),
    ('Choose', 'Select the programme and campus that suit the applicant’s aspirations.'),
    ('Apply', 'Complete the application and submit the documents requested.'),
    ('Hear back', 'The admissions office contacts applicants about the next steps.'),
]

# --------------------------------------------------------------------------- testimonials
VOICES = [
    ('We appreciate the contribution of the Dawoodi Bohra community to Kenya’s growth, especially in the housing, healthcare '
     'and education sectors. Through Aljamea-tus-Saifiyah, a world-class Arabic academy, they continue to make a lasting '
     'impact on learning, values, and social…', 'Dr William Samoei Ruto', 'President of Kenya'),
    ('Today, as the country starts its journey towards the ‘Golden Era’ of its independence, the importance of this '
     'contribution of the Bohra community in the field of education is all the more significant.', 'Shri Narendra Modi',
     'Prime Minister of India, inaugurating the Mumbai campus'),
    ('The quality indeed that we have seen today of the physical facilities in this complex attest to the readiness and '
     'commitment, to the vision and mission of education in Kenya.', 'Mr Uhuru Kenyatta', 'President of Kenya, inaugurating the Nairobi campus'),
]

# --------------------------------------------------------------------------- redirects from the WordPress URLs
LEGACY = {
    'about-us': ('site.page', dict(slug='about')),
    'the-realization': ('site.history', {}),
    'brief-history': ('site.history', {}),
    'fatemi-architecture': ('site.page', dict(slug='architecture')),
    'fatemi-philosophy': ('site.page', dict(slug='philosophy')),
    'al-imtehan-al-sanawi': ('site.page', dict(slug='examinations')),
    'the-three-stages-at-a-glance': ('site.academics', {}),
    'mumbai-campus': ('site.campus', dict(slug='mumbai')),
    'nairobi-campus': ('site.campus', dict(slug='nairobi')),
    'karachi-campus': ('site.campus', dict(slug='karachi')),
    'the-residence': ('site.facility', dict(slug='residences')),
    'sports-complex': ('site.facility', dict(slug='sports')),
    'dining-hall': ('site.facility', dict(slug='dining')),
    'library': ('site.facility', dict(slug='library')),
    'computer-lab': ('site.facility', dict(slug='computer-lab')),
    'auditorium': ('site.facility', dict(slug='auditorium')),
    'faculty-of-philosophy-hikma': ('site.faculty', dict(slug='philosophy')),
    'faculty-of-literature': ('site.faculty', dict(slug='literature')),
    'faculty-of-languages': ('site.faculty', dict(slug='languages')),
    'faculty-of-jurisprudence': ('site.faculty', dict(slug='jurisprudence')),
    'faculty-of-history': ('site.faculty', dict(slug='history')),
    'faculty-of-empirical-and-social-sciences': ('site.faculty', dict(slug='sciences')),
    'mahad-al-zahra': ('site.department', dict(slug='mahad-al-zahra')),
    'the-department-of-dissertations': ('site.department', dict(slug='dissertations')),
    'centre-for-research': ('site.department', dict(slug='research')),
    'centre-for-cultural-activities': ('site.department', dict(slug='cultural-activities')),
    'darse-burhani': ('site.admissions', {}),
    'news': ('site.news', {}),
}


def img_alt(key):
    """Readable alt text from a media key, used when a section does not supply its own."""
    return key.replace('-', ' ')


def search_index(url_for):
    items = [dict(t='Home', u=url_for('site.home'), g='Page')]
    for k, p in PAGES.items():
        items.append(dict(t=p['title'], u=url_for('site.page', slug=k), g='Page', a=p['ar']))
    for t, e in [('History & timeline', 'site.history'), ('Academics & the eleven years', 'site.academics'),
                 ('Campuses', 'site.campuses'), ('Campus life', 'site.life'), ('Luminaries', 'site.luminaries'),
                 ('News & events', 'site.news'), ('Admissions', 'site.admissions'), ('Contact', 'site.contact')]:
        items.append(dict(t=t, u=url_for(e), g='Page'))
    for c in CAMPUSES:
        items.append(dict(t=f"{c['name']} campus", u=url_for('site.campus', slug=c['slug']), g='Campus', a=c['ar']))
    for f in FACULTIES:
        items.append(dict(t=f"Faculty of {f['name']} ({f['native']})", u=url_for('site.faculty', slug=f['slug']), g='Faculty', a=f['ar']))
    for d in DEPARTMENTS:
        items.append(dict(t=d['name'], u=url_for('site.department', slug=d['slug']), g='Department', a=d['ar']))
    for f in FACILITIES:
        items.append(dict(t=f"{f['name']} · {f['native']}", u=url_for('site.facility', slug=f['slug']), g='Campus life', a=f['ar']))
    for l in LUMINARIES:
        items.append(dict(t=f"{l['name']} {l['hon']}", u=url_for('site.luminary', slug=l['slug']), g='Luminary'))
    for n in NEWS:
        items.append(dict(t=n['title'], u=url_for('site.article', slug=n['slug']), g='News'))
    return items
