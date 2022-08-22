# About
 This is a six page dynamic portfolio website with python/django as backend.
 It was intended for a web, graphic designer and a content creator as well.
 Pages include home page, graphics portfolio page, contents page, content 
 view page and error pages for 404 and 500.


 # Features
 * 100% dynamic - Page contents are served directly from database.
 * Links to social media handles is dynamic and set from database.
 * Simple admin dashboard to save data to database.
 * Home page has sections for about, CV download, skills, services, team,
   portfolio, contents and testimonials.
 * Home page also have a contact form with email messaging capabilities.
 * Error 404 and 500 pages implemented to handle error pages.
 * Sitemap feature implemented to boost SEO.
 * Configured to use cloudinary cloud storage to serve media files.
 * Configured for heroku hosting.


 # Libraries/Packages
python 3.7
dj-database-url==0.5.0
Django==3.2.2
django-ckeditor==6.3.2
gunicorn==20.1.0
Pillow==9.2.0
django-cloudinary-storage==0.3.0
django-heroku==0.3.1
psycopg2==2.9.3
python-magic==0.4.25(online/live/hosted) / python-magic-bin==0.4.14(offline for windows os)
python-decouple==3.6
whitenoise==5.3.0


# Images
images for portfolio, teams should be of consistent size(width x height)
to avoid layout distort. default image dimension for portfolio is 440x500(WxL)
while for team is 320x300(WxL). Logo should be white if needed. Each content can 
only have one image.