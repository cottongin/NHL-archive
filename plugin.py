###
# Copyright (c) 2015, cottongin
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import requests
import json
import pickle
import urllib
from lxml import html
import string
from bs4 import BeautifulSoup
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('NHL')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x

class PrivFuncs:
    """Private functions"""

    def _parse_rows(self, rows):
        """ Get data from rows """
        results = []
        for row in rows:
            table_headers = row.find_all('th')
            if table_headers:
                results.append([headers.get_text() for headers in table_headers])

            table_data = row.findAll(True, {'class':['skedStartDateSite', 'teamName', 'skedStartTimeEST', 'tvInfo']})
            if table_data:
                results.append([data.get_text() for data in table_data])
            # #table_data_date = table_data_date.find('div', { 'class' : 'skedStartDateSite' })
            # if table_data_date:
            #     results.append([data.get_text() for data in table_data_date])
            # table_data_team = row.findAll('td', { 'class' : 'team' })
            # if table_data_team:
            #     results.append([data.get_text() for data in table_data_team])
            # table_data_time = row.findAll('td', { 'class' : 'time' })
            # if table_data_time:
            #     results.append([data.get_text() for data in table_data_time])
            # table_data_tvInfo = row.findAll('td', { 'class' : 'tvInfo' })
            # if table_data_tvInfo:
            #     results.append([data.get_text() for data in table_data_tvInfo])
        return results

class NHL(callbacks.Plugin):
    """Plugin to support various functions related to NHL."""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(NHL, self)
        self.__parent.__init__(irc)

    def next5(self, irc, msg, args, optteam):
        """<optional team>
        Gets next 5 games, for a specific team if passed.
        """

        url = 'http://www.nhl.com/ice/schedulebymonth.htm'
        try:
            sched = utils.web.getUrl(url).decode('utf8')
        except URLError as e:
            print 'An error occured fetching %s \n %s' % (url, e.reason)
        html = BeautifulSoup(sched, "lxml")

        try:
            table = html.find('table', { 'class' : 'data schedTbl'})
            rows = table.findAll('tr')
        except AttributeError as e:
            raise ValueError("No valid table found")

        # Get data
        parser = PrivFuncs()
        table_data = parser._parse_rows(rows)
        table_data = table_data[0]

        # # Print data
        # for i in table_data:
        #     print '\t'.join(i)
        irc.reply(table_data)

    next5 = wrap(next5, [optional('text')])

Class = NHL


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
