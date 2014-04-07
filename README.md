ididit
======

Simple idonethis clone with Django + Angular.js, used internally in [StreetVoice](http://streetvoice.com/)

![Screenshot](https://raw.github.com/StreetVoice/ididit/master/docs/images/screenshot.png)


Installation
-----------------


Settings
-----------------

Required `heroku config`

```
GOOGLE_OAUTH2_CLIENT_ID
GOOGLE_OAUTH2_CLIENT_SECRET
GOOGLE_WHITE_LISTED_DOMAINS


POSTMARK_INBOUND_EMAIL

DEFAULT_FROM_EMAIL

EMAIL_HOST
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
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
