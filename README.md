ididit
======

Simple idonethis clone with Django + Angular.js, used internally in [StreetVoice](http://streetvoice.com/)

`ididit` uses `Heroku` + `Google Apps account` + `PostMark inboud email` you can deploy your own.

![Screenshot](https://raw.github.com/StreetVoice/ididit/master/docs/images/screenshot.png)


Prepare
------------

1. [Heroku](http://heroku.com) Account
1. Register a OAuth2 Client on [Google Developers Console](https://console.developers.google.com/project) to obtain key and secret
2. Add `Postmark` on Heroku 

```
$ heroku addons:add postmark
```

and create a mail server in postmark


Installation
-----------------




Settings
-----------------

Required `heroku config`

```
# django
SECRET_KEY

# email
DEFAULT_FROM_EMAIL
EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD

# ididit uses Google Apps account for login,and white list domain for restriction
GOOGLE_OAUTH2_CLIENT_ID
GOOGLE_OAUTH2_CLIENT_SECRET
GOOGLE_WHITE_LISTED_DOMAINS

# ididit uses Postmark for receving inboud email
POSTMARK_INBOUND_EMAIL
```


```
$ heroku config:add SECRET_KEY=<your secret key>
```

How to generate SECRET_KEY? you could try this.

```
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
get_random_string(50, chars)
```
