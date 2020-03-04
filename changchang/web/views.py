from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect
from django.template.response import TemplateResponse

#@login_required: redirects to settings.LOGIN_URL if not logged in

def index(request):
    context = {
        'thumbnails' : [{
            'title': 'Roku Themes',
            'subtitle': 'seasonal & sellable themes | 2017-2018',
            'image': 'thumbnail-roku-themes.jpg',
            'url': '/roku-themes',
            'filter': 'base-filter, ui-ux-filter, all-filter'
        }, {
            'title': 'Cinema 4D',
            'subtitle': 'from uisdc.com | 2019',
            'image': 'thumbnail-cinema-4d.jpg',
            'url': '/cinema-4d',
            'filter': 'base-filter, ui-ux-filter, all-filter'
        }, {
            'title': 'Personalized Activation',
            'subtitle': 'seasonal & sellable themes | 2017-2018',
            'image': 'thumbnail-personalized-activation.jpg',
            'url': '/personalized_activation',
            'filter': 'base-filter, ui-ux-filter, branding-filter, all-filter'
        }, {
            'title': 'Roku Guest Mode',
            'subtitle': 'advanced feature | 2018',
            'image': 'thumbnail-guest-mode.jpg',
            'url': '/guest-mode',
            'filter': 'base-filter, ui-ux-filter, branding-filter, all-filter'
        }, {
            'title': 'Visual Voice Search',
            'subtitle': 'Roku’s multi-modal search | 2017',
            'image': 'thumbnail-voice-search.jpg',
            'url': '/voice-search',
            'filter': 'base-filter, ui-ux-filter, branding-filter, all-filter'
        }, {
            'title': 'Daily Design Challenge',
            'subtitle': 'from uisdc.com | 2017',
            'image': 'thumbnail-design-challenge.jpg',
            'url': '/design-challenge',
            'filter': 'base-filter, ui-ux-filter, branding-filter, all-filter'
        }, {
            'title': 'PEToYOU',
            'subtitle': 'co-founded startup | 2014',
            'image': 'thumbnail-petoyou.jpg',
            'url': '/pet-to-you',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'Hackathon',
            'subtitle': 'of Roku Inc. | 2017',
            'image': 'thumbnail-hackathon.jpg',
            'url': '/hackathon',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'Roku Zones',
            'subtitle': 'content collections | 2019',
            'image': 'thumbnail-roku-zones.jpg',
            'url': '/roku-zones',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'hulu Redesign',
            'subtitle': 'design exercise | 2016',
            'image': 'thumbnail-hulu.jpg',
            'url': '/LeECO_Design_Challenge',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'Fine Art',
            'subtitle': 'hand drawings | since 2008',
            'image': 'thumbnail-fine-art.jpg',
            'url': '/fine_art',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'Skype Redesign',
            'subtitle': 'conceptual design | 2015',
            'image': 'thumbnail-skype.jpg',
            'url': '/skype',
            'filter': 'base-filter, all-filter'
        }, {
            'title': 'banmi.com',
            'subtitle': 'experience sharing (before airbnb) | 2015',
            'image': 'thumbnail-banmi.jpg',
            'url': '/chummy',
            'filter': 'all-filter'
        }, {
            'title': 'CATrait',
            'subtitle': 'cat’s fashion & beyond | since 2015',
            'image': 'thumbnail-catrait.jpg',
            'url': '/catrait',
            'color': '#a6988f',
            'filter': 'all-filter'
        }, {
            'title': 'Personal Branding',
            'subtitle': 'changchang liu | 2016',
            'image': 'thumbnail-personal-branding.jpg',
            'url': '/personal_branding',
            'color': '#fe339c',
            'filter': 'all-filter'
        }, {
            'title': 'Package Design',
            'subtitle': 'tea, candy etc. | since 2008',
            'image': 'thumbnail-package.jpg',
            'url': '/package',
            'color': '#7c8a7d',
            'filter': 'all-filter'
        }, {
            'title': 'Wabash Visualization',
            'subtitle': 'from research to visualization | 2013',
            'image': 'thumbnail-wabash.jpg',
            'url': '/wabash',
            'hidden' : True,
            'filter': 'all-filter'
        }, {
            'title': 'Infographics',
            'subtitle': 'data visualization | since 2012',
            'image': 'thumbnail-infographics.jpg',
            'url': '/infographics',
            'filter': 'all-filter'
        }, {
            'title': 'Landscape Architecture',
            'subtitle': 'concept to construction | since 2008',
            'image': 'thumbnail-landscape.jpg',
            'url': '/landscape',
            'filter': 'all-filter'
        }, {
            'title': 'LeanTaaS Redesign',
            'subtitle': 'website re-skin | 2016',
            'image': 'thumbnail-leantaas.jpg',
            'url': '/leantaas',
            'filter': 'all-filter'
        }]
    }
    return render(request, 'index.html', context)

