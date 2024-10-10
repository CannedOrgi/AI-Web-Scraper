import re

text = """
Accounting, Insurance, and Finance
1.	HSBC- https://www.about.hsbc.co.uk/
2.	Barclays- https://home.barclays/careers/
3.	Lloyds Banking Group- https://www.lloydsbankinggrouptalent.com/
4.	NatWest Group- https://jobs.natwestgroup.com/
5.	Standard Chartered- https://www.sc.com/en/global-careers/our-employee-stories/
6.	Aviva- https://careers.aviva.co.uk/
7.	Prudential- https://www.prudentialplc.com/en/careers
8.	Legal & General- https://careers.legalandgeneral.com/
9.	Zurich Insurance Group- https://www.zurich.co.uk/careers
10.	AXA UK- https://jobs.axa.co.uk/
11.	Santander UK- https://www.santander.co.uk/
12.	Abrdn- https://www.abrdn.com/en-gb
13.	Nationwide Building Society - https://www.nationwide-jobs.co.uk/ https://www.nationwide.co.uk/
14.	Royal London Group - https://www.royallondon.com/
15.	Fidelity International - https://www.fidelityinternational.com/
16.	Phoenix Group - https://www.thephoenixgroup.com/
17.	Direct Line Group - https://www.directlinegroup.co.uk/en/index.html

Business Consulting and Management
1.	PricewaterhouseCoopers- https://www.pwc.co.uk/careers.html
2.	Deloitte- https://www.deloitte.com/uk/en/careers.html
3.	Ernst & Young- https://www.ey.com/en_uk/careers/what-its-like-to-work-here/people-stories
4.	KPMG- https://kpmg.com/uk/en/home/careers.html
5.	Grant Thornton UK - https://www.grantthornton.co.uk/people/ https://www.grantthornton.co.uk/careers/
6.	BDO - https://www.bdo.co.uk/
7.	Accenture- https://www.accenture.com/gb-en/careers
8.	Capgemini- https://www.capgemini.com/gb-en/careers/meet-our-people/
9.	McKinsey & Company- https://www.mckinsey.com/uk/careers
10.	Boston Consulting Group- https://careers.bcg.com/early-careers
11.	Bain & Company- https://www.bain.com/
12.	Oliver Wyman- https://www.oliverwyman.com/
13.	IBM Global Business Services- https://www.ibm.com/uk-en
14.	Kearney - https://www.kearney.com/
15.	Roland Berger - https://www.rolandberger.com/en/UnitedKingdom.html
16.	FTI Consulting - https://www.fticonsulting.com/uk/
17.	Mott MacDonald - https://www.mottmac.com/united-kingdom
18.	Alvarez & Marsal - https://www.alvarezandmarsal.com/global-locations/united-kingdom
19.	OC&C Strategy Consultants - https://www.occstrategy.com/en/
20.	LEK Consulting - https://www.lek.com/

Government and NGO
1.	HM Revenue and Customs (HMRC)- https://www.civil-service-careers.gov.uk/departments/working-for-hm-revenue-and-customs-landing-page/
2.	Department for Work and Pensions (DWP)- https://www.civil-service-careers.gov.uk/dwp-our-careers/
3.	Ministry of Defence (MoD)- https://www.civil-service-careers.gov.uk/mod-hub/
4.	Home Office- https://careers.homeoffice.gov.uk/ https://www.civil-service-careers.gov.uk/departments/working-for-the-home-office/
5.	Department for Education (DfE)- https://www.civil-service-careers.gov.uk/departments/working-for-the-department-for-education/
6.	Department for Transport (DfT)- https://careers.dft.gov.uk/stories/
7.	Environment Agency- https://environmentagencycareers.co.uk
8.	Foreign, Commonwealth & Development Office (FCDO)- https://www.fcdoservicescareers.co.uk/our-people/
9.	Met Office- https://careers.metoffice.gov.uk/stories
10.	UK Civil Service- https://www.gov.uk/government/organisations/civil-service
11.	Oxfam- https://www.oxfam.org.uk/
12.	Amnesty International UK- https://www.amnesty.org.uk/
13.	Save the Children UK- https://www.savethechildren.org.uk/
14.	World Wildlife Fund (WWF) UK- https://www.wwf.org.uk/
15.	Greenpeace UK- https://www.greenpeace.org.uk/
16.	British Red Cross- https://www.redcross.org.uk/
17.	Tearfund - https://www.tearfund.org/
18.	Royal Society for the Protection of Birds (RSPB) - https://www.rspca.org.uk/
19.	Médecins Sans Frontières (MSF) UK - https://msf.org.uk/
20.	Plan International UK - https://plan-uk.org/
Health and Care
1.	NHS- https://www.healthcareers.nhs.uk/working-health/real-life-stories
2.	Bupa- https://careers.bupa.co.uk/news-and-stories
3.	HCRG Care Group- https://www.hcrgcaregroup.jobs/
4.	Spire Healthcare- https://www.spirehealthcare.com/recruitment
5.	Care UK- https://www.careuk.com/
6.	Four Seasons Health Care- https://careers.fshcgroup.com/jobs/our-people/
7.	HC-One- https://apply.hc-one.co.uk/working-for-hc-one/colleague-stories.aspx
8.	Priory Group- https://jobs.priorygroup.com/about-us/meet-our-people/ https://jobs.priorygroup.com/blog/
9.	Nuffield Health- https://www.nuffieldhealthcareers.com/stories 
10.	Cygnet Health Care- https://careers.cygnetgroup.com/ 
11.	GlaxoSmithKline- https://www.gsk.com/en-gb/
12.	AstraZeneca- https://www.astrazeneca.co.uk/
13.	Pfizer UK- https://www.pfizer.co.uk/
14.	Roche UK- https://www.roche.co.uk/
15.	Sanofi UK- https://www.sanofi.co.uk/en
16.	Boots- https://www.boots-uk.com/
17.	Circle Health Group- https://www.circlehealthgroup.co.uk/
18.	HCA Healthcare UK- https://www.hcahealthcare.co.uk/
19.	Johnson & Johnson UK - https://jnj.co.uk/
20.	Novartis UK - https://www.novartis.com/uk-en/

Law and Legal
1.	Clifford Chance- https://jobs.cliffordchance.com/our-people
2.	Linklaters- https://careers.linklaters.com/en/early-careers/our-people
3.	A&O Shearman- https://www.aoshearman.com/
4.	Freshfields Bruckhaus Deringer- https://www.freshfields.com/en-gb/careers/uk
5.	Slaughter and May- https://www.slaughterandmay.com/careers/trainee-solicitors/our-people/
6.	Herbert Smith Freehills- https://careers.herbertsmithfreehills.com/global/en/uk/insight-hub
7.	Pinsent Masons- https://www.pinsentmasons.com/careers
8.	Eversheds Sutherland- https://www.eversheds-sutherland.com/en/United-Kingdom/careers/careers-page
9.	DLA Piper- https://earlycareers.dlapiper.com/uk/
10.	Norton Rose Fulbright- https://www.nortonrosefulbright.com/en-gb/graduates
11.	Herbert Smith Freehills- https://www.herbertsmithfreehills.com/legal-and-regulatory/uk
12.	CMS- https://cms.law/en/gbr/
13.	Hogan Lovells - https://www.hoganlovells.com/en/locations/london
14.	Ashurst - https://www.ashurst.com/
15.	Baker McKenzie - https://www.bakermckenzie.com/en/
16.	Simmons & Simmons - https://www.simmons-simmons.com/
17.	Macfarlanes - https://www.macfarlanes.com/home/
18.	Travers Smith - https://www.traverssmith.com/
19.	Addleshaw Goddard - https://www.addleshawgoddard.com/en/
20.	Burges Salmon - https://www.burges-salmon.com/

Marketing and Advertising and PR
1.	WPP- https://www.wpp.com/
2.	Publicis Groupe UK- https://www.publicisgroupeuk.com/
3.	Omnicom Group UK- https://omgukcareers.com/
4.	Saatchi & Saatchi- https://saatchi.co.uk/
5.	Ogilvy - https://www.ogilvy.com/uk/
6.	Dentsu - https://www.dentsu.com/uk/en
7.	Havas UK- https://www.havas.com/
8.	Edelman UK- https://www.edelman.co.uk/
9.	Weber Shandwick UK- https://webershandwick.co.uk/
10.	Grey UK- https://www.grey.com/locations/united-kingdom
11.	M&C Saatchi - https://mcsaatchi.london/
12.	TBWA UK - https://tbwalondon.com/
13.	VCCP - https://www.vccp.com/
14.	McCann Worldgroup UK - https://www.mccannworldgroup.com/
15.	Bartle Bogle Hegarty - https://www.bartleboglehegarty.com/
16.	VML- https://www.vml.com/united-kingdom
17.	Next 15 - https://www.next15.com/
18.	FleishmanHillard UK - https://fleishmanhillard.co.uk/ 
19.	Hill+Knowlton - https://hillandknowlton.com/
20.	AMV BBDO - https://www.amvbbdo.com/ 

Property and Infrastructure
1.	British Land- https://www.britishland.com/careers
2.	Landsec- https://landsec.com/life-landsec
3.	Taylor Wimpey- https://www.taylorwimpey.co.uk/
4.	Barratt Developments- https://www.barrattcareers.co.uk/
5.	Persimmon- https://www.persimmonhomes.com/corporate/careers/
6.	Balfour Beatty- https://www.balfourbeattycareers.com/
7.	Mace Group- https://www.macegroup.com/people/experienced-people?service=&location=96e44aa0-3752-4f6e-95e6-21238df62062
8.	Savills- https://www.savills.co.uk/contact-us/careers/why-join-us/savills-stories.aspx
9.	Jones Lang LaSalle- https://www.jll.co.uk/
10.	Cushman & Wakefield- https://www.cushmanwakefield.com/en/united-kingdom
11.	CBRE UK- https://www.cbre.co.uk/
12.	Kier Group- https://www.kier.co.uk/
13.	Lendlease UK - https://www.lendlease.com/uk/
14.	Berkeley Group - https://www.berkeleygroup.co.uk/ 
15.	Bellway - https://www.bellway.co.uk/
16.	Redrow - https://www.redrow.co.uk/
17.	Hammerson - https://www.hammerson.com/
18.	Countryside Properties -. http://www.countrysidehomes.com/
19.	SEGRO - https://www.segro.com/
20.	St. Modwen Properties - https://www.stmodwen.co.uk/
Tech, IT and Digital
1.	BT Group- https://jobs.bt.com/content/Life-at-BT-Group/?locale=en_GB
2.	Vodafone- https://careers.vodafone.com/uk/life-at-vodafone/
3.	Arm- https://careers.arm.com/stories
4.	Sage Group- https://www.sage.com/en-gb/company/careers/
5.	Capita- https://www.capita.com/careers/hear-our-brilliant-people
6.	BAE Systems- https://www.baesystems.com/en/careers/careers-in-the-uk/employee-stories
7.	Fujitsu UK- https://www.fujitsu.com/uk/about/careers/early-careers/
8.	Atos- https://atos.net/advancing-what-matters/en/join-us
9.	IBM UK- https://www.ibm.com/uk-en/careers/culture
10.	Amazon UK- https://www.amazon.jobs/en-gb
11.	Cisco UK- https://www.cisco.com/c/en_uk/about.html#~digital-society
12.	Infosys UK - https://www.infosys.com/uk/public-sector/insights.html
13.	Tata Consultancy Services (TCS)- https://www.tcs.com/careers/united-kingdom

Grad Mentoring Sites
1.	https://www.brightnetwork.co.uk/
2.	https://earlycareers.colliers.com/graduate-testimonials/
3.	https://www.grb.uk.com/careers-advice/graduate-mentoring
4.	https://www.knowledgementoring.com/
5.	https://www.milkround.com/
6.	https://www.insidecareers.co.uk/
7.	https://step.org.uk/

"""

pattern = r"[\d]+.\s*([^-]+)-\s*(https?://\S+)"
matches = re.findall(pattern, text)

output_list = [f"{url.strip()}" for company, url in matches]
count=0
for item in output_list:
    print(item)
    count+=1
print(count)
