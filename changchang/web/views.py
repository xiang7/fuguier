from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.shortcuts import redirect

#login_required: redirects to settings.LOGIN_URL if not logged in

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def work(request):
    return render(request, 'work.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def design_challenge(request):
	context = {
		'title': 'Daily Design Challenge',
		'subtitle': 'from uisdc.com | 2017',
		'featurecolor': '#ff6000',
		'primarycolor': '#fff',
		'categories': ['UI / UX', 'illustration'],
		'overviewlines': [
			'As a designer, the last thing I want to see is that I’ve lost passion in designing; or stopped being curious about new trends and techiniques.',
			'I was thirlled discovering  the daily design challenge held by uisdc.com. Designers from all over the world (US, UK, China, Norway...) would take the same design challenge, and then have a session looking at everyone’s approaches.',
			'Loved it!'
			],
		'demos': [
			{
				'title': 'Design A Font, AND Make It to A Logo (Plant Tech)',
				'images': [{'filename':'project-yizhi.png'}],
				},
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
				},
			{
				'title': 'Apply Colors to The Scene Created in #10',
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
				'images': [{'filename':'image/project-mobile-popup.png'}],
				},
			{
				'title': 'Do An Illustration!',
				'images': [{'filename':'project-illustration-group-photo.png'}],
				},
			]
		}	
	return render(request, 'project.html', context)

@login_required
def design_challenge_template(request):
	context = {
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
		'bannerimage': {'filename':'project-hackathon-banner.png', 'height':18},
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
		}	
	return render(request, 'project.html', context)

