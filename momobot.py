#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The main bot file
"""

import settings
from irc import irc
from bot import commands

def public_message(irc, data):
    print "Received a message:"
    print data

def just_joined(irc, data):
    irc.say('Hello, everyone!')

def someone_joined(irc, data):
    if data['username'] != settings.USERNAME:
        irc.say('Hello, %s!' % data['username'])

myirc = irc.IRC(settings.SERVER, settings.PORT, settings.USERNAME)

myirc.register_callback('channel_message', public_message)
myirc.register_callback('join', just_joined)
myirc.register_callback('channel_join', someone_joined)

myirc.join(settings.CHANNEL)

while True:
    myirc.read()
