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
		'categories': ['UI / UX', 'illustration'],
		'overviewlines': [
			'As a designer, the last thing I want to see is that I’ve lost passion in designing; or stopped being curious about new trends and techiniques.',
			'I was thirlled discovering  the daily design challenge held by uisdc.com. Designers from all over the world (US, UK, China, Norway...) would take the same design challenge, and then have a session looking at everyone’s approaches.',
			'Loved it!'
			],
		'demos': [
			{
				'title': 'Design A Font, AND Make It to A Logo (Plant Tech)',
				'images': ['image/project-yizhi.png'],
				},
			{
				'title': 'Create an Illustration, AND Design It Into A Weather App',
				'images': ['image/project-weather-app.png'],
				},
			{
				'title': 'Create 2 Illustrations, AND Design Them Into App Intro and Banner',
				'images': ['image/project-nextdoor.png'],
				},
			{
				'title': 'Create Graph Line in Ai, AND Design It Into an App Interface',
				'images': ['image/project-finance-app.png'],
				},
			{
				'title': 'Create 3D Objects in Ai, AND Design It Into an App Interface',
				'images': ['image/project-gift-card-app-redesign.png'],
				},
			{
				'title': 'Show the Process of Designing a Figure Using MBE Style',
				'images': ['image/project-capricorn-illustration.png', 'image/project-capricorn-sketch.png'],
				},
			{
				'title': 'Design a Pixel Figure in Ps AND Make It Into a GIF',
				'images': ['image/project-pixel-graphic-corgi.png'],
				},
			{
				'title': 'Design a Set of Objects Using the Same Style',
				'images': ['image/project-bag-icons.png'],
				},
			{
				'title': 'Design a Set of Objects Using the Same Style V2',
				'images': ['image/project-icon-style-explorations.png'],
				},
			{
				'title': 'Design a Set of Objects AND Make Them Into a Scene',
				'images': ['image/project-combo-mono.png'],
				},
			{
				'title': 'Apply Colors to The Scene Created in #10',
				'images': ['image/project-combo-color.png'],
				},
			{
				'title': 'Draw An Axe, Pay Attention to Textures Different Mateials',
				'images': ['image/project-indian-axe-rendering.png'],
				},
			{
				'title': 'Design A Set of Icons for Mobile Interface',
				'images': ['image/project-mobile-icon.png','image/project-mobile-icon-camera.png','image/project-mobile-icon-settings.png','image/project-mobile-icon-contacts.png','image/project-mobile-icon-email.png'],
				},
			{
				'title': 'Based on #13, Design An Unconventional Unlocking Experience',
				'images': ['image/project-mobile-unlocking.png'],
				},
			{
				'title': 'Pick an App, AND Redesign its Popup Dialog',
				'images': ['image/project-mobile-popup.png'],
				},
			{
				'title': 'Do An Illustration!',
				'images': ['image/project-illustration-group-photo.png'],
				},
			]
		}	
	return render(request, 'project.html', context)