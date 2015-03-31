import hexchat
from urllib.request import urlopen
from urllib.error import URLError
import json
import re
import string
from time import sleep

__module_name__ = "doritoBot"
__module_version__ = "0.1"
__module_description__ = "IRC bot for #eldorito"

eldorito_server = "irc.gamesurge.net"
public_channel = "#eldorito"
private_channel = "#dorito-dev"

pub = hexchat.find_context(server=eldorito_server, channel=public_channel)
dev = hexchat.find_context(server=eldorito_server, channel=private_channel)

apiKey = 'AIzaSyAVcm67qjgMd3m9tvF_vvctD-k0Es8TwtA'
partOptions = 'snippet,contentDetails,statistics'

def nameFilter (word):
    ind1 = word.find(":")
    ind2 = word.find("!")
    return word[ind1+1:ind2]

def pubChathook (word, word_eol, attr):
    if word[2] == public_channel
        hexchat.EAT_NONE

def devChathook (word, word_eol, attr):
    if word[2] == private_channel
        hexchat.EAT_NONE

def pubJoinhook (word, word_eol, attr):
    if word[2] == public_channel
        list hexchat.get_list("users")
        nick_filtered = nameFilter(word[0])
        power = ''
        for x in list:
            if x.nick == nick_filtered
                power = x.prefix
        if power == '':
            pub.command("NOTICE "+format(nick_filtered)+":Welcome to #eldorito! Please read the topic for the latest announcements and rules!"
    hexchat.EAT_NONE

def devJoinhook (word, word_eol, attr):
    if word[2] == private_channel
        hexchat.EAT_NONE

hexchat.hook_server("PRIVMSG", pubChathook)
hexchat.hook_server("PRIVMSG", devChathook)
hexchat.hook_server("PRIVMSG", pubJoinhook)
hexchat.hook_server("PRIVMSG", devJoinhook)