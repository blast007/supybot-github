###

"""
Add a description of the plugin (to be presented to the user inside the wizard)
here.  This should describe *what* the plugin does.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = ""

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author('kongr45gpen', 'alezakos', 'kongr45gpen@helit.org')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a url where the most recent plugin package can be downloaded.
__url__ = 'https://github.com/kongr45gpen/supybot-github'


import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!
import local.globals
import local.utility
import local.handler.GithubHandler as RequestHandler
import local.handler.PingHandler
import local.handler.PushHandler
import local.handler.WikiHandler
import local.handler.IssueHandler
import local.handler.StatusHandler
import local.handler.TravisHandler
import local.handler.MessageHandler
import local.handler.NetlifyHandler
import local.handler.ReleaseHandler
import local.handler.UnknownHandler
import local.handler.AppVeyorHandler
import local.handler.CreateDeleteHandler
import local.handler.IssueCommentHandler
import local.theme.Theme
import local.theme.DefaultTheme
import local.theme.CompactTheme
reload(local.globals)
reload(local.utility)
reload(RequestHandler)
reload(local.handler.PingHandler)
reload(local.handler.PushHandler)
reload(local.handler.WikiHandler)
reload(local.handler.IssueHandler)
reload(local.handler.StatusHandler)
reload(local.handler.TravisHandler)
reload(local.handler.MessageHandler)
reload(local.handler.NetlifyHandler)
reload(local.handler.ReleaseHandler)
reload(local.handler.UnknownHandler)
reload(local.handler.AppVeyorHandler)
reload(local.handler.CreateDeleteHandler)
reload(local.handler.IssueCommentHandler)
reload(local.theme.Theme)
reload(local.theme.DefaultTheme)
reload(local.theme.CompactTheme)

local.globals.init()

if world.testing:
    import test

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
