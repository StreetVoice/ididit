ididit
======

Simple idonethis clone with Django + Angular.js, used internally in [StreetVoice](http://streetvoice.com/)

`ididit` uses `Heroku` + `Google Apps account` + `PostMark inboud email` you can deploy your own.

![Screenshot](https://raw.github.com/StreetVoice/ididit/master/docs/images/screenshot.png)


Prepare
----------

1. Get your [Heroku](http://heroku.com/) account
2. Register a OAuth2 Client on [Google Developers Console](https://console.developers.google.com/project) to obtain key and secret


Setting up Application
--------------------

1. Clone `ididit` source code

  ```
  $ git clone https://github.com/StreetVoice/ididit.git
  ```


2. Create a `Heroku` app, and publish

  ```
  $ heroku create <your-app-name>
  $ git push heroku master
  ```

3. Add `Postmark` on Heroku

  ```
  $ heroku addons:add postmark
  ```

4. Setting up heroku config


  ```sh
  $ heroku config:add SECRET_KEY=<your secret key> # random string

  $ heroku config:add GOOGLE_OAUTH2_CLIENT_ID=<your client id>
  $ heroku config:add GOOGLE_OAUTH2_CLIENT_SECRET=<your client secret>

  # optional, but recommended
  $ heroku config:add GOOGLE_WHITE_LISTED_DOMAINS=<restrct login google apps domain>
  ```

5. Setting up Postmark Sender Signature

> Go to [https://postmarkapp.com/signatures](https://postmarkapp.com/signatures)

Setting up Postmark
---------------------

Open Postmark settings page
  
```
$ heroku addons:open postmark
```

1. Inbound Hook

  Go to `Server` > `Settings` and look at `Inbound Hook` and enter following URL

  ```
  http://<your-domain>/inbound/
  ```
  
2. Sender Signature

  Go to `Sender Signature` and confirm your sender email address.
  And your better setting up DKIM and SPF domain record that Postmark provided.


Development
==================

`ididit` uses Python, [Django](https://www.djangoproject.com/) for Backend REST API and [Angular.js](http://angularjs.org/) for frontend.


Settings up django
-------------------

Use `virtualenv` and `virtualenvwrapper` for development is recommended. If you are python developer, you should already install both of this. 

OK, Let's assume you are python developer, and both `virtualenv` and `virtualenvwrapper` are installed, you can just follow these steps to get started to development.

First of all, fork this repo.

```
$ mkproject ididit
$ git clone <your-ididit-git-repo>
$ pip install -r requirements.txt
$ ./manage.py runserver
```

You are good to go!