def design_challenge(request):
    demos = [
			{
				'title': 'Create an Illustration, AND Design It Into A Weather App',
				'images': [{'filename':'project-weather-app.png'}],
				},
			{
				'title': 'Create 2 Illustrations, AND Design Them Into App Intro and Banner',
				'images': [{'filename':'project-nextdoor.png'}],
				},
			{
				'title': 'Create Graph Line in Ai, AND Design It Into an App Interface',
				'images': [{'filename':'project-finance-app.png'}],
				},
			{
				'title': 'Create 3D Objects in Ai, AND Design It Into an App Interface',
				'images': [{'filename':'project-gift-card-app-redesign.png'}],
				},
			{
				'title': 'Show the Process of Designing a Figure Using MBE Style',
				'images': [{'filename':'project-capricorn-illustration.png'}, {'filename':'project-capricorn-sketch.png'}],
				},
			{
				'title': 'Design a Pixel Figure in Ps AND Make It Into a GIF',
				'images': [{'filename':'project-pixel-graphic-corgi.gif'}],
				},
			{
				'title': 'Design a Set of Objects Using the Same Style',
				'images': [{'filename':'project-bag-icons.png'}],
				},
			{
				'title': 'Design a Set of Objects Using the Same Style V2',
				'images': [{'filename':'project-icon-style-explorations.png'}],
				},
			{
				'title': 'Design a Set of Objects AND Make Them Into a Scene',
				'images': [{'filename':'project-combo-mono.png'}],
				}]
    lastIndex = len(demos)
    demos.extend(
        [{
            'title': 'Apply Colors to The Scene Created in #' + str(lastIndex),
            'images': [{'filename':'project-combo-color.png'}],
            },
        {
            'title': 'Draw An Axe, Pay Attention to Textures Different Mateials',
            'images': [{'filename':'project-indian-axe-rendering.png'}],
            },
        {
            'title': 'Design A Set of Icons for Mobile Interface',
            'images': [{'filename':'project-mobile-icon.gif'},{'filename':'project-mobile-icon-camera.png'},{'filename':'project-mobile-icon-settings.png'},{'filename':'project-mobile-icon-contacts.png'},{'filename':'project-mobile-icon-email.png'}],
            },
        {
            'title': 'Based on #13, Design An Unconventional Unlocking Experience',
            'images': [{'filename':'project-mobile-unlocking.png'}],
            },
        {
            'title': 'Pick an App, AND Redesign its Popup Dialog',
            'images': [{'filename':'project-mobile-popup.png'}],
            },
        {
            'title': 'Do An Illustration!',
            'images': [{'filename':'project-illustration-group-photo.png'}],
            }
        ])
    context = {
        'contents': [{
		'title': 'Daily Design Challenge',
		'subtitle': 'from uisdc.com | 2017',
		'featurecolor': '#ff6000',
		'primarycolor': '#fff',
		'categories': ['UI / UX', 'illustration'],
		'overviewlines': [
			'As a designer, the last thing I want to see is that I’ve lost passion in designing; or stopped being curious about new trends and techiniques.',
			'I was thirlled discovering the daily design challenge held by uisdc.com. Designers from all over the world (US, UK, China, Norway...) would take the same design challenge, and then have a session looking at everyone’s approaches.',
			'Loved it!'
			],
		'demos': demos,
        }]}
    return render(request, 'project.html', context)

def hackathon(request):
	context = {
        'contents': [{
		'title': 'Hackathon',
		'subtitle': 'of Roku Inc. | 2017',
		'titlebackgroundimage' : 'linear-gradient(to top, #f38a93, #fa5c75);',
		'featurecolor': '#f95c75',
		'primarycolor': '#fff',
		'categories': ['UI / UX', 'illustration'],
		'overviewlines': [
            'It’s never easy to hack something in 24 hours— but we (3 Roku web engineers + me) made it! Moreover, we didn’t just “hack”-ed it, we walked out with dark circles AND a real working game. Remember, we four only have 24 hours :)'
			],
		'bannerimage': {'filename':'project-hackathon-banner.png', 'height':25},
		'demos': [
			{
				'title': 'Roku Hackathon Presentation',
				'images': [{'filename': 'roku_hackathon_presentation.jpg'}]
				},
			{
				'title': 'Problems & Opportunities',
				'descriptions': ['- Roku users mainly use Roku devices for streaming purposes; while Roku actually has more to offer',
                                 '- In 2016, games have generated $100B; and 37% is from mobile',
                                 '- By 2019, the percentage is projected to be 50%',
                                 '- In home parties, not all guests can get involved in the same game due to limited number of controllers',
                                 '- Web games could be projected to TVs; and mobile devices could serve as game controllers'],
				'images': [{'filename': 'roku_hackathon_problem_2016.png'}]
				},
            {
                'title': 'How It Works',
                'descriptions': ['1. Users launch the channel on Roku',
                                 '2. Scan the QR code there to pick characters and customize names',
                                 '3. Pick a way to play: tapping on screen or using the motion senser in smart phones',
                                 '4. Objects on scene would worth different points based on their physical weight and structure',
                                 '5. The goal is to send out “angry cats” and “destroy” as many furnitures as possible…'],
                'images': [{'filename': 'roku_hackathon_wireframe.png',
                            'descriptions': ['Users have two ways to interact with their phone controller: A. using the slingshot on the screen; B. taking advantage of the motion sensor in phones.']}, 
                           {'filename': 'roku_hackathon_characters.png',
                            'descriptions': ['8 characters are available for users to pick from. For potential revenue chance, “big cats”, with stonger hittign power, are available for purchase.']},
                          {'filename':'roku_hackathon_character_animation.png',
                           'descriptions':['Characters are provided as sprits to engineers for animation.']},
                          {'filename':'roku_hackathon_screen_shot.gif',
                           'descriptions':['What do cats like to destroy? Furnitures!',
                                           'In this game, me as the designer created objects in difference shapes and sizes;',
                                           'the engineers defined the weights of them accordingly.',
                                           'When cats hit these objects, they would fall based on the weight.',
                                           'Hence cats would score based on the weight of the furnitures they’ve kocked down.',
                                           'Lastly, sorry! Innocent puppy.']}],
                },
            {
                'title': 'Outcome',
                'descriptions': ['1. We’ve succesfully identified other cat people in Roku',
                                 '2. We made T shirts and stickers out of the characters',
                                 '3. We continued working on it, hoping to bring the game to a new level'],
                'images': [{'filename': 'roku_hackathon_outcome_1.jpg'},
                           {'filename': 'roku_hackathon_outcome_2.jpg'},
                           {'filename': 'roku_hackathon_outcome_3.jpg',
                            'descriptions': ['We found game artists via a member’s connection.',
                                             'We’ve been working with them to the game REAL.']}]
                }
			]
		}]}
	return render(request, 'project.html', context)

