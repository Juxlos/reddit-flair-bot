# imports
import praw
from time import gmtime, strftime

# main function


def main():
    teams = {
        'team-gb': 'Team GB 2012',
        'misc-1966-england': 'World Cup - England \'66',
        'misc-1970-mexico': 'World Cup - Mexico \'70',
        'misc-1974-wgermany': 'World Cup - West Germany \'74',
        'misc-1978-holland': 'World Cup - Holland \'78',
        'misc-1982-spain': 'World Cup - Spain \'82',
        'misc-1986-mexico': 'World Cup - Mexico \'86',
        'misc-1990-italy': 'World Cup - Italy \'90',
        'misc-1994-usa': 'World Cup - USA \'94',
        'misc-1998-france': 'World Cup - France \'98',
        'misc-2002-japan': 'World Cup - Japan 2002',
        'misc-2006-germany': 'World Cup - Germany 2006',
        'misc-2010-south-africa': 'World Cup - S.Africa 2010',
        'misc-2014-rio': 'World Cup - Rio 2014',
        'misc-2014-rio2': 'Rio 2014 Logo',
        'misc-bundes': 'Bundesliga',
        'misc-chmpl': 'Champions League',
        'misc-faprem': 'FA Premier League',
        'misc-seriea': 'Serie A',
        'misc-wil': 'FC Wil',
        'misc-pahang': 'Pahang FA',
        'misc-fcman': 'FC United of Manchester',
        'misc-afctel': 'AFC Telford',
        'prem-arsenal': 'Arsenal',
        'prem-aston-villa': 'Aston Villa',
        'prem-chelsea': 'Chelsea',
        'prem-everton': 'Everton',
        'prem-fulham': 'Fulham',
        'prem-liverpool': 'Liverpool',
        'prem-manchester-city': 'Manchester City',
        'prem-manchester-united': 'Manchester Utd',
        'prem-newcastle-united': 'Newcastle Utd',
        'prem-norwich-city': 'Norwich City',
        'prem-queens-park-rangers': 'Queens Park Rangers',
        'prem2-reading': 'Reading',
        'prem2-southampton': 'Southampton',
        'prem-stoke-city': 'Stoke City',
        'prem-sunderland': 'Sunderland',
        'prem-swansea': 'Swansea',
        'prem-tottenham-hotspur': 'Tottenham Hotspur',
        'prem-west-bromwich-albion': 'W.B.A',
        'prem2-west-ham': 'West Ham',
        'prem-wigan-athletic': 'Wigan Athletic',
        'lgone-bourne': 'Bournemouth',
        'lgone-brent': 'Brentford',
        'lgone-bury': 'Bury',
        'lgone-carl': 'Carlisle Utd',
        'lgone-colch': 'Colchester Utd',
        'lgone-covent': 'Coventry City',
        'lgone-craw': 'Crawley Town',
        'lgone-crewe': 'Crewe Alexandra',
        'lgone-donc': 'Doncaster Rovers',
        'lgone-hart': 'Hartlepool Utd',
        'lgone-leyt': 'Leyton Orient',
        'lgone-mkdons': 'MK Dons',
        'lgone-notts': 'Notts County',
        'lgone-oldh': 'Oldham Athletic',
        'lgone-pne': 'Preston North End',
        'lgone-ports': 'Portsmouth',
        'lgone-scun': 'Scunthorpe Utd',
        'lgone-sheff': 'Sheffield Utd',
        'lgone-shrew': 'Shrewsbury Town',
        'lgone-steven': 'Stevenage',
        'lgone-swin': 'Swindown Town',
        'lgone-tran': 'Tranmere Rovers',
        'lgone-swin': 'Swindon Town',
        'lgone-yeovil': 'Yeovil Town',
        'lgtwo-accr': 'Accrington Stanley',
        'lgtwo-ald': 'Aldershot',
        'lgtwo-barnet': 'Barnet',
        'lgtwo-brad': 'Bradford City',
        'lgtwo-brrov': 'Bristol Rovers',
        'lgtwo-burt': 'Burton Albion',
        'lgtwo-chelt': 'Cheltenham Town',
        'lgtwo-chest': 'Chesterfield',
        'lgtwo-dagred': 'Dagenham and Redbridge',
        'lgtwo-exe': 'Exeter City',
        'lgtwo-fleet': 'Fleetwood Town',
        'lgtwo-gill': 'Gillingham',
        'lgtwo-more': 'Morecambe',
        'lgtwo-north': 'Northampton Town',
        'lgtwo-oxf': 'Oxford United',
        'lgtwo-ply': 'Plymouth Argyle',
        'lgtwo-port': 'Port Vale',
        'lgtwo-roch': 'Rochdale',
        'lgtwo-roth': 'Rotherham Utd',
        'lgtwo-south': 'Southend Utd',
        'lgtwo-torq': 'Torquay',
        'lgtwo-wimb': 'Wimbledon',
        'lgtwo-wyc': 'Wycombe Wanderers',
        'lgtwo-york': 'York City',
        'eurnat-albania': 'Albania',
        'eurnat-andorra': 'Andorra',
        'eurnat-armenia': 'Armenia',
        'eurnat-austria': 'Austria',
        'eurnat-belgium': 'Belgium',
        'eurnat-bosnia-herzegovina': 'Bosnia-Herzegovina',
        'eurnat-bulgaria': 'Bulgaria',
        'eurnat-croatia': 'Croatia',
        'eurnat-cyprus': 'Cyprus',
        'eurnat-czech-republic': 'Czech Republic',
        'eurnat-denmark': 'Denmark',
        'eurnat-england': 'England',
        'eurnat-estonia': 'Estonia',
        'eurnat-faroe-islands': 'Faroe Islands',
        'eurnat-finland': 'Finland',
        'eurnat-france': 'France',
        'eurnat-georgia': 'Georgia',
        'eurnat-germany': 'Germany',
        'eurnat-greece': 'Greece',
        'eurnat-hungary': 'Hungary',
        'eurnat-iceland': 'Iceland',
        'eurnat-ireland': 'Ireland',
        'eurnat-italy': 'Italy',
        'eurnat-latvia': 'Latvia',
        'eurnat-liechtenstein': 'Liechtenstein',
        'eurnat-lithuania': 'Lithuania',
        'eurnat-luxembourg': 'Luxembourg',
        'eurnat-macedonia': 'Macedonia',
        'eurnat-malta': 'Malta',
        'eurnat-moldova': 'Moldova',
        'eurnat-monaco': 'Monaco',
        'eurnat-netherlands': 'Holland',
        'eurnat-norway': 'Norway',
        'eurnat-poland': 'Poland',
        'eurnat-portugal': 'Portugal',
        'eurnat-romania': 'Romania',
        'eurnat-russia': 'Russia',
        'eurnat-san-marino': 'San Marino',
        'eurnat-scotland': 'Scotland',
        'eurnat-serbia-montenegro': 'Serbia',
        'eurnat-slovakia': 'Slovakia',
        'eurnat-slovenia': 'Slovenia',
        'eurnat-switzerland': 'Switzerland',
        'eurnat-turkey': 'Turkey',
        'eurnat-ukraine': 'Ukraine',
        'eurnat-united-kingdom': 'United Kingdom',
        'eurnat-vatican-city': 'Vatican City',
        'eurnat-wales': 'Wales',
        'esp-athletic-bilbao': 'Athletic Bilbao',
        'esp-athletico-madrid': 'Athletico Madrid',
        'esp-barcelona': 'Barcelona',
        'esp-espanyol': 'Espanyol',
        'esp-getafe': 'Getafe',
        'esp-granada': 'Granada',
        'esp-levante-utd': 'Levante Utd',
        'esp-malaga': 'Malaga',
        'esp-mallorca': 'Mallorca',
        'esp-osasuna': 'Osasuna',
        'esp-racing-santander': 'Racing Santander',
        'esp-rayo-vallecano': 'Vallecano',
        'esp-real-betis': 'Real Betis',
        'esp-real-madrid': 'Real Madrid',
        'esp-real-sociedad': 'Real Sociedad',
        'esp-sevilla': 'Sevilla',
        'esp-sporting-gijon': 'Sporting Gijon',
        'esp-valencia': 'Valencia',
        'esp-villareal': 'Villareal',
        'esp-zaragoza': 'Zaragoza',
        'esp-oviedo': 'Real Oviedo',
        'usa-chicago-fire': 'Chicago Fire',
        'usa-chivas-usa': 'Chivas USA',
        'usa-colorado-rapids': 'Colorado Rapids',
        'usa-columbus-crew': 'Columbus Crew',
        'usa-dc-united': 'DC United',
        'usa-fc-dallas': 'FC Dallas',
        'usa-houston': 'Houston',
        'usa-sporting-kansas': 'Sporting Kansas City',
        'usa-los-angeles-galaxy': 'Los Angeles Galaxy',
        'usa-montreal-impact': 'Montreal Impact',
        'usa-new-england-revolution': 'New England Revolution',
        'usa-new-york-red-bulls': 'New York Red Bulls',
        'usa-philadelphia-union': 'Philadelphia Union',
        'usa-portland-timbers': 'Portland Timbers',
        'usa-real-salt-lake': 'Real Salt Lake',
        'usa-san-jose-earthquakes': 'San Jose Earthquakes',
        'usa-seattle-sounders': 'Seattle Sounders',
        'usa-toronto-fc': 'Toronto FC',
        'usa-vancouver-whitecaps': 'Vancouver Whitecaps',
        'fed-albania': 'Albania',
        'fed-andorra': 'Andorra',
        'fed-armenia': 'Armenia',
        'fed-austria': 'Austria',
        'fed-belarus': 'Belarus',
        'fed-belgium': 'Belgium',
        'fed-bosnia-herzegovina': 'Bosnia-Herzegovina',
        'fed-bulgaria': 'Bulgaria',
        'fed-cyprus': 'Cyprus',
        'fed-czech-republic': 'Czech Republic',
        'fed-denmark': 'Denmark',
        'fed-england': 'England',
        'fed-faroe-islands': 'Faroe Islands',
        'fed-finland': 'Finland',
        'fed-france': 'France',
        'fed-fyr-macedonia': 'Macedonia',
        'fed-georgia': 'Georgia',
        'fed-germany': 'Germany',
        'fed-greece': 'Greece',
        'fed-greenland': 'Greenland',
        'fed-hungary': 'Hungary',
        'fed-iceland': 'Iceland',
        'fed-israel': 'Israel',
        'fed-italy': 'Italy',
        'fed-kazakhstan': 'Kazakhstan',
        'fed-latvia': 'Latvia',
        'fed-liechtenstein': 'Liechtenstein',
        'fed-lithuania': 'Lithuania',
        'fed-luxembourg': 'Luxembourg',
        'fed-malta': 'Malta',
        'fed-moldova': 'Moldova',
        'fed-montenegro': 'Montenegro',
        'fed-netherlands': 'Netherlands',
        'fed-northern-ireland': 'Northern Ireland',
        'fed-norway': 'Norway',
        'fed-portugal': 'Portugal',
        'fed-roi': 'Republic of Ireland',
        'fed-romania': 'Romania',
        'fed-russia': 'Russia',
        'fed-san-marino': 'San Marino',
        'fed-scotland': 'Scotland',
        'fed-serbia': 'Serbia',
        'fed-slovakia': 'Slovakia',
        'fed-slovenia': 'Slovenia',
        'fed-spain': 'Spain',
        'fed-sweden': 'Sweden',
        'fed-switzerland': 'Switzerland',
        'fed-turkey': 'Turkey',
        'fed-wales': 'Wales',
        'ita-atalanta': 'Atalanta',
        'ita-bologna': 'Bologna',
        'ita-cagliari': 'Cagliari',
        'ita-catania': 'Catania',
        'ita-cesena': 'Cesena',
        'ita-chievo-verona': 'Chievo-Verona',
        'ita-fiorentina': 'Fiorentina',
        'ita-genoa': 'Genoa',
        'ita-inter': 'Internazionale',
        'ita-juventus': 'Juventus',
        'ita-lazio': 'Lazio',
        'ita-lecce': 'Lecce',
        'ita-milan': 'A.C Milan',
        'ita-napoli': 'Napoli',
        'ita-novara': 'Novara',
        'ita-palermo': 'Palermo',
        'ita-parma': 'Parma',
        'ita-roma': 'Roma',
        'ita-siena': 'Siena',
        'ita-udinese': 'Udinese',
        'sco-aberdeen': 'Aberdeen',
        'sco-celtic': 'Celtic',
        'sco-dundee-united': 'Dundee Utd',
        'sco-dunfermline-athletic': 'Dunfermline',
        'sco-elgin-city': 'Elgin City',
        'sco-glasgow-rangers': 'Rangers',
        'sco-hearts': 'Hearts',
        'sco-hibernian': 'Hibs',
        'sco-inverness-caledonian-thistle': 'Inverness',
        'sco-kilmarnock': 'Kilmarnock',
        'sco-motherwell': 'Motherwell',
        'sco-st-johnstone': 'St. Johnstone',
        'sco-st-mirren': 'St. Mirren',
        'germ-mainz-05': '1. FSV Mainz 05',
        'germ-nur': '1. FC Nuremberg',
        'germ-hoffenheim': 'Hoffenheim',
        'germ-bayer-leverkusen': 'Bayer Leverkusen',
        'germ-bayern-munchen': 'Bayern Munich',
        'germ-borussia-dortmund': 'Borussia Dortmund',
        'germ-borussia-m': 'Borussia Moenchengladbach',
        'germ-augsburg': 'Augsburg',
        'germ-fc-koln': 'FC Koln',
        'germ-schalke-04': 'Schalke 04',
        'germ-hamburger-sv': 'Hamburger SV',
        'germ-hannover-96': 'Hannover 96',
        'germ-hertha-berlin': 'Hertha Berlin',
        'germ-kaiserslautern': 'Kaiserslautern',
        'germ-ksc': 'Karlsruher SC',
        'germ-freiburg': 'Freiburg',
        'germ-werder-bremen': 'Werder Bremen',
        'germ-vfb-oldenburg': 'VfB Oldenburg',
        'germ-vfb-stuttgart': 'VfB Stuttgart',
        'germ-wolfsburg': 'Wolfsburg',
        'germ-ein-frank': 'Eintracht Frankfurt',
        'fr-ajaccio': 'Ajaccio',
        'fr-auxerre': 'Auxerre',
        'fr-bordeaux': 'Bordeaux',
        'fr-brest': 'Brest',
        'fr-caen': 'Caen',
        'fr-dijon': 'Dijon',
        'fr-evian-thonon-gaillard': 'Evian Thoron Gaillard',
        'fr-lille': 'Lille',
        'fr-lorient': 'Lorient',
        'fr-lyon': 'Lyon',
        'fr-marseille': 'Marseille',
        'fr-montpellier': 'Montpellier',
        'fr-nancy': 'Nancy',
        'fr-nice': 'Nice',
        'fr-paris-saint-germain': 'Paris St. Germain',
        'fr-saint-etienne': 'St. Etienne',
        'fr-sochaux': 'Sochaux',
        'fr-stade-rennais': 'Stade Rennais',
        'fr-toulouse': 'Toulouse',
        'fr-valenciennes': 'Valenciennes',
        'ire-bohemians': 'Bohemians',
        'ire-bray-wanderers': 'Bray Wanderers',
        'ire-derry-city': 'Derry City',
        'ire-drogheda-united': 'Drogheda United',
        'ire-dundalk': 'Dundalk',
        'ire-galway-united': 'Galway United',
        'ire-shamrock-rovers': 'Shamrock Rovers',
        'ire-sligo-rovers': 'Sligo Rovers',
        'ire-st-patricks-athletic': 'St. Patrick\'s Athletic',
        'ire-ucd': 'UCD',
        'port-academica': 'Academia',
        'port-beira-mar': 'Beira Mar',
        'port-benfica': 'Benfica',
        'port-braga': 'Braga',
        'port-guimaraes': 'Guimares',
        'port-maritimo': 'Maritimo',
        'port-nacional': 'Nacional',
        'port-naval-de-maio': 'Naval de Maio',
        'port-olhanense': 'Olhanense',
        'port-pacos-ferreira': 'Pacos Ferreira',
        'port-portimonense': 'Portimonense',
        'port-porto': 'Porto',
        'port-rio-ave': 'Rio Ave',
        'port-sporting': 'Sporting',
        'port-uniao-leiria': 'Uniao Leiria',
        'port-vitoria-setubal': 'Vitoria Setubal',
        'neth-ajax': 'Ajax',
        'neth-az-alkmaar': 'AZ Alkmaar',
        'neth-de-graafschap': 'De Graafschap',
        'neth-den-haag': 'Den Haag',
        'neth-excelsior': 'Excelsior',
        'neth-feyenoord': 'Feyenoord',
        'neth-groningen': 'Groningen',
        'neth-heerenveen': 'Heerenveen',
        'neth-heracles-almelo': 'Heracles Almelo',
        'neth-nac-breda': 'NAC Breda',
        'neth-nec-nijmegen': 'NEC Nijmegen',
        'neth2-pec-zwolle': 'PEC Zwolle',
        'neth-psv-eindhoven': 'PSV Eindhoven',
        'neth-rkc-waalwijk': 'RKC Waalwijk',
        'neth-roda': 'Roda',
        'neth-twente': 'FC Twente',
        'neth-utrecht': 'Utrecht',
        'neth-vitesse': 'Vitesse',
        'neth-vvv-venlo': 'VVV Venlo',
        'neth2-willem-ii': 'Willem II',
        'tur-ankaragucu': 'Ankaragucu',
        'tur-antalyaspor': 'Antalyaspor',
        'tur-besiktas': 'Besiktas',
        'tur-bursaspor': 'Bursaspor',
        'tur-eskisehirspor': 'Eskisehirspor',
        'tur-fenerbahce': 'Fenerbahce',
        'tur-galatasaray': 'Galatasaray',
        'tur-gaziantepspor': 'Gaziantepspor',
        'tur-genclerbirligi': 'Genclerbirligi',
        'tur-istanbulbb': 'Istanbul BB',
        'tur-karabukspor': 'Karabukspor',
        'tur-kayserispor': 'Kayserispor',
        'tur-manisaspor': 'Manisaspor',
        'tur-mersinidmanyurdu': 'Mersinidmanyurdu',
        'tur-orduspor': 'Orduspor',
        'tur-samsunspor': 'Samsunspor',
        'tur-sivasspor': 'Sivasspor',
        'tur-trabzonspor': 'Trabzonspur',
        'oz-adelaide-united': 'Adelaide United',
        'oz-brisbane-roar': 'Brisbane Roar',
        'oz-central-coast-mariners': 'Central Coast Mariners',
        'oz-gold-coast-united': 'Gold Coast United',
        'oz-melbourne-heart': 'Melbourne Heart',
        'oz-melbourne-victory': 'Melbourne Victory',
        'oz-newcastle-jets': 'Newcastle Jets',
        'oz-perth-glory': 'Perth Glory',
        'oz-sydney': 'Sydney',
        'oz-wellington-phoenix': 'Wellington Phoenix',
        'oz-western-sydney': 'Western Sydney Wanderers',
        'bra-america-mineiro': 'America Mineiro',
        'bra-atletico-goianiense': 'Atletico Goianiense',
        'bra-atletico-mineiro': 'Atletico Mineiro',
        'bra-atletico-pr': 'Atletico PR',
        'bra-avai': 'Avai',
        'bra-botafogo': 'Botafogo',
        'bra-ceara': 'Ceara',
        'bra-corinthians': 'Corinthians',
        'bra-coritiba': 'Coritiba',
        'bra-cruzeiro': 'Cruzeiro',
        'bra-esporte-clube-bahia': 'Esporte Clube Bahia',
        'bra-figueirense': 'Figueirense',
        'bra-flamengo': 'Flamengo',
        'bra-fluminense': 'Fluminense',
        'bra-gremio': 'Gremio',
        'bra-internacional': 'Internacional',
        'bra-nautico-capibaribe': 'Nautico Capibaribe',
        'bra-palmeiras': 'Palmeiras',
        'bra-ponte-preta': 'Ponte Presa',
        'bra-portuguesa-de-desportos': 'Portuguesa de Desportos',
        'bra-santos': 'Santos',
        'bra-sao-paulo': 'Sao Paulo',
        'bra-sport-recife': 'Sport Recife',
        'bra-vasco-da-gama': 'Vasco da Gama',
        'gre-aek-athen': 'AEK Athens',
        'gre-aris-salonika': 'Aris Salonika',
        'gre-asteras-tripoli': 'Asteras Tripoli',
        'gre-atromitos-athens': 'Atromitos Athens',
        'gre-ergotelis': 'Ergotelis',
        'gre-fc-xanthi': 'FC Xanthi',
        'gre-giannina': 'Giannina',
        'gre-kerkyra': 'Kerkyra',
        'gre-levadiakos': 'Levadiakos',
        'gre-ofi-crete': 'OFI Crete',
        'gre-olympiakos': 'Olympiakos',
        'gre-panathinaikos': 'Panathinaikos',
        'gre-panetolikos': 'Panetolikos',
        'gre-panionios': 'Panionios',
        'gre-paok-salonika': 'PAOK Salonika',
        'alb-apolonia-fier': 'Apolonia Fier',
        'alb-besa-kavaje': 'Besa Kavaje',
        'alb-bilisht-sporti': 'Bilisht Sporti',
        'alb-bylis-ballshi': 'Bylis Ballshi',
        'alb-elbasani': 'Elbasani',
        'alb-flamurtari-vlora': 'Flamurtari Vlora',
        'alb-kastrioti-kruje': 'Kastrioti Kruje',
        'alb-laci': 'Laci',
        'alb-lushnja': 'Lushnja',
        'alb-partizani-tirana': 'Partizani Tirana',
        'alb-shkumbini-peqin': 'Shkumbini Peqin',
        'alb-skenderbeu-korce': 'Skenderbeu Korce',
        'alb-teuta-durres': 'Teuta Durres',
        'alb-tirana': 'Tirana',
        'alb-veleciku-koplik': 'Veleciku Koplik',
        'alb-vllaznia-shkoder': 'Vllaznia Shkoder',
        'arg-all-boys': 'All Boys',
        'arg-argentinos-juniors': 'Argentinos Juniors',
        'arg-arsenal-de-sarandi': 'Arsenal de Sarandi',
        'arg-atletico-de-rafaela': 'Atletico de Rafaela',
        'arg-atletico-tigre': 'Atletico Tigre',
        'arg-banfield': 'Banfield',
        'arg-belgrano': 'Belgrano',
        'arg-boca-juniors': 'Boca Juniors',
        'arg-colon': 'Colon',
        'arg-estudiantes': 'Estudiantes',
        'arg-godoy-cruz': 'Godoy Cruz',
        'arg-independiente': 'Independiente',
        'arg-lanus': 'Lanus',
        'arg-newells-old-boys': 'Newell\'s Old boys',
        'arg-olimpo': 'Olimpo',
        'arg-racing-club': 'Racing Club',
        'arg-river-plate': 'River Plate',
        'arg-san-lorenzo': 'San Lorenzo',
        'arg-san-martin-san-juan': 'San Martin San Juan',
        'arg-union-de-santa-fe': 'Union de Santa Fe',
        'arg-velez-sarsfield': 'Velez Sarsfield',
        'aus-admira-wacker': 'Admira Wacker',
        'aus-austria-vienna': 'Austria Vienna',
        'aus-fc-wacker-innsbruck': 'FC Wacker Innsbruck',
        'aus-kapfenberg': 'Kapfenburg',
        'aus-mattersburg': 'Mattersburg',
        'aus-ried': 'Ried',
        'aus-salzburg': 'Salzburg',
        'aus-sk-rapid-wien': 'SK Rapid Wien',
        'aus-sturm-graz': 'Sturm Graz',
        'bel-anderlecht': 'Anderlecht',
        'bel-beerschot': 'Beerschot',
        'bel-cercle-brugge': 'Cercle Brugge',
        'bel-club-brugge': 'Club Brugge',
        'bel-genk': 'Genk',
        'bel-germinal-beerschot': 'Germinal Beerschot',
        'bel-kaa-gent': 'KAA Gent',
        'bel-kortrijk': 'Kortrijk',
        'bel-kv-mechelen': 'KV Mechelen',
        'bel-lierse': 'Lierse',
        'bel-mons': 'Mons',
        'bel-oud-heverlee': 'Oud-Heverlee',
        'bel-sporting-lokeren': 'Sporting Lokeren',
        'bel-st-truiden': 'St. Truiden',
        'bel-standard-liege': 'Standard Liege',
        'bel-westerlo': 'Westerlo',
        'bel-zulte-waregem': 'Zulte Waregem',
        'cze-banik-ostrava': 'Banik Ostrava',
        'cze-bohemians-1905': 'Bohemians 1905',
        'cze-dukla-praha': 'Dukla Praha',
        'cze-dynamo-budejovice': 'Dynamo Budejovice',
        'cze-hradec-kralove': 'Hradec Kralove',
        'cze-jablonec': 'Jablonec',
        'cze-mlada-boleslav': 'Mlada Boleslav',
        'cze-marila-pribram': 'Marila Pribram',
        'cze-sigma-olomouc': 'Sigma Olomouc',
        'cze-slavia-praha': 'Slavia Praha',
        'cze-slovan-liberec': 'Slovan Liberec',
        'cze-slovacko': 'Slovacko',
        'cze-sparta-praha': 'Sparta Praha',
        'cze-teplice': 'Teplice',
        'cze-viktoria-zizkov': 'Viktoria Zizkov',
        'cze-viktoria-plzeri': 'Viktoria Plzeri',
        'den-aalborg': 'Aalborg',
        'den-agf-aarhus': 'AGF Aarhus',
        'den-brondby': 'Brondby',
        'den-fc-copenhagen': 'FC Copenhagen',
        'den-fc-nordsjaelland': 'FC Nordsjaelland',
        'den-hb-koge': 'HB Koge',
        'den-horsens': 'Horsens',
        'den-lyngby': 'Lyngby',
        'den-midtjylland': 'Midtjylland',
        'den-odense': 'Odense',
        'den-silkeborg': 'Silkeborg',
        'den-sonderjyske': 'Sonderjyske',
        'ni-ballinamallard-fc': 'Ballinamallard FC',
        'ni-ballymena': 'Ballymena',
        'ni-cliftonville': 'Cliftonville',
        'ni-coleraine': 'Coleraine',
        'ni-crusaders': 'Crusaders',
        'ni-distillery': 'Lisburn Distillery',
        'ni-donegal-celtic': 'Donegal Celtic',
        'ni-dungannon': 'Dungannon Swifts',
        'ni-glenavon': 'Glenavon',
        'ni-glentoran': 'Glentoran',
        'ni-linfield': 'Linfield',
        'ni-portadown': 'Portadown',
        'pol-cracovia-krakow': 'Cracovie Krakow',
        'pol-gks-belchatow': 'GKS Belchatow',
        'pol-gornik-zabrze': 'Gornik Zabrze',
        'pol-jagiellonia-bialystok': 'Jagiellonia Bialystok',
        'pol-korona-kielce': 'Korona Kielce',
        'pol-lech-poznan': 'Lech Poznan',
        'pol-lechia-gdansk': 'Lechia Gdansk',
        'pol-legia-warszawa': 'Legia Warszawa',
        'pol-lodzki-ks': 'Lodzki KS',
        'pol-podbeskidzie-bielsko': 'Podbeskidzie Bielsko',
        'pol-polonia-warszawa': 'Polonia Warszawa',
        'pol-ruch-chorzow': 'Ruch Chorzow',
        'pol-slask-wroclaw': 'Slask Wroclaw',
        'pol-widzew-lodz': 'Widzew Lodz',
        'pol-wisla-krakow': 'Wisla Krakow',
        'pol-zaglebie-lubin': 'Zaglebie Lubin',
        'ukr-arsenal-kiev': 'Arsenal Kiev',
        'ukr-chornomorets-odessa': 'Chornomorets Odessa',
        'ukr-dnipro-dnipropetrovsk': 'Dnipro Dnipropetrovsk',
        'ukr-dynamo-kyiv': 'Dynamo Kyiv',
        'ukr-illychivets-mariupol': 'Illychivets Mariupol',
        'ukr-karpaty': 'Karpaty',
        'ukr-kryvbas-kryvyi-rih': 'Kryvbas Kryvyi Rih',
        'ukr-metalist-charkiw': 'Metalist Chrkiw',
        'ukr-metalurh-donetsk': 'Metalurh Donetsk',
        'ukr-obolon-kyiv': 'Obolon Kyiv',
        'ukr-oleksandriya': 'Oleksandriya',
        'ukr-shakhtar-donetsk': 'Shakhtar Donetsk',
        'ukr-tavriya-simferopol': 'Tavriya Simferopol',
        'ukr-volyn-lutsk': 'Volyn Lutsk',
        'ukr-vorskla-poltava': 'Vorskla Poltava',
        'ukr-zorya-luhansk': 'Zorya Luhansk',
        'eng-champ-barnsley': 'Barnsley',
        'eng-champ-birmingham': 'Birmingham',
        'eng-champ-blackburn-rovers': 'Blackburn Rovers',
        'eng-champ-blackpool': 'Blackpool',
        'eng-champ-bolton-wanderers': 'Bolton Wanderers',
        'eng-champ-brighton': 'Brighton',
        'eng-champ-bristolcity': 'Bristol City',
        'eng-champ-burnley': 'Burnley',
        'eng-champ-cardiff': 'Cardiff',
        'eng-champ-charlton': 'Charlton',
        'eng-champ-crystalpalace': 'Crystal Palace',
        'eng-champ-derby': 'Derby Co.',
        'eng-champ-huddersfield': 'Huddersfield',
        'eng-champ-hullcity': 'Hull City',
        'eng-champ-ipswich': 'Ipswich',
        'eng-champ-leeds': 'Leeds',
        'eng-champ-leicester': 'Leicester',
        'eng-champ-middlesbrough': 'Middlesbrough',
        'eng-champ-millwall': 'Millwall',
        'eng-champ-notts-forest': 'Notts Forest',
        'eng-champ-peterborough': 'Peterborough',
        'eng-champ-shef-weds': 'Sheff Weds',
        'eng-champ-watford': 'Watford',
        'eng-champ-wolverhampton-wanderers': 'Wolves',
        'rus-amkar-perm': 'Perm',
        'rus-anzhi-makhachkala': 'Makhachkala',
        'rus-cska-moscow': 'CSKA Moscow',
        'rus-dynamo-moscow': 'Dynamo Moscow',
        'rus-krasnodar': 'Krasnodar',
        'rus-krylya-sovetov': 'Krylya Sovetov',
        'rus-lokomotiv-moscow': 'Locomotiv Moscow',
        'rus-rostov': 'Rostov',
        'rus-rubin-kazan': 'Rubin Kazan',
        'rus-spartak-moscow': 'Spartak Moscow',
        'rus-spartak-nalchik': 'Spartak Nalchik',
        'rus-terek-grozny': 'Terek Grozny',
        'rus-tom-tomsk': 'Tom Tomsk',
        'rus-volga': 'Volga',
        'rus-zenit': 'Zenit',
        'jap-albirex-niigata': 'Albirex Niigata',
        'jap-avispa-fukuoka': 'Avispa Fukuoka',
        'jap-cerezo-osaka': 'Cerezo Osaka',
        'jap-gamba-osaka': 'Gamba Osaka',
        'jap-hiroshima': 'Hiroshima',
        'jap-jubilo-iwata': 'Jubilo Iwata',
        'jap-kashima-antlers': 'Kashima Antlers',
        'jap-kashiwa-reysol': 'Kashiwa Reysol',
        'jap-kawasaki': 'Kawasaki',
        'jap-montedio-yamagata': 'Monetdio Yamagata',
        'jap-nagoya-grampus': 'Nagoya Grampus',
        'jap-omiya-ardija': 'Omiya Ardija',
        'jap-shimizu-s-pulse': 'Shimizu S Pulse',
        'jap-urawa-reds': 'Urawa Reds',
        'jap-vegalta-sendai': 'Vegalta Sendai',
        'jap-ventforet-kofu': 'Ventforet Kofu',
        'jap-vissel-kobe': 'Vissel Kobe',
        'jap-yokohama-f-marinos': 'Yokohama F Marinos',
        'swe-aik': 'AIK',
        'swe-atvidabergs': 'Atvidabergs',
        'swe-bk-hacken': 'BK Hacken',
        'swe-djurgardens': 'Djurgardens',
        'swe-elfsborg': 'Elfsborg',
        'swe-gais': 'Gais',
        'swe-gefle-if': 'Gefle',
        'swe-helsingborgs': 'Helsingborgs',
        'swe-ifk-goteborg': 'Goteborg',
        'swe-ifk-norrkoping': 'Norrkoping',
        'swe-kalmar': 'Kalmar',
        'swe-malmo': 'Malmo',
        'swe-mjallby': 'Mjallby',
        'swe-orebro': 'Orebro',
        'swe-sundsvall': 'Sundsvall',
        'swe-syrianska': 'Syrianska',
        'conmebol-argentina': 'Argentina',
        'conmebol-bolivia': 'Bolivia',
        'conmebol-brazil': 'Brazil',
        'conmebol-colombia': 'Colombia',
        'conmebol-conmebol': 'CONMEBOL',
        'conmebol-ecuador': 'Ecuador',
        'conmebol-paraguay': 'Paraguay',
        'conmebol-peru': 'Peru',
        'conmebol-uruguay': 'Uruguay',
        'conmebol-venezuela': 'Venezuela',
        'euro-mascot-1980': 'Italy \'80 (Pinocchio)',
        'euro-mascot-1984': 'France \'84 (Peno)',
        'euro-mascot-1988': 'W. Germany \'88 (Berni)',
        'euro-mascot-1992': 'Sweden \'92 (Rabbit)',
        'euro-mascot-1996': 'England \'96 (Goliath)',
        'euro-mascot-2000': 'Netherlands-Belgium \'00 (Benelucky)',
        'euro-mascot-2004': 'Portugal \'04 (Kinas)',
        'euro-mascot-2008': 'Austria-Switzerland \'08 (Trix and Flix)',
        'rom-astra-ploiesti': 'Astra Ploiesti',
        'rom-ceahlaul-piatra-neamt': 'Ceahlaul Piatra Neamt',
        'rom-cfr-cluj': 'CFR Cluj',
        'rom-concordia-chiajna': 'Concordia Chiajna',
        'rom-csu-vointa-sibiu': 'CSU Vointa Sibiu',
        'rom-dacia-mioveni': 'Dacia Mioveni',
        'rom-dinamo-bucuresti': 'Dinamo Bucuresti',
        'rom-fc-brasov': 'FC Brasov',
        'rom-gaz-metan-medias': 'Gaz Metan Medias',
        'rom-otelul-galati': 'Otelul Galati',
        'rom-pandurii-targu-jiu': 'Pandurii Targu Jiu',
        'rom-petrolul-ploiesti': 'Petrolul Ploiesti',
        'rom-rapid-bucuresti': 'Rapid Bucuresti',
        'rom-sportul-studentesc': 'Sportul Studentesc',
        'rom-steaua-bucuresti': 'Steaua Bucuresti',
        'rom-targu-mures': 'Targu Mures',
        'rom-universitatea-cluj': 'Universitatea Cluj',
        'rom-vaslui': 'Vaslui'
    }
    print "Fired: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
    r = praw.Reddit(user_agent='Some bot name for some subreddit')
    r.login('some_user_name', 'some_password')
    for msg in r.get_unread(limit=None):
        subj = str(msg.subject)
        print "Subject: " + subj
        if subj == 'crest':
            print msg
            auth = str(msg.author)
            body = str(msg.body)
            print "Author: " + auth
            print "Message content: " + body
            sub = r.get_subreddit('football')
            if body in teams:
                ftext = str(teams[body])
                sub.set_flair(auth, ftext, body)
                with open('log.txt', 'a') as logfile:
                    tn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    lm = ' : ' + body + ' @ ' + tn
                    logfile.write('\n\rAdded: ' + auth + ' : ' + ftext + lm)
                print "Setting flair: " + auth + " : " + ftext + " : " + body
                msg.mark_as_read()

if __name__ == '__main__':
    main()
