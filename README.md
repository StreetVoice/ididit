ididit
======

Simple idonethis clone with Django + Angular.js, used internally in [StreetVoice](http://streetvoice.com/)

`ididit` uses `Heroku` + `Google Apps account` + `PostMark inboud email` you can deploy your own.

![Screenshot](https://raw.github.com/StreetVoice/ididit/master/docs/images/screenshot.png)


Prepare
----------

1. Get your [Heroku](http://heroku.com/) account
2. Register a OAuth2 Client on [Google Developers Console](https://console.developers.google.com/project) to obtain key and secret


Setup
------------

1. Clone `ididit` source code

> $ git clone https://github.com/StreetVoice/ididit.git


2. Create a `Heroku` app, and publish

> $ heroku create <your-app-name>
> $ git push heroku master

3. Add `Postmark` on Heroku

> $ heroku addons:add postmark

4. Setting up heroku config


```sh
$ heroku config:add SECRET_KEY=<your secret key> # random string

# google apps
$ heroku config:add GOOGLE_OAUTH2_CLIENT_ID=<your client id>
$ heroku config:add GOOGLE_OAUTH2_CLIENT_SECRET=<your client secret>

$ heroku config:add GOOGLE_WHITE_LISTED_DOMAINS=<restrct login google apps domain>
```

5. Setting up Postmark Sender Signature

> Go to [https://postmarkapp.com/signatures](https://postmarkapp.com/signatures)