def cinema_4d(request):
	context = {
        'contents': [{
		'title': 'Cinema 4D',
		'subtitle': 'from uisdc.com | 2019',
		'titlebackgroundimagewithcolor' : {'image':'cinema-4d-title.svg', 'color':'linear-gradient(to right, #221275, #3a157e)'},
		'featurecolor': '#31147b',
		'primarycolor': '#fff',
		'categories': ['illustration'],
		'overviewlines': ['With my happy experience with uisdc in the past, I did’t give it a second thought when knowing they have an online course for Cinema 4D. I finished the course (and homework) when I was on maternity leave…',
                          'So inevitably lots of them have some elements related to my son <3 <3 <3'],
		'demos': [
			{
				'title': 'Design 1+ Houses and Build the 3D Model',
				'images': [{'filename': 'cinema-4d-3d-model.jpg'}]
				},
			{
				'title': 'Design 3D Letters Using Small Components',
				'images': [{'filename': 'cinema-4d-pao.jpg'}]
				},
            {
				'title': 'Use Cinema 4D to Build Balloons and Draw an Illustration out of It',
				'images': [{'filename': 'cinema-4d-paopao.jpg'}]
				},
            {
				'title': 'Design and Build a Character',
				'images': [{'filename': 'cinema-4d-model-sheep.jpg'}]
				},
            {
				'title': 'Design a Package and Render It out',
				'images': [{'filename': 'cinema-4d-maomao.jpg'}]
				},
            {
				'title': 'Design and Build a Room',
				'images': [{'filename': 'cinema-4d-build-room.jpg'}]
				},
			]
		}]}
	return render(request, 'project.html', context)

def roku_themes(request):
	context = {
        'contents': [{
		'title': 'Roku Themes',
		'subtitle': 'seasonal and sellable themes | 2017-2018',
		'titlebackgroundimage' : 'linear-gradient(to top, #08a4df, #8e5cfa);',
		'featurecolor': '#3881d6',
		'primarycolor': '#fff',
        'separatorimage': 'linear-gradient(to right, #734cc8, #0da6e0);',
		'categories': ['UI', 'illustration', 'dev package'],
		'overviewlines': ['Roku has verious types of themes— brand themes, network themes, seasonal themes, sellable themes, and partner themes. I’ve created 8 theme packages end-to-end.'],
		'bannerimage': {'filename':'roku_themes_title_banner.png', 'height':18},
		'demos': [
			{
				'title': '2018 Winter Theme',
				'descriptions': ['Every year, during holiday season, Roku will release a special winter theme to delight our users. It is the seasonal theme that will be on users’ devices for the longest period of time.'],
				'images': [
					{'filename': 'roku_themes_winter_rating.png'},
                    {'filename': 'roku-winter-theme.gif'},
                    {'prologues':['The overall style is generally following the 2018 Holiday Campaign Guideline'], 'filename': 'roku_themes_winter_guideline.png'},
                    {'prologues':['The theme is animated, with 3 scenes rotating'], 'filename': 'roku_themes_scenes.jpg'}
					]
				},
			{
				'title': '2018 New Year’s Eve Theme',
				'images': [
					{'filename': 'roku_themes_new_year_theme.png'},
                    {'filename': 'roku_themes_new_year_screens.jpg'}
					]
				},
            {
                'title': '2018 4th of July',
                'images': [
                    {'filename': 'roku_themes_new_year.png'},
                    {'filename': 'roku_themes_fourth_july_explorations.jpg', 'descriptions': ['explorations through the process']}
                    ]
                },
            {
				'title': '2017 New Year’s Eve Theme',
				'images': [
					{'filename': 'roku_themes_new_year_2017.png'},
                    {'filename': 'roku_themes_new_year_2017_screens.jpg'}
					]
				},
            {
				'title': 'My Personal Sellable Themes - Pet House',
				'images': [
					{'filename': 'roku_themes_pet_house_rating.png'},
                    {'filename': 'roku_themes_pet_house_theme.png'},
                    {'filename': 'roku_themes_pet_house_screens.jpg'}
					]
				},
            {
				'title': 'My Personal Sellable Themes - Panda Wonderland',
				'images': [
					{'filename': 'roku_themes_panda_ratings.png'},
                    {'filename': 'roku_themes_panda_theme.png'},
                    {'filename': 'roku_themes_panda_screens.jpg'}
					]
				},
            {
                'title': 'Valentine’s Day Theme',
                'descriptions': ['When think of Valentine’s Day, what usually comes to our minds are red color and hearts. It’s nice especially when you have someone to celebrate that day with. But when it comes to a theme that’s facing all the audiences, the designer needs to be more thoughtful. With such empathy in mind, I explored three directions. '],
                'images': [{'filename': 'roku_theme_valentine1.jpg'},
                          {'filename': 'roku_theme_valentine2.jpg'},
                          {'filename': 'roku_theme_valentine3.jpg'}]
                },
            {
				'title': 'Outcome',
                'descriptions': ['Other than the themes being shown above, I’ve also worked on Brand Themes— for example, RCA Roku TV Theme; and some other sellable themes like Jungle in the Dark…',
                                 'It’s hard to tie KPIs to themes to measure the value; but bringing the delightful moments to users is invaluable :)']
				},
			]
		}]}
	return render(request, 'project.html', context)

