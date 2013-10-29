TextTunes
=========

A simple Twilio/Soundcloud application to add songs to your soundcloud playlist via text.

How to Use
----------
By texting your Twilio phone number, it will search SoundCloud for a song matching the query and add the first match to your playlist.

Dependencies
------------

Python Modules
* flask
* twilio
* soundcloud

Also requires Python 2.6+. This particular version was coded with 2.6 in mind.

All of the required libraries can be installed by running `pip install <module>`.

In addition, you need a Twilio account with a valid phone number, and a SoundCloud account.

You'll need to set up your Twilio number to respond to SMS by sending a HTTP request to the "/" route of the Flask service.

Customization Notes
-------------------
This is designed to support a single Twilio and Soundcloud account. If you wish to adapt this to your own purposes, there are a few changes you'll need to do.

First, you will need a soundcloud.json file located in your home directory (unless you change the source) with the following members (all keys and values are strings):

* "client\_id" : your SoundCloud client ID
* "client\_secret" : your SoundCloud client secret
* "redirect\_uri" : your SoundCloud app redirect URI, though I never used it
* "username" : your SoundCloud username
* "password" : your SoundCloud password
* "playlist\_name" : the name of your SoundCloud playlist
* "twilio\_number" : your Twilio phone number

In python26hack.py (a hack I made to get around the SoundCloud module's dependency on collection.Counter), there is a reference to a copy of the python26hack directory in this repository. Change this path to whatever you want, or leave it out if you plan on using a more recent version of Python.

In path\_fix.py (which includes user-pip-installed modules), I include my local Python modules. Either change the path's to point to yours, or omit if you have installed the packages system-wide.

Change .htaccess to suit your servers needs.

Demo
----
My service is hosted at [http://ocf.berkeley.edu/~jtcramer/texttunes/], and the SoundCloud playlist I'm using is at [http://www.soundcloud.com/spiicytunaroll/sets/texttunes/].
