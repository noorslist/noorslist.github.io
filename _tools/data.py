# Mockup data: the Oct 29, 2026 edition, with org + audience tags added.
# Each event: date (ISO), time, title, place, orgs[], aud[], slug (existing page or None), note
GH = "https://noorslist.github.io/"

EVENTS = [
  # ---- weekend Fri 10/30 - Sun 11/1
  ("2026-10-30","Jumma","Vote for the Ummah (Early Voting)","",[],[],"2026-10-30-vote-for-the-ummah"),
  ("2026-10-30","3p","Meet U.S. Senate Candidate Angie Nixon, then Vote Together","ICO",["ICO"],[],"2026-10-30-meet-angie-nixon"),
  ("2026-10-30","","Young Professionals Lighthouse Conference","Hyatt Regency",["MAS"],[],None),
  ("2026-10-30","5:30p - 7p","Muslim Seniors Meetup","Dough Show",["ourMSC"],["Seniors"],"2026-10-30-ourmsc-seniors-meetup"),
  ("2026-10-31","8a - 10a","Pickleball Men's Doubles Tournament (& Nov 1)","AMCC",["AMCC"],["Brothers"],"2026-10-31-amcc-pickleball-tournament"),
  ("2026-10-31","8:30a - 10p","2nd North American Qur'an Competition (& Nov 1)","ICO",["ICO"],[],"2026-10-31-north-american-quran-competition"),
  ("2026-10-31","11a","Neighborly Needs Community Feeding Event","Masjid Al-Haqq",["Masjid Al-Haqq"],[],None),
  ("2026-10-31","12p - 2p","Community Serve Day","The Sharing Center",["Amnesty Youth"],["Youth"],None),
  ("2026-10-31","12p","Pink Together: Picnic for Health, Hope & Sisterhood","Bill Frederick Park",["ICNA Sisters"],["Sisters"],"2026-10-31-icna-sisters-pink-together"),
  ("2026-10-31","2p - 6p","In Celebration and Praises of the Prophet ﷺ","Oviedo Masjid",["Rabata"],["Sisters"],"2026-10-31-rabata-celebration-of-the-prophet"),
  ("2026-10-31","4p - 8p","NMCA Fall Picnic","Lake Nona Masjid",["NMCA"],[],"2026-10-31-lake-nona-fall-picnic"),
  ("2026-10-31","6p - 9p","Youth Game Night","Windermere",["Siraat"],["Youth"],"2026-10-31-siraat-youth-game-night"),
  ("2026-10-31","6:45p","Family Night: Dhikr and Sweet (Kids)","HMCC",["HMCC"],["Youth"],"2026-10-31-hmcc-family-night"),
  ("2026-11-01","2a","Clocks Fall Back 1 Hour","",[],[],"2026-11-01-clocks-fall-back"),
  ("2026-11-01","12p - 6p","Niche Market: Egyptian Heritage & Global Artisan Finds","Avalon Park Clubhouse",[],[],"2026-11-01-niche-market"),
  ("2026-11-01","3p - 5p","Dawah: The Art of Inviting to Good (Part 2)","Oviedo Masjid",["OMA"],[],"2026-11-01-oma-dawah-workshop-part-2"),
  # ---- next week Mon 11/2 - Sun 11/8
  ("2026-11-03","7a - 7p","General Election — Polls Open","",[],[],None),
  ("2026-11-03","2p - 5p","Islamic Book Fair (Nov 3-6)","ICO",["ICO"],[],"2026-11-03-ico-islamic-book-fair"),
  ("2026-11-06","2p - 4p","Walgreens Free Flu and Vaccine Clinic","ICO",["ICO"],[],None),
  ("2026-11-06","Maghrib - late","Brothers Game Night (6th grade - YP)","MAGO",["ICO Youth"],["Brothers","Youth"],"2026-11-06-ico-youth-brothers-game-night"),
  ("2026-11-07","9a - 12p","Faith, Gratitude & Everyday Joy — Potluck Breakfast","Masjid Tazkiah",["Masjid Tazkiah"],["Seniors"],"2026-11-07-tazkiah-potluck-breakfast"),
  ("2026-11-07","12p - 1:30p","Mental Health Workshop & Potluck (Girls 14+)","Oviedo Masjid",["YMS","Yusra"],["Sisters","Youth"],"2026-11-07-yms-mental-health-workshop"),
  ("2026-11-07","1:30p - 5p","Muslim Matrimonial Event (18+)","Masjid Al-Rahman",["ISCF"],[],"2026-11-07-iscf-muslim-matrimonial"),
  ("2026-11-07","Asr - Isha","Sisters Game Night (6th grade - YP)","MAGO",["ICO Youth"],["Sisters","Youth"],"2026-11-07-ico-youth-sisters-game-night"),
  ("2026-11-08","11a - 3p","Seniors Picnic (60+)","ICO",["ICO"],["Seniors"],None),
  ("2026-11-08","2:30p - 6:30p","Community Matrimonial Event","AMCC",["AMCC"],[],None),
  # ---- later
  ("2026-11-13","6:30p","Qur'an Night: Unity Through Recitation","ICO",["IDEA"],[],"2026-11-13-ico-idea-quran-night"),
  ("2026-11-14","5p - 11p","Masjid Al-Rahman Fall Festival","Masjid Al-Rahman",["Masjid Al-Rahman"],[],"2026-11-14-masjid-al-rahman-fall-festival"),
  ("2026-11-14","7:30p","Family Night: Islamic Perspective on Holidays","ICO",["ICO"],[],"2026-11-14-ico-family-night-holidays"),
  ("2026-11-15","11a - 12:30p","Keep Calm and Dabka On (Ladies 10+)","Winter Park",["Bismillah Institute"],["Sisters"],"2026-11-15-dabka-on-caregivers"),
  ("2026-11-15","11a - 5p","Masjid Al-Salam Annual Picnic","Masjid Al-Salam",["Masjid Al-Salam"],[],None),
  ("2026-11-19","6:30p","Fall United Plates Project","Oviedo Amphitheatre",["CG-USA"],[],"2026-11-19-cg-usa-united-plates"),
  ("2026-11-21","2p","Florida Islamic Center Site Walk-Through","FL Islamic Center",[],[],None),
  ("2026-12-05","9:30a - 5p","Central Florida Muslim Business Expo","Husseini Islamic Center",[],[],None),
  ("2026-12-06","12p","1st Muslim Medical School in the US (NCOM)","Coco Key Hotel",[],[],"2026-12-06-ncom-medical-school-celebration"),
  ("2026-12-18","6:30p - 9:30p","Building Bridges & Breaking Bread","Masjid Al-Rahman",["American Islam"],[],None),
  ("2026-12-18","","Dawah Retreat 2026 (Dec 18-20)","MECCA Center",["American Islam"],[],"2026-12-18-american-islam-dawah-retreat"),
  ("2027-01-23","12p - 1p","Young Professional Meetup","Maitland Civic Center",[],[],None),
  ("2027-01-23","12p - 6p","Muslim Business Networking Event","Maitland Civic Center",[],[],None),
]

PROGRAMS = [
  ("Thursdays, Maghrib - Isha","Thursday Halaqa: Allah's Names Series","Oviedo Masjid",["MAS"],[],"2026-10-22-mas-thursday-halaqa"),
  ("Saturdays @ Asr, from Oct 24","Hadith & Hidaya (ages 11-22)","ICO",["ICO Youth"],["Sisters","Youth"],None),
  ("Thursdays 7p, from Oct 29","Arabic 101 & Salah Classes","Masjid Al-Haqq",["Masjid Al-Haqq"],[],None),
  ("Saturdays 5:45p","Hadith & Hoops (ages 14-18)","ICO",["ICO Youth"],["Brothers","Youth"],"2026-10-31-ico-hadith-and-hoops"),
  ("Saturdays 10a - 12p","Free Medical Health Clinic","MAGO",["UMSS"],[],"2026-10-31-umss-free-medical-clinic"),
]