def guest_mode(request):
	context = {
        'contents': [{
		'title': 'Roku Guest Mode',
		'subtitle': 'flagship feature | 2018',
		'titlebackgroundimagewithcolor' : {'color': 'linear-gradient(to bottom, #280578, #a02f94, 91.5%, #fff 0);', 'image': 'guest_mode_title_background.png'},
		'featurecolor': '#671288',
		'primarycolor': '#fff',
		'categories': ['UI', 'illustration'],
		'overviewlines': [
			'As Roku’s one of flagship features in 2018, Guest Mode is targeting at opportunities in short-term rentals. In such case, multiple users would use the same device during different time frames. Making the switching process easier is what both owners and guests are looking for.', '',
            'And that’s why we were working on Guest Mode feature.',
			],
		'demos': [
			{
				'title': 'Problems & Opportunities',
				'descriptions': ['Imagining you’re an Airbnb owner and you’re providing a Roku device for guests use during their stay— the guests, as much as they appreciate it, they should not worry about earasing their credentials on the devices manually. Also, for the owers, setting up the device for guests everytime is not fun thing to do either.', '',
                                 'The past four years have seen the beginning of the short-term vacation rental boom. While Airbnb may the most prominent name in the business, it’s far from the only one. Expedia’s $3.9 billion takeover of Homeaway grabbed plenty of headlines back in November 2015, which had acquired VRBO in November of 2006.', '',
                                 'Airbnb’s growth is simply unprecedented. An inventory of around 3,000 lodgings in 2009 has surged to over 4 million listings worldwide in 2018.   The USA leads all countries accounting for 660,000 as of August 2017.  By contrast, it took the Hilton group nearly a century to grow to 690, 000 hotel rooms (across roughly 4200 hotels representing 11 different brands) across 93 countries.', '',
                                 'As of March 2017, Airbnb has had 150 MM unique guests and 3 million hosts worldwide in 65K cities.'],
				},
			{
				'title': 'Host Activate Guest Mode',
				'images': [
					{'filename': 'guest_mode_guest_activate.png'},
                    {'filename': 'guest-mode-host-activate-flow.png'}
					]
				},
            {
                'title': 'Guest Welcome/ Check In',
                'descriptions': ['Welcome the user to start streaming.',
                                 'Communicate: Roku Guest mode - branding and about benefits of Roku Channel, login information will be removed when user signs out. (Security)'],
                'images': [{'filename': 'guest-mode-guest-checkin.png'}]
                },
            {
                'title': 'Guest Mode Theme',
                'descriptions': ['Guest Mode theme is created specifically for short term rentals experience.',
                                 'Once the host has set the device (Roku TV/ streaming device) to Guest Mode, the Guest Mode theme would replace the previous theme.'],
                'images': [{'filename':'guest-mode-theme-1.jpg',
                           'descriptions': ['The scene remains the same: it\'s an interior home setting the friendly welcoming dog is the focal point-- carrying a key chain in its mouth.',
                                            'By doing so: we\'re delivering a welcoming message to users who\'re using the short term rental service']}, 
                           {'filename': 'guest-mode-theme-2.jpg',
                           'descriptions': ['Use luggages as main menu item of the theme design a set of backgrounds showcasing difference locations',
                                            'change the backgrounds every ## minutes (the system has the ability to do so)',
                                            'By doing so: hopefully users can relate the scenes to theirs such luggage element pictures the "short term rental" situation']},
                          {'prologues': ['Early Explorations'],
                          'filename': 'guest-mode-early-explorations.jpg'},
                          {'prologues': ['On-brand solutions'],
                          'filename': 'guest-mode-beach-scene.jpg'},
                          {'filename': 'guest-mode-beach-scene-search.jpg',
                          'descriptions': ['Scene1: beach']},
                          {'filename': 'guest-mode-cityscape-scene.jpg'},
                          {'filename': 'guest-mode-cityscape-scene-search.jpg',
                          'descriptions': ['Scene2: cityscape']},
                          {'filename': 'guest-mode-snow-scene.jpg'},
                          {'filename': 'guest-mode-snow-scene-search.jpg',
                          'descriptions': ['Scene3: snowy mountain']},
                           {'filename': 'guest-mode-checkin-calendar.jpg',
                           'descriptions': ['Check in calendar']},
                           {'filename': 'guest-mode-xml-1.jpg',
                           'descriptions': ['Code in xml that’s making the background scenes’ rotation possible']}
                          ]
                },
            {
                'title': 'Outcome',
                'descriptions': ['Due to some unexpected partner hurdles, the design shown above can’t be released as the very 1st version. Instead, we had to go to the safer route using existing default theme and use the name “Auto Sign Out Mode”.', '',
                                 'The ultimate goal, however, is still utilizing the design proposed above to showcase the delightful part of traveling/ vacation; and call the feature “Guest Mode”.', '',
                                 'Stay tuned.']}
			]
		}]}
	return render(request, 'project.html', context)

