<img width="50%" alt="responsiveness" src="djangorest.png">

# LIVE VIEW: https://django-rest-api-walkalong.herokuapp.com/

Documentation: https://www.django-rest-framework.org/


## API Project Setup with Django and Cloudinary

Steps:
1. Install Packages incl. Django, Cloudinary, Pillow
2. Create Project
3. Create env.py file and store Cloudinary url value
4. In settings.py, add cloudinary to installed apps and create storage


pip3 install 'django<4'

Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4

In the Terminal:

1. Install Django pip install ‘django<4’
2. Create Project django-admin startproject PROJ_NAME . (Don’t forget the ‘.‘)
3. Install Cloudinary Storage pip install django-cloudinary-storage==0.3.0
4. Install Pillow (Image Processing) pip install Pillow==8.2.0

In drf_api / settings.py:

5. Add Installed Apps INSTALLED_APPS = [
(...)
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
]
Note: Cloudinary storage must go before django.contrib.staticfiles, as shown.


In the IDE:

6. Create an env.py file within the top level directory Note: Ensure env.py is listed in the .gitignore file so it does not get pushed to GitHub.

In env.py: (Create file)

* Must first create a cloudinary account and create space for images.
7. import os import os
8. Set the URL value as a variable CLOUDINARY_URL
(URL value copied from Cloudinary Account Desktop) Make sure to only paste the correct part of the URL
os.environ['CLOUDINARY_URL'] = 'cloudinary://<cloudinary_key>'


In drf_api / settings.py:

8. Import os from pathlib import Path

import os

9. Add statement to import env.py if it exists - below import os

if os.path.exists('env.py'):

import env

10. Set CLOUDINARY_STORAGE variable equals to the CLOUDINARY_URL variable
- Place directly below imports
CLOUDINARY_STORAGE = {
'CLOUDINARY_URL':
os.environ.get('CLOUDINARY_URL')
}

11. Define Media Storage URL
- Place directly below MEDIA_URL = '/media/'

12. Define Default File Storage to
Cloudinary
- Place directly below
DEFAULT_FILE_STORAGE =
'cloudinary_storage.storage.MediaCloudinaryStorage
'


In the Terminal:

* Git add, commit and push


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

