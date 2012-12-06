# Backward compatibility
from errbot.version import VERSION
from errbot.utils import version2array
if version2array(VERSION) >= [1,6,0]:
    from errbot import botcmd, BotPlugin
else:
    from errbot.botplugin import BotPlugin
    from errbot.jabberbot import botcmd

import urllib
from pyquery import PyQuery as pq

__author__ = 'xnaveira'

class InsultBot(BotPlugin):

    @botcmd
    def insult(self, mess, args):
        """ Insults someone for you
        Example: !insult my_enemy_name
        """
        if not args:
            return 'Am I supposed to insult myself?...'
        args = args.strip()
        d = pq(url='http://www.randominsults.net/')
        p = d("i")
        return str(args) + ', ' + p.html()