def roku_zones(request):
	context = {
        'contents': [{
		'title': 'Roku Zones',
		'subtitle': 'content collections | 2019',
		'titlebackgroundimagewithcolor' : {'color': 'linear-gradient(to top, #eb8af3, #8e5cfa);', 'image': 'roku-zones-title-background.jpg'},
		'featurecolor': '#b36ef0',
		'primarycolor': '#fff',
		'categories': ['UI/UX'],
		'overviewlines': ['“Unlike the typically text-based search results, zones are visual guides with thumbnail images, scrollable rows and content sourced from Roku’s partners” — Tech Crunch'],
        'separatorimage': 'linear-gradient(94deg, #8758ed, #eb8af3)',
		'demos': [
			{
				'title': 'Analysis',
				'images': [
					{
                        'prologues': ['Immediate Scenario of Artworks Being Used'],
						'filename': 'roku-zones-analysis-1.png',
						},
                    {
                        'prologues': ['Matrix of Strategy'],
                        'filename': 'roku-zones-analysis-2.png'
                        }
					]
				},
			{
				'title': 'Zone Types',
				'images': [
					{
                        'prologues': ['Programmatic Genres - Explorations of Tiles'],
						'filename': 'roku-zones-type-exploration.jpg'
						},
                    {
                        'prologues': ['Programmatic Genres - Tiles'],
						'filename': 'roku-zones-type.jpg',
                        'descriptions': ['The design pattern of genre tiles is overlaying customized font on top of scenes that are specific to each genre']
						},
                    {
                        'prologues': ['Example: Look-and-feel of a Genre Zone'],
                        'filename': 'roku-zones-example.jpg',
                        'descriptions': ['Zone asset has been referenced in an artical on engadget']
                        },
                    {
                        'prologues': ['Editorial Zones - Explorations of Tile Guidelines'],
                        'filename': 'roku-zones-editorial-exploration.jpg',
                        'descriptions': ['Reference of “existing” collection tiles at that time.']
                        },
                    {'filename': 'roku-zones-mild.jpg'},
                    {'filename': 'roku-zones-med.jpg'},
                    {'filename': 'roku-zones-wild.jpg'},
                    {
                        'prologues': ['Editorial Zones - Tiles'],
                        'filename': 'roku-zones-transformers.jpg',
                        },
                    {'filename': 'roku-zones-tiles-2.jpg'}
					]
				},
            {
                'title': 'Outcome',
                'images': [
                    {'filename': 'roku-zones-outcome.jpg'}
                ]
            }
			]
		}]}
	return render(request, 'project.html', context)

