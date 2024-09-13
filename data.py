def save_testimonials(testimonials):
    """Save the updated testimonials back to the file."""
    with open(__file__, 'w') as f:
        content = f'company_testimonials = {testimonials}'
        f.write(content)

company_testimonials = [
{
    'company':'HSBC',
    'web_url':[
        'https://www.business.us.hsbc.com/en/campaigns/commercial-banking-client-stories',
        'https://www.trustpilot.com/review/www.hsbc.com'
        ]
},
{
    'company':'Barclays',
    'web_url':[
        'https://www.trustpilot.com/review/www.barclays.co.uk',
        'https://www.reviews.io/company-reviews/store/barclays'
    ]
},
{
    'company':'Lloyds Banking Group',
    'web_url':[
        'https://www.lloydsbankinggroup.com/careers/colleague-stories.html',
        'https://www.trustpilot.com/review/www.lloydsbankinggroup.com',
        'https://www.lloydsbankinggroup.com/careers/learn-and-develop/what-makes-lloyds-banking-group-worth-coming-back-to.html'
    ]
},
{
   'company': 'Natwest',
   'web_url':[
       'https://www.trustpilot.com/review/www.natwest.com'
   ] 
},
{
    'company':'Aviva',
    'web_url':[
        'https://www.aviva.com/about-us/our-customers/',
        'https://static.aviva.io/content/dam/document-library/adviser/individualprotection/pt151108c.pdf',
        'https://www.trustpilot.com/review/www.aviva.co.uk',
        'https://www.reviews.io/company-reviews/store/aviva',
        'https://tractable.ai/en/case-studies/aviva-testimonial'
    ]
},
{
    'company':'Standered Chartered',
    'web_url':[
        'https://www.sc.com/en/global-careers/our-employee-stories/',
        'https://www.trustpilot.com/review/www.standardchartered.com',
        'https://www.temenos.com/community/success-stories/standard-chartered-success-story/'
    ]
},
{
    'company':'Prudentials',
    'web_url':[
        'https://reviews.io/company-reviews/store/gc-prudential',
        'https://uk.trustpilot.com/review/mandg.com/pru',
        'https://uk.trustpilot.com/review/prudential.co.uk'
    ]
},
{
    'company':'Legal and General',
    'web_url':[
        'https://www.legalandgeneral.com/adviser/protection/adviser-toolkit/our-claims/case-studies/people-stories/',
        'https://www.trustpilot.com/review/legalandgeneral.com',
        'https://www.reviews.io/company-reviews/store/gc-legalgeneral',
        'https://prod-epi.legalandgeneral.com/insurance/life-insurance/critical-illness-cover/customer-testimonials/',
        'https://www.forbes.com/uk/advisor/life-insurance/legal-and-general-review/',
        'https://ie.trustpilot.com/review/legalandgeneral.com'
    ]
},
{
    'company':'Zurich',
    'web_url':[
        'https://www.insurancewatch.com.au/zurich-insurance-reviews.html',
        'https://www.trustpilot.com/review/www.zurich.com',
        'https://www.reviews.io/company-reviews/store/www.zurich.com',
        'https://www.trustpilot.com/review/www.zurich.co.uk',
        'https://www.productreview.com.au/listings/zurich-insurance'
    ]
},
{
    'company':'AXA UK',
    'web_url':[
        'https://www.axa.co.uk/about/customer-reviews/',
        'https://uk.trustpilot.com/review/www.axa.co.uk',
        'https://www.trustpilot.com/review/axa-travel-insurance.com',
        'https://www.reviews.io/company-reviews/store/gc-axainsurance',
        'https://www.feefo.com/en-GB/reviews/axa-direct?displayFeedbackType=SERVICE&timeFrame=YEAR',
        'https://www.axa.ie/general/customer-reviews/'

    ]

}
,{
    'company':'General',
    'web_url':[
        'https://www.parkstreetpeople.com/about-us/testimonials/',
        'https://www.emearecruitment.com/employers/testimonials',
        'https://www.hyperec.com/about-us/testimonials'
    ]
}

,{
    'company':'Atos',
    'web_url':[
        'https://sapeducation.atos.net/success-stories/',
        'https://atosjiujitsuhq.com/testimonials/',
        'https://in.adp.com/resources/what-others-say/testimonials/a/atos.aspx',
        'https://www.atosmedical.com/news/user-testimonials-3',
        'https://atoswellness.com.sg/beauty-testimonials/'

    ]
}
,{
    'company':'Capita',
    'web_url':[
        'https://uk.trustpilot.com/review/capita.co.uk'
   
    ]
}
,{
    'company':'Savills',
    'web_url':[
        'https://pdf.savills.com/idc_testimonials.pdf',
        'https://www.humancapitalsolutions.co.uk/pages/savills-testimonial-case-study',
        'https://www.trustpilot.com/review/www.savills.co.uk',
        'https://www.reviews.io/company-reviews/store/savills-com'
    ]
}
,{
    'company':'Landsec',
    'web_url':[
        'https://landsec.com/sites/default/files/2019-06/Landsec_AR2019_Our_Portfolio.pdf'
    ]
}
,{
    'company':'Vodafone',
    'web_url':[
        'https://uk.trustpilot.com/review/www.vodafone.co.uk',
        'https://www.trustpilot.com/review/www.vodafone.co.uk',
        'https://www.which.co.uk/reviews/mobile-phone-providers/article/mobile-phone-provider-reviews/vodafone-mobile-review-akiF04e5Ussf',
        'https://vodafone-uk.pissedconsumer.com/review.html',
        'https://www.broadband.co.uk/providers/vodafone/broadband/reviews',
        'https://www.reviews.io/company-reviews/store/vodafone-customer-service.co.uk',
        'https://www.reviews.io/company-reviews/store/blog-vodafone-co-uk'
    ]
}
,{
    'company':'BAE System',
    'web_url':[
        'https://www.baesystems.com/en/our-company/our-businesses/intelligence-and-security/capabilities-and-services/advanced-component-obsolescence/testimonials',
        'https://www.baesystems.com/en/careers/careers-in-the-uk/employee-stories',
        'https://www.baesystems.com/en-be/campaign-typhoon-for-belgium/typhoon-pilot-testimonials'
    ]
}
,{
    'company':'Microsoft UK',
    'web_url':[
        'https://ie.trustpilot.com/review/microsoft.uk'
        
    ]
}
,{
    'company':'BT Group',
    'web_url':[
        'https://www.bt.com/about/annual-reports/2023summary/',
        'https://www.trustpilot.com/review/bt.com'
    ]
}
,{
    'company':'Linklaters',
    'web_url':[
        'https://www.linklaters.com/en/client-services/employment-and-incentives/employment-testimonials',
        'https://careers.linklaters.com/early-careers/testimonials-from-our-rising-stars'
        
    ]
}
,{
    'company':'Freshfields Bruckhaus Deringer',
    'web_url':[
        'https://www.freshfields.com/en-gb/about-us/alumni/alumni-network/member-stories/',
        'https://www.salesforce.com/uk/resources/customer-stories/freshfields/'
        
    ]
}
,{
    'company':'Herbert Smith Freehills',
    'web_url':[
        'https://www.herbertsmithfreehills.com/pro-bono-legal/stories-from-herbert-smith-freehills-secondees-in-freetown-sierra-leone'
    ]
}
,{
    'company':'Cushman & Wakefield',
    'web_url':[
        'https://www.trustpilot.com/review/www.cushmanwakefield.co.uk'
        
    ]
}
,{
    'company':'Slaughter and May',
    'web_url':[
        'https://www.brightnetwork.co.uk/employer-advice/slaughter-and-may/slaughter-and-may-what-sets-you-apart/'
        
    ]
}
,{
    'company':'ARM Holdings',
    'web_url':[
        'https://www.trustpilot.com/review/arm.com'
    ]
}
,{
    'company':'Clifford Chance',
    'web_url':[
        'https://www.cliffordchance.com/content/dam/cliffordchance/Our-responsibilities/Annual-Review-2008.pdf'
    ]
}
,{
    'company':'Jones Lang LaSalle',
    'web_url':[
        'https://www.yelp.com/brands/jones-lang-lasalle'
    ]
}
,{
    'company':'Boston Consulting Group',
    'web_url':[
        'https://www.g2.com/products/boston-consulting-group/reviews'
    ]
}
,{
    'company':'Capgemini',
    'web_url':[
        'https://www.capgemini.com/pt-en/careers/meet-our-people/'
    ]
}
,{
    'company':'Pinsent Masons',
    'web_url':[
        'https://www.pinsentmasons.com/careers/vario/blog/enfinium-client-case-study',
        'https://www.ansarada.com/customers/pinsent-masons',
        'https://www.pinsentmasons.com/careers/vario/blog/greer-epton'

    ]
}
,{
    'company':'Norton Rose Fulbright',
    'web_url':[
        'https://www.nortonrosefulbright.com/en/about/our-firm/alumni-community/alumni-stories',
        'https://www.nortonrosefulbright.com/en-us/about/our-firm/alumni-community/alumni-stories/building-bridges--united-by-music--rail-tracks-and-pop-tracks'

    ]
}
,{
    'company':'Fujitsu UK',
    'web_url':[
        'https://uk.trustpilot.com/review/fujitsu.com',
        'https://www2.fujitsu.com/uk/customer-stories/cs-centrica-plc-20221118/'
    ]
}
,{
    'company':'Department for Work and Pensions (DWP)',
    'web_url':[
        'https://www.trustpilot.com/review/www.dwp.gov.uk'
    ]
}
,{
    'company':'Environment Agency ',
    'web_url':[
        'https://www.trustpilot.com/review/environment-agency.gov.uk'
    ]
}
,{
    'company':'British Land',
    'web_url':[
        'https://www.homeviews.com/company/british-land'
    ]
}
,{
    'company':'Barratt Developments',
    'web_url':[
        'https://www.barrattdevelopments.co.uk/land/testimonials',
        'https://www.trustpilot.com/review/www.barratthomes.co.uk',
        'https://www.trustpilot.com/review/www.barratthomes.co.uk?page=5',
        'https://www.barrattdevelopments.co.uk/media/media-releases/pr-2022/pr-23-03-2022'
    ]
}
,{
    'company':'Care UK',
    'web_url':[
        'https://uk.trustpilot.com/review/www.careuk.com',
        'https://www.helpinghandshomecare.co.uk/about-us/testimonials/'
    ]
}
,{
    'company':'Cygnet Health Care',
    'web_url':[
        'https://www.trustpilot.com/review/www.cygnethealth.co.uk',
        'https://www.carehome.co.uk/care_search_results.cfm/searchgroup/65432242909'
    ]
}
,{
    'company':'Taylor Wimpey',
    'web_url':[
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyer-takes-a-step-on-the-property-ladder-at-thorn-fields',
        'https://www.taylorwimpey.co.uk/customer-stories?page=6',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-buy-dream-house-together-at-the-orangery',
        'https://www.taylorwimpey.co.uk/customer-stories/waffles-finds-growing-up-at-shaw-valley-pawsitively-perfect',
        'https://www.taylorwimpey.co.uk/customer-stories/homeowners-find-perfect-home-at-stour-view-development',
        'https://www.taylorwimpey.co.uk/customer-stories/family-downsizes-with-the-three-bedroom-braxton',
        'https://www.taylorwimpey.co.uk/customer-stories/mother-and-daughter-take-step-to-new-beginnings-in-riven-stones',
        'https://www.taylorwimpey.co.uk/customer-stories/family-find-dream-home-at-bingham-gate',
        'https://taylorwimpeyspain.com/testimonials/',
        'https://www.taylorwimpey.co.uk/news/2024/may/couple-find-their-perfect-home-at-our-cheddar-development',
        'https://www.trustpilot.com/review/www.taylorwimpey.co.uk',
        'https://www.taylorwimpey.co.uk/customer-stories/family-surprises-children-with-dream-home-at-plumb-park',
        'https://www.taylorwimpey.co.uk/customer-stories/we-help-first-time-buyer-to-find-dream-home',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-finds-their-dream-home-in-south-newsham',
        'https://www.taylorwimpey.co.uk/customer-stories/london-family-find-their-dream-coastal-home-in-kirby-cross',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-buy-their-first-home-together-at-rothwells-farm',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-make-the-move-out-of-the-city-for-more-space-in-east-lothian',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyer-falls-in-love-with-apartment-life-at-chobham-manor',
        'https://www.taylorwimpey.co.uk/customer-stories/local-couple-settle-into-retirement-at-the-heath',
        'https://www.taylorwimpey.co.uk/customer-stories/second-time-taylor-wimpey-customer-finds-perfect-location-at-watermill-green',
        'https://www.taylorwimpey.co.uk/customer-stories/returning-taylor-wimpey-customers-embrace-lifestyle-change-at-woodlands-chase',
        'https://www.taylorwimpey.co.uk/customer-stories/another-happy-resident-at-our-osiers-square-development',
        'https://www.taylorwimpey.co.uk/customer-stories/young-family-leave-london-behind-for-a-quieter-life-in-aylesbury',
        'https://www.taylorwimpey.co.uk/customer-stories/a-dream-move-to-a-new-home-makes-perfect-sense-for-marcus',
        'https://www.taylorwimpey.co.uk/customer-stories/family-of-six-upsize-and-fall-in-love-with-our-orchard-chase-development-in-biggleswade',
        'https://www.taylorwimpey.co.uk/customer-stories/family-upsize-to-cosy-village-home-in-codicote',
        'https://www.taylorwimpey.co.uk/customer-stories/family-delighted-with-spacious-lydford-home-after-upsizing',
        'https://www.taylorwimpey.co.uk/customer-stories/help-to-buy-brings-an-end-to-renting-for-oxfordshire-couple',
        'https://www.taylorwimpey.co.uk/customer-stories/family-upsize-with-spacious-home-at-our-uttoxeter-development',
        'https://www.taylorwimpey.co.uk/customer-stories/last-few-homes-remaining-at-ambrose-gardens-in-swindon',
        'https://www.taylorwimpey.co.uk/customer-stories/family-take-a-step-up-the-property-ladder-in-herne-bay',
        'https://www.taylorwimpey.co.uk/customer-stories/easymover-helps-laura-take-a-step-up-the-property-ladder-in-edinburgh',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-overjoyed-with-flexible-manford-home-at-our-copthorne-development',
        'https://www.taylorwimpey.co.uk/customer-stories/new-residents-join-growing-community-at-seagrave-park',
        'https://www.taylorwimpey.co.uk/customer-stories/part-exchange-scheme-helps-couple-make-the-move-to-rownhams',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-make-a-return-to-the-south-coast-countryside',
        'https://www.taylorwimpey.co.uk/customer-stories/family-take-a-step-up-the-property-ladder-in-herne-bay',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-overjoyed-with-flexible-manford-home-at-our-copthorne-development',
        'https://www.taylorwimpey.co.uk/customer-stories/buyers-downsize-with-an-easy-move-to-kilwinning',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-celebrate-being-the-first-to-move-to-our-newton-park-development',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-take-a-step-on-the-property-ladder-in-edinburgh',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-delighted-with-convenient-location-of-our-arborfield-development',
        'https://www.taylorwimpey.co.uk/customer-stories/family-fall-in-love-with-the-four-bedroom-huxford',
        'https://www.taylorwimpey.co.uk/customer-stories/new-home-feels-like-fate-for-irchester-couple-now-settled-in-overstone',
        'https://www.taylorwimpey.co.uk/customer-stories/julie-finds-dream-home-at-the-orangery',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-finds-their-dream-home-in-south-newsham',
        'https://www.taylorwimpey.co.uk/customer-stories/family-upsize-with-spacious-home-at-our-uttoxeter-development',
        'https://www.taylorwimpey.co.uk/customer-stories/new-home-feels-like-fate-for-irchester-couple-now-settled-in-overstone',
        'https://www.taylorwimpey.co.uk/customer-stories/retired-couple-find-it-is-easy-to-downsize-to-west-craigs-edinburgh',
        'https://www.taylorwimpey.co.uk/customer-stories/couple-thrilled-with-multi-purpose-home-at-our-peaceful-wokingham-development',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-thrilled-with-binfield-location',
        'https://www.taylorwimpey.co.uk/customer-stories/alleviate-the-stress-of-selling-a-home-with-part-exchange-and-easymover',
        'https://www.taylorwimpey.co.uk/customer-stories/double-celebration-for-customers-at-our-church-view-development',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-take-a-step-on-the-property-ladder-in-east-calder',
        'https://www.taylorwimpey.co.uk/customer-stories/upsizer-finds-dream-family-home-at-east-hollinsfield',
        'https://www.taylorwimpey.co.uk/customer-stories/buyers-take-a-step-up-the-property-ladder-in-inverkeithing',
        'https://www.taylorwimpey.co.uk/customer-stories/we-welcome-first-residents-to-lygon-green',
        'https://www.taylorwimpey.co.uk/customer-stories/a-new-home-offers-a-stress-free-move-on-the-property-ladder-for-first-time-buyers',
        'https://www.taylorwimpey.co.uk/customer-stories/young-family-get-more-living-space-by-choosing-to-call-calderwood-home',
        'https://www.taylorwimpey.co.uk/customer-stories/buyers-take-a-step-up-the-property-ladder-with-taylor-wimpey',
        'https://www.taylorwimpey.co.uk/customer-stories/family-fall-in-love-with-village-living-at-thornbury-green',
        'https://www.taylorwimpey.co.uk/customer-stories/family-find-dream-home-at-pine-trees',
        'https://www.taylorwimpey.co.uk/customer-stories/family-finds-dream-ipswich-home-during-pandemic',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-find-dream-home-just-in-time-to-welcome-first-baby',
        'https://www.taylorwimpey.co.uk/customer-stories/colchester-couple-make-stoneway-grange-their-home',
        'https://www.taylorwimpey.co.uk/customer-stories/exmouth-couple-create-their-dream-garden-at-buckingham-heights',
        'https://www.taylorwimpey.co.uk/customer-stories/first-time-buyers-who-step-on-the-ladder-get-more-by-reserving-early-in-inverkeithing',
        'https://www.taylorwimpey.co.uk/customer-stories/easy-step-on-the-ladder-for-first-time-buyers-in-inverkeithing'
    ]
}
,{
    'company':'Allen & Overy',
    'web_url':[
        'https://www.trustpilot.com/review/allenovery.com'
    ]
}
,{
    'company':'Bupa',
    'web_url':[
        'https://www.nivabupa.com/customer-testimonials.html',
        'https://www.bupa.co.uk/health/health-insurance/member-stories',
        'https://www.bupa.co.nz/residents-stories/'
    ]
}
,{
    'company':'Department for Education (DfE)',
    'web_url':[
        'https://committees.parliament.uk/work/6675/dfe-recall-send-review-schools-white-paper-and-the-national-tuition-programme/'
    ]
}
,{
    'company':'Nation Health Service(NHS)',
    'web_url':[
        'https://www.nationalhealthexecutive.com/nhe-testimonials'
    ]
}
,{
    'company':'Ministry of Defence (MoD)',
    'web_url':[
        'https://www.gov.uk/government/organisations/ministry-of-defence',
        'https://researchbriefings.files.parliament.uk/documents/CBP-7313/CBP-7313.pdf'
    ]
}
,{
    'company':'HM Revenue and Customs (HMRC)',
    'web_url':[
        'https://www2.fujitsu.com/global/customer-stories/cs-hmrc-20220610/',
        'https://www.gov.uk/government/organisations/hm-revenue-customs',
        'https://www.trustpilot.com/review/online.hmrc.gov.uk'
    ]
}
,{
    'company':'PricewaterhouseCoopers',
    'web_url':[
        'https://www.pwc.com/m1/en/about-us/client-stories.html',
        'https://www.g2.com/products/pricewaterhousecoopers-pwc/reviews',
        'https://www.yelp.com/brands/pricewaterhousecoopers-llp'
    ]
}
,{
    'company':'Deloitte',
    'web_url':[
        'https://www.featuredcustomers.com/vendor/deloitte-digital/testimonials',
        'https://www.deloitte.com/mt/en/careers/explore-your-fit/students/mt-why-malta-expats-testimonials.html',
        'https://theoxfordscience.org/pdf/Testimonials.pdf'
    ]
}
,{
    'company':'Ernst & Young',
    'web_url':[
        'https://www.ey.com/en_in/careers/people-stories',
        'https://www.ey.com/en_uk/careers/what-its-like-to-work-here/people-stories',
        'https://www.ey.com/en_gl/services/private-business/client-experience',
        'https://www.g2.com/products/ernst-young/reviews',
        'https://www.comparably.com/brands/ey'
    ]
}
,{
    'company':'KPMG',
    'web_url':[
        'https://kpmg.com/in/en/home/services/kpmg-client-stories.html',
        'https://kpmg.com/xx/en/home/insights/2021/10/esg-client-stories.html',
        'https://kpmg.com/us/en/how-we-work/client-stories/workday-client-stories.html',
        'https://kpmg.com/xx/en/home/insights/2021/10/esg-people-stories.html',
        'https://kpmglearningmalta.com/testimonials/'

    ]
}
,{
    'company':'Grant Thornton UK LLP',
    'web_url':[
        'https://careers.grantthornton.co.uk/life-at-grant-thornton/our-people-stories/',
        'https://www.trustpilot.com/review/www.grantthornton.co.uk',
        'https://trainees.grantthornton.co.uk/life-at-grant-thornton/our-people-stories/'
    ]
}
,{
    'company':'Accenture',
    'web_url':[
        'https://www.potentialproject.com/testimonials/accenture',
        'https://www.sap.com/assetdetail/2023/10/f028ae1a-907e-0010-bca6-c68f7e60039b.html',
        'https://www.congress.gov/118/meeting/house/116188/witnesses/HHRG-118-VR10-Wstate-MichlK-20230713.pdf'
    ]
}
,{
    'company':'McKinsey & Company',
    'web_url':[
        'https://www.trustpilot.com/review/mckinsey.com',
        'https://www.mckinsey.com/careers/tech/our-stories',
        'https://www.mckinsey.com/capabilities/operations/how-we-help-clients/operations-excellence-program/testimonials'
    ]
}
,{
    'company':'Met Office',
    'web_url':[
        'https://www.trustpilot.com/review/www.metoffice.gov.uk',
        'https://nz.trustpilot.com/review/www.metoffice.gov.uk?page=3'
    ]
}
,{
    'company':'DLA Piper',
    'web_url':[
        'https://www.bighand.com/en-gb/resources/case-studies/bhc-client-testimonials-dla-piper-x-rm/',
        'https://www.bighand.com/en-gb/resources/case-studies/womble-bond-dickinson-and-bighand-resource-management/',
        'https://www.bighand.com/en-gb/resources/case-studies/honigman-llp-resource-management/',
        'https://www.bighand.com/en-gb/resources/case-studies/stephenson-harwood-embracing-a-one-firm-approach-to-collaboration-with-bighand-resource-management/',
        'https://www.dlapiper.com/en/news/2024/02/dla-piper-lauded-in-world-trademark-review-1000-annual-list-of-top-trademark-professionals'
    ]
}
,{
    'company':'Home Office',
    'web_url':[
        'https://careers.homeoffice.gov.uk/our-stories',
        'https://smartmove2uk.com/uk-immigration-law-firm-in-mumbai/uk-visa-immigration-smartmove2uk-reviews/uk-visa-immigration-customer-testimonials-delhi/',
        'https://uk.trustpilot.com/review/www.ukvisaandimmigration.co.uk',
        'https://www.visasimple.com/testimonials',
        'https://uk.trustpilot.com/review/homedoq.shop'
    ]
}
,{
    'company':'Balfour Beatty',
    'web_url':[
        'https://www.trustpilot.com/review/balfourbeatty.com',
        'https://www.483.co.uk/about-us/testimonials/balfour-beatty-construction',
        'https://www.multivista.com/portfolio/balfour-beatty-video-testimonial/'
    ]
}
,{
    'company':'HC-One',
    'web_url':[
        'https://apply.hc-one.co.uk/working-for-hc-one/colleague-stories.aspx',
        'https://www.trustpilot.com/review/www.hc-one.co.uk',
        'https://www.hc-one.co.uk/',
        'https://www.carehome.co.uk/care_search_results.cfm/searchgroup/79334',
        'https://www.hc-one.co.uk/our-news/corporate-news/four-hc-one-care-homes-receive-the-perfect-ten-on'
    ]
}
,{
    'company':'Eversheds Sutherland',
    'web_url':[
        'https://www.bighand.com/en-us/resources/case-studies/bhc-client-testimonial-eversheds-sutherland-bighand-workflow-management/',
        'https://www.bighand.com/en-us/resources/case-studies/charles-russell-speechlys-and-bighand-workflow-management/',
        'https://www.bighand.com/en-us/resources/case-studies/bhc-client-testimonial-eversheds-sutherland-bighand-workflow-management/',
        'https://www.bighand.com/en-us/resources/case-studies/bhvc-restructure-support-team/',
        'https://www.bighand.com/en-us/resources/case-studies/bhvc-workflow-visibility/',
        'https://www.bighand.com/en-us/resources/case-studies/larkin-hoffman-automates-workflow-management-with-bighand/',
        'https://www.bighand.com/en-us/resources/case-studies/charles-russell-speechlys-and-bighand-workflow-management/',
        'https://www.eversheds-sutherland.com/en/global/capabilities/industries/energy',
        'https://www.trustpilot.com/review/www.eversheds-sutherland.co.uk',
        'https://www.eversheds-sutherland.com/en/asia/careers/careers-page/students-and-recent-graduates/eversheds-sutherland-hong-kong-student-award'
    ]
}
,{
    'company':'NHS',
    'web_url':[
        'https://www.england.nhs.uk/nhsbirthday/your-nhs-stories/staff/',
        'https://www.england.nhs.uk/nhsbirthday/your-nhs-stories/volunteers/',
        'https://www.england.nhs.uk/nhsbirthday/your-nhs-stories/nhs-retirement-fellowship/',
        'https://www.christie.nhs.uk/staff-testimonials'
    ]
}
,{
    'company':'Four Seasons Health Care',
    'web_url':[
        'https://www.trustpilot.com/review/www.fshc.co.uk',
        'https://www.carehome.co.uk/care_search_results.cfm/searchgroup/36153518FOUA',
        'https://www.fshcgroup.com/',
        'https://www.carehome.co.uk/care_search_results.cfm/searchgroup/36153518FOUA?utm_source=widgets&utm_medium=horizontal_widget&utm_campaign=Four%2520Seasons%2520Health%2520Care_35696&utm_content=read_all_link&rcsid=1003#reviews'
    ]
}
,{
    'company':'Virgin Care',
    'web_url':[
        'https://www.spirehealthcare.com/spire-yale-hospital/patient-information/testimonials/1/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/11/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-yale-hospital/patient-information/testimonials/4/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-yale-hospital/patient-information/testimonials/3/?consultant=&treatment=',
        'https://www.trustpilot.com/review/www.virgincare.co.uk',
        'https://drarockiavirginiaivf.com/testimonials/',
        'https://www.trustpilot.com/review/www.spirehealthcare.com',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/24/?consultant=&treatment=',
        'https://www.spirehealthcare.com/patient-information/testimonials/',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/4/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-fylde-coast-hospital/patient-information/testimonials/3/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/14/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/5/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-yale-hospital/patient-information/testimonials/2/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-fylde-coast-hospital/patient-information/testimonials/',
        'https://www.spirehealthcare.com/spire-fylde-coast-hospital/patient-information/testimonials/5/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/25/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-fylde-coast-hospital/patient-information/testimonials/4/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/21/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-fylde-coast-hospital/patient-information/testimonials/2/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/2/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/3/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/16/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/20/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/17/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/5/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/9/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/6/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/19/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/8/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/7/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/12/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/15/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/10/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/13/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/18/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/22/?consultant=&treatment=',
        'https://www.spirehealthcare.com/spire-harpenden-hospital/patient-information/testimonials/23/?consultant=&treatment='
    ]
}
,{
    'company':'Priory Group',
    'web_url':[
        'https://www.priorygroup.com/live-your-life/mental-health-stories',
        'https://www.priorygroup.com/live-your-life/addiction-stories',
        'https://www.priorygroup.com/live-your-life/eating-disorder-stories',
        'https://www.priorygroup.com/live-your-life/nhs-stories',
        'https://www.trustpilot.com/review/www.priorygroup.com',
        'https://www.topdoctors.co.uk/gh/priory-group/',
        'https://www.priorygroup.com/live-your-life/supported-living-stories',
        'https://www.priorygroup.com/live-your-life/residential-stories'
    ]
}
,{
    'company':'IBM UK',
    'web_url':[
        'https://uk.trustpilot.com/review/www.ibm.com',
        'https://endorsal.io/reviews/ibm',
        'https://www.ibm.com/blogs/think/uk-en/page/2/',
        'https://www.ibm.com/blogs/think/uk-en/',
        'https://www.ibm.com/blogs/think/uk-en/page/4/',
        'https://www.ibm.com/blogs/think/uk-en/page/3/',
        'https://www.ibm.com/blogs/think/uk-en/page/5/',
        'https://www.ibm.com/blogs/think/uk-en/page/6/',
        'https://www.ibm.com/blogs/think/uk-en/page/7/',
        'https://www.ibm.com/blogs/think/uk-en/page/8/',
        'https://www.ibm.com/blogs/think/uk-en/page/9/',
        'https://www.ibm.com/blogs/think/uk-en/page/10/',
        'https://www.ibm.com/blogs/think/uk-en/page/11/',
        'https://www.ibm.com/blogs/think/uk-en/page/12/',
        'https://www.ibm.com/blogs/think/uk-en/page/13/',
        'https://www.ibm.com/blogs/think/uk-en/page/14/',
        'https://www.ibm.com/blogs/think/uk-en/page/15/',
        'https://www.ibm.com/blogs/think/uk-en/page/16/',
        'https://www.ibm.com/blogs/think/uk-en/page/17/',
        'https://www.ibm.com/blogs/think/uk-en/page/18/',
        'https://www.ibm.com/blogs/think/uk-en/page/19/',
        'https://www.ibm.com/blogs/think/uk-en/page/20/',
        'https://www.ibm.com/blogs/think/uk-en/page/21/',
        'https://www.ibm.com/blogs/think/uk-en/page/22/',



    ]
}
,{
    'company':'Persimmon',
    'web_url':[
        'https://www.persimmonhomes.com/our-customers/customer-stories/finding-the-ideal-new-build-home-in-market-harborough',
        'https://www.persimmonhomes.com/our-customers/customer-stories/a-first-time-buyer-journey-with-exceptional-customer-service',
        'https://journalijecc.com/index.php/IJECC/article/view/3624',
        'https://www.persimmonhomes.com/our-customers/customer-stories/moving-from-london-to-the-welsh-coast-a-new-build-buying-journey'
        'https://www.persimmonhomes.com/our-customers/customer-stories/downsizing-to-a-home-by-the-seaside',
        'https://www.persimmonhomes.com/our-customers/customer-stories/buying-a-new-build-as-a-solo-buyer',
        'https://www.persimmonhomes.com/our-customers/customer-stories/a-perfect-part-exchange-solution-after-a-separation',
        'https://www.persimmonhomes.com/our-customers/customer-stories/family-life-in-a-persimmon-hadleigh',
        'https://www.persimmonhomes.com/our-customers/customer-stories/living-in-a-persimmon-alnwick-with-young-children',
        'https://www.persimmonhomes.com/our-customers/customer-stories/buying-a-second-home-with-persimmon',
        'https://www.persimmonhomes.com/our-customers/customer-stories/living-in-a-persimmon-chedworth',
        'https://www.persimmonhomes.com/our-customers/customer-stories/the-journey-to-a-new-family-home-in-rothwell-northamptonshire',
        'https://www.persimmonhomes.com/our-customers/customer-stories/a-first-time-buyer-journey-with-exceptional-customer-service'
    ]
}
,{
    'company':'Sage Group',
    'web_url':[
        'https://www.sage.com/en-us/success-stories/',
        'https://www.sage.com/en-gb/success-stories/',
        'https://www.adssglobal.net/company/testimonials/',
        'https://www.trustpilot.com/review/sage.com'
    ]
}
,{
    'company':'Mace Group',
    'web_url':[
        'https://www.macegroup.com/people/clients/paola-lettieri',
        'https://www.macegroup.com/people/clients/cath-shaw',
        'https://www.macegroup.com/people/clients/john-holland-kaye',
        'https://www.macegroup.com/people/clients/colin-naish',
        'https://www.macegroup.com/people/clients/george-kyriacou',
        'https://www.macegroup.com/people/clients/richard-hough'
        'https://www.macegroup.com/people/clients/gurjit-singh',
        'https://www.macegroup.com/people/clients/anuj-puri',
        'https://www.macegroup.com/people/clients/carlos-neuhaus',
        'https://www.macegroup.com/people/clients/gudmundur-runarsson'
    ]
}
,{
    'company':'Nuffield Health',
    'web_url':[
        'https://www.nuffieldhealth.com/article/patient-story',
        'https://www.nuffieldhealth.com/article/patient-story?&page=3&sortby=updated',
        'https://www.nuffieldhealth.com/article/patient-story?&page=2&sortby=updated',
        'https://www.trustpilot.com/review/www.nuffieldhealth.com?page=2'
        'https://uk.trustpilot.com/review/www.nuffieldhealth.com',
        'https://www.nuffieldhealth.com/about-us/our-impact/threads',
        'https://www.nuffieldhealth.com/physiotherapy/newcastle/nuffield-health-newcastle-hospital-physiotherapy-testimonials'
    ]
}

]