def voice_search(request):
    context = {
        'contents': [{
		'title': 'Visual Voice Search',
		'subtitle': 'Roku’s multimodal search | 2017',
		'titlebackgroundimagewithcolor' : {'color': 'radial-gradient(circle at 50% 0, #77737e, #221421)', 'image': 'voice-search-microphone.png'},
		'featurecolor': '#76727d',
		'primarycolor': '#fff',
		'categories': ['UI/UX', 'research'],
		'overviewlines': [
			'Visual voice search (VVS) is a UX and platform component designed to provide and display search-related information in a valuable way.', '',
            'Its goal is to provide and structure voice search-related results in a layout that users find easy to use, enjoyable, and effective in terms of search success and content discovery. VVS is also meant to make voice searches less destructive, more contextually aware, less frictionful, and less cryptic.'
			],
        'separatorimage': 'linear-gradient(94deg, #77737e, #221421)',
		'demos': [
			{
				'title': 'Benefits at Glance',
				'descriptions': ['<b>Non-Destructive:</b> visual voice search is an overlay; it does not kill the current application.', '',
                                 '<b>Uniform:</b> a common interface to all search experiences on Roku.', '',
                                 '<b>Integrated:</b> visual voice search can pull in content/results from the a back-end API.', '',
                                 '<b>Value for users:</b> offer current app-specific results.', '',
                                 '<b>Value for Partner apps:</b> opportunity to present result they feel is best to attract the users.', '',
                                 '<b>Value for Roku:</b> results are presented in such a way that Roku can add additional rows.', '',
                                 '<b>Flexibility:</b> visual presentation of search results can handle a mix of content imagery.', '',
                                 '<b>Engaging:</b> visual presentation creates a more modern and visually engaging experience.', '',
                                 '<b>Economy:</b> re-use existing Roku components to minimize engineering expenditure']
				},
			{
				'title': 'User Study',
				'images': [
					{
						'filename': 'voice-search-user-study.jpg',
						'descriptions': ['We have recruited 30 participants. Either not tech savvy, or do not have much knowledge about voice.',
                                         'For such guerrilla research, we used Survey Monkey to get potential participants’ info and filter from there.']
						},
                    {
                        'filename': 'voice-search-ab-comparison.jpg',
                        'descriptions': ['We had 3 A/B camparions.  Above shows how we ramdomize them.']
                        },
                    {
                        'filename': 'voice-search-script.jpg',
                        'descriptions': ['User study script 1']
                        },
                    {
                        'filename': 'voice-search-look-for-content.jpg',
                        'descriptions': ['Places in which participants look for content']
                        },
                    {
                        'filename': 'voice-search-script2.jpg',
                        'descriptions': ['User study script 2']
                        },
                    {
                        'filename': 'voice-search-usage-frequency.jpg',
                        'descriptions': ['How often do users use voice feature? (on non-Roku device) ']
                        },
                    {
                        'filename': 'voice-search-usage-frequency-roku-device.jpg',
                        'descriptions': ['How often do users use voice feature? (on Roku device) ']
                        },
                    {
                        'filename': 'voice-search-search-methods.jpg',
                        'descriptions': ['What method do participants prefer when searching? (on streaming device)']
                        },
                    {
                        'filename': 'voice-search-dislike-reason.jpg',
                        'descriptions': ['Why do participants dislike using voice feature?']
                        },
                    {
                        'filename': 'voice-search-script-3-1.jpg',
                        'descriptions': ['User study script 3.1']
                        },
                    {
                        'filename': 'voice-search-prototype-home-screen.jpg',
                        'descriptions': ['Prototype showing home screen']
                        },
                    {
                        'filename': 'voice-search-happy-path.jpg',
                        'descriptions': ['Happy path — get exactly what they want']
                        },
                    {
                        'filename': 'voice-search-easiness.jpg',
                        'descriptions': ['Easiness of starting using voice feature']
                        },
                    {
                        'filename': 'voice-search-behind-the-failures.jpg',
                        'descriptions': ['Behind the failures']
                        },
                    {
                        'filename': 'voice-search-command-format.jpg',
                        'descriptions': ['Format of voice command']
                        },
                    {
                        'filename': 'voice-search-script-3-2.jpg',
                        'descriptions': ['User study script 3.2']
                        },
                    {
                        'filename': 'voice-search-medium-path.jpg',
                        'descriptions': ['Medium path — search term is not specific enough']
                        },
                    {
                        'filename': 'voice-search-franchise-movie-command.jpg',
                        'descriptions': ['Franchise movie — format of voice commands']
                        },
                    {
                        'filename': 'voice-search-participants-assumption.jpg',
                        'descriptions': ['Participants’ assumption of the next step after clicking into a content tile']
                        },
                    {
                        'filename': 'voice-search-script-4.jpg',
                        'descriptions': ['User study script 4']
                        },
                    {
                        'filename': 'voice-search-unhappy-path.jpg',
                        'descriptions': ['Unhappy path — returning the wrong result with similar spellings']
                        },
                    {
                        'filename': 'voice-search-success-rate.jpg',
                        'descriptions': ['Success rate - fixed via editing via keyboard']
                        },
                    {
                        'filename': 'voice-search-failure-guesses.jpg',
                        'descriptions': ['Users’ guesses of why they failed']
                        }
					]
				},
            {
                'title': 'Outcome',
                'descriptions': ['The study has collected very useful and usable data and information; which will be used in future interations of the design.',
                                 'The era of voice has not officially come; but it’s just right around the corner :)']
                }
			]
		}]}
    return render(request, 'project.html', context)

def pet_to_you(request):
	context = {
        'contents':[{
		'title': 'PEToYOU',
		'subtitle': 'co-founded startup | 2014',
		'featurecolor': '#41d2cb',
		'primarycolor': '#fff',
		'categories': ['UI/UX', 'branding', 'illustration', 'infographics'],
        'overviewtitle': 'Overview - Pet\'s Diary & Social Platform',
		'overviewlines': [
            'Pet owners, love posting your pets’ photos on social media? Of course! But for those who are not crazy for pets, it could be annoying to see photos of pets all over the place.', '',
            'PEToYOU is the solution for it.', '',
            'It is a diary for pets, as well as a social platform with pets’ updates. Pet owners may make friends here too — with other pet owners.'
			],
		'bannerimage': {'filename':'pettoyou-title-background.png', 'height':30},
		'demos': [
			{
				'title': 'Problems & Opportunities',
				'descriptions': ['As pet lovers and pet owners, we keep encountering (or hearing our friend encountering) problems such as: lost pets, pet sitting, friends showing slight antipathy on posting pet photos, worrying about pets when at work…and so on.', '',
                                 'The world of pet products is a huge kingdom already, but such problems still exist — which shows the room for improvement.'],
				'images': [{'filename': 'petoyou-problem-statement.jpg'}]
				},
			{
				'title': 'Research',
				'descriptions': ['The goal of the product is to lessen pet owners’ burdens/ problems and concerns; as well as improve their/ their pets’ lives. Thus the research is focused on the pet owners only. For those who are pet lovers (but don’t have any)— they tend to have vary different answers than pet owners, which can impact the design path. Moreover, the possibility of them using/ purchasing pet products is very low.', '',
                                 'Regarding pet owners, they were investigated on structure; interest in pet’s app media and satisfaction on current pet products. Besides, open-ended questions were asked to find out their top needs.'],
				'images': [{'filename': 'petoyou-research.jpg'}]
				},
            {
                'title': 'Design Concept',
                'descriptions': ['With the pain points and researching findings kept in mind, 3 products are conceptualized to fulfill the goal.', '',
                                 'The APP, the collar and the wearable device — they each can solve certain amount of problems and together there are more possibilities and functions to benefit pets and pet owners. The map below is to show how they each could work collaboratively and the eco system they start to form.'],
                'images': [{'filename': 'petoyou-design-concept.jpg'}]
                },
            {
                'title': 'Development Phases',
                'descriptions': ['Due to the nature of the products and the way they are introduced to pet owners — they each would be released in difference phases.', '',
                                 'App with profile/ namecard/ diary function would be released first to attract potential users. This product/ phase is cost-free. When more users are attracted to PEToYOU, collars with QR code will be released to work along with the APP. While there’s the need for socializing, social platform in APP will be launched. At that point, PEToYOU would have some impact on existing users and raise interests from potential users. Wearable devices are developed to attach to collars and send tweets regarding to pets’ activities. As an impactful brand, it is the good timing to publish more collections for fashionable collars and bring out more powerful devices to track the locations of pets.', '',
                                 'In that sense, the APP, the collars and the wearable devices together they will form a healthy and steady eco system.'],
                'images': [{'filename': 'petoyou-development-phases.jpg'}]
                },
            {
                'title': 'Wireframes',
                'descriptions': ['According to the research and analysis, the wireframe is developed to ensure the flow is smooth and logical.'],
                'images': [{'filename': 'pettoyou-wireframe.jpg'}]
                },
            {
                'title': 'Prototype',
                'descriptions': ['Switch/ navigate pages through the photo model is an efficient and helpful way to think through and iterate the layout and look of interfaces.'],
                'images': [{'filename': 'pettoyou-prototype.jpg'}]
                },
            {
                'title': 'Outcome',
                'descriptions': ['A demo version of PEToYOU App is established to collect comments and feedbacks from beta users. Along with the clean, aesthetic and rationale pitch keynote, the PEToYOU Startup project was selected as one of the TOP 5 startup projects by SVACE.'],
                'images': [{'filename': 'petoyou-app-icon.jpg'}, 
                           {'filename': 'petoyou-app-copy.jpg', 'descriptions': ['Pets could have their own “social network”. The app can serve as pet’s diary; a platform to check other animals’ updates;'
                                                                                 'moreover, adding pet friends via QR codes on the collars or searching “pets nearby”.']},
                          {'filename': 'petoyou-final.jpg'}]
                },
			],
            'transitiontext': '<div class=\'uk-text-center\'><p>PEToYOU is not only about APP and technology.<br><b style=\'color:#7f131b\'>See the fashion side of PEToYOU.</b></p></div>'
		}, {
            'title': 'PETiTAG',
            'subtitle': 'co-founded startup | 2014',
            'featurecolor': '#7e151e',
            'primarycolor': '#fff',
            'categories': ['all design'],
            'bannerimage': {'filename':'pettoyou-petitag-banner.png', 'height':36, 'leadheight':12},
            'demos': [
                {
                    'title': 'Fashion for Pets',
                    'descriptions': ['A demo version of PEToYOU App is established to collect comments and feedbacks from beta users. Along with the clean, aesthetic and rationale pitch keynote, the PEToYOU Startup project was selected as one of the TOP 5 startup projects by SVACE.'],
                    'images': [{'filename': 'petoyou-holiday.jpg'}]
                    },
                {
                    'title': 'Gift for Pets',
                    'descriptions': ['Meet PETiTAG— like the first time you met your pet. PETiTAG is a line under PEToYOU that focuses on pet’s fashion. As a member of the family, our pets deserve such deluxe experience. There’s also a chic touch on wearable devices, including the packages they come with.'],
                    'images': [{'filename': 'petoyou-box-2.jpg'}, {'filename': 'petoyou-box-3.jpg'}, {'filename': 'petoyou-box-4.jpg'}]
                    },
                {
                    'title': 'Outcome',
                    'descriptions': ['Like all of the premium brands, PETiTAG is all about paying attention to details. Every small part of the product and package is thoughtfully well designed.'],
                    'images': [{'filename': 'petoyou-box.jpg'}, {'filename': 'petoyou-box-9.jpg'}]
                    },
                ]
            }]}
	return render(request, 'project.html', context)

def personalized_activation(request):
	context = {
        'contents': [{
            'title': 'Personalized Activation',
            'subtitle': 'personalize users’ activation experience | 2019',
            'titlebackgroundimage' : 'linear-gradient(to top, #662d91, #8e5cfa);',
            'featurecolor': '#662d91',
            'primarycolor': '#fff',
            'categories': ['UI/UX'],
            'overviewlines': [
                '“In the past, when you set up your Roku you possibly got a handful of Roku channel suggestions that you wanted to add. Roku has updated its set-up process to help you find a huge catalog of Roku channels based on your interests.”—— Cord Cutters News'
                ],
            'bannerimage': {'filename':'personalized_activation.png', 'height':10},
            'demos': [
                {
                    'title': 'Previous Flow',
                    'descriptions': ['In the previous flow, all users will go through the same steps with the same channels being pre-selected. Also it didn’t offer the opportunity to signup offers instantly.'],
                    'images': [{'filename': 'personalized_activation_previous_flow.png'}]
                    },
                {
                    'title': 'Opportunities for Improvements',
                    'descriptions': ['While previous design worked fine, there’s always room for improvements. Also with all the new features and products coming, the actvation flow needs to be tweaked to embrace all of them.'],
                    'images': [
                        {
                            'filename': 'personalized_activation_opporunities.png',
                            'descriptions': ['^ The goal of the step is simple—having users put in link code that’s on TV screen. The screen should not look any harder than it actually is.']
                            },
                        {
                            'filename': 'personalized_activation_opportunities2.png',
                            'descriptions': ['^ The order of the options should follow certain logic; either based on popularity or alphabet']
                            },
                        {
                            'filename': 'personalized_activation_opportunities3.png',
                            'descriptions': ['^ Though arranged by popularity, user groups vary when it comes to preferences. The low discoveribilty of less popular channels leads to a worse cycle for them.']
                            },
                        {
                            'filename': 'personalized_activation_opportunities4.png',
                            'descriptions': ['^ Neither the artwork nor the text has highlighted what’s special about the specific provider; it’s not very informational to users ']
                            },
                        {
                            'filename': 'personalized_activation_opportunities5.png',
                            }
                        ]
                    },
                {
                    'title': 'Personalized Activation Flow',
                    'descriptions': ['Every customer is different. A more customized experience is more likely leading to higher engament. Screenshots in production shown below.'],
                    'images': [
                        {
                            'filename': 'personalized_activation_flow.png',
                            'descriptions': ['^ The first few steps have inherited the elements in WIP web UI component library so that the whole experience is more on-brand; the next step is to improve the UX design.']
                            },
                        {
                            'filename': 'personalized_activation_flow2.png',
                            'descriptions': ['^ In the new design, we added up to 5 survey questions to get to know each individual better; and collect certain information that’ll be helpful in finding business opportunities. ']
                            },
                        {
                            'filename': 'personalized_activation_flow3.png',
                            'descriptions': ['^ With the help from Machine Learning and Data Analyst team, we’re recommending the channels and trial offers case-by-case; the goal is to help users find what they like sooner; hence channels they like are more likely to appear above fold on home screen; and eventually increase the streaming hours']
                            },
                        ]
                    },
                {
                    'title': 'Process and Outcome',
                    'descriptions': ['As simple as the current flow seems to be, almost every design decision through the process has been vetted by A/B test; and supported by solid data. The lessons and insights learned in this projects could be or even being applied in other areas.'],
                    'images': [
                        {'filename': 'personalized_activation_outcome.png'},
                        {'filename': 'personalized_activation_outcome2.png', 'descriptions': ['^ Guidelines being created for partners']},
                        {'filename': 'personalized_activation_outcome3.png'},
                        {'filename': 'personalized_activation_outcome4.png'}
                        ]
                    }
                ]
            }]}
	return render(request, 'project.html', context)

def design_challenge_template(request):
	context = {
        'contents': [{
            'title': 'title text',
            'subtitle': 'subtitle text',
            'titlebackgroundimage' : 'linear-gradient(to top, #f38a93, #fa5c75);',
            'featurecolor': '#ff6000',
            'primarycolor': '#fff',
            'categories': ['Category #1', 'Category #2'],
            'overviewlines': [
                'overview line #1',
                'overview line #2'
                ],
            'bannerimage': {'filename':'project-hackathon-banner.png', 'height':18, 'leadheight': 9},
            'demos': [
                {
                    'title': 'title #1',
                    'descriptions': ['description line 1', 'description line 2'],
                    'images': [
                        {
                            'filename': 'project-mobile-popup.png',
                            'descriptions': ['description line 1', 'description 2']
                            },
                        ]
                    },
                {
                    'title': 'title #2',
                    'descriptions': ['description line 1', 'description line 2'],
                    'images': [
                        {
                            'filename': 'project-nextdoor.png',
                            'descriptions': ['description line 1', 'description 2']
                            },
                        ]
                    },
                ]
            }]}
	return render(request, 'project.html', context)


### Old pages

def catrait(request):
    return render(request, 'old/catrait.html')

def LeECO_Design_Challenge(request):
    return render(request, 'old/LeECO_Design_Challenge.html')

def fine_art(request):
    return render(request, 'old/fine_art.html')

def landscape_temp112560123254(request):
    return render(request, 'old/landscape_temp112560123254.html')

def package(request):
    return render(request, 'old/package.html')

def skype(request):
    return render(request, 'old/skype.html')

def infographics(request):
    return render(request, 'old/infographics.html')

def leantaas_mock_up(request):
    return render(request, 'old/leantaas-mock-up.html')

def personal_branding(request):
    return render(request, 'old/personal_branding.html')

def wabash(request):
    return render(request, 'old/wabash.html')

def chummy(request):
    return render(request, 'old/chummy.html')

def landscape(request):
    return render(request, 'old/landscape.html')

def leantaas(request):
    return render(request, 'old/leantaas.html')

def product_design(request):
    return render(request, 'old/product_design.html')