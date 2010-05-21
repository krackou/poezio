#!/usr/bin/python
# -*- coding:utf-8 -*-
#
# Copyright 2010 Le Coz Florent <louizatakk@fedoraproject.org>
#
# This file is part of Poezio.
#
# Poezio is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# Poezio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Poezio.  If not, see <http://www.gnu.org/licenses/>.

from random import randrange
from config import config
from datetime import timedelta, datetime

class User(object):
    """
    keep trace of an user in a Room
    """
    def __init__(self, nick, affiliation, show, status, role):
        self.last_talked = None
        self.update(affiliation, show, status, role)
        self.change_nick(nick)
        self.color = randrange(2, 10)

    def update(self, affiliation, show, status, role):
        self.affiliation = affiliation
        self.show = show
        self.status = status
        self.role = role

    def change_nick(self, nick):
        self.nick = nick.encode('utf-8')

    def set_last_talked(self, time):
        """
        time: datetime object
        """
        self.last_talked = time

    def has_talked_since(self, t):
        """
        get a int
        Return True if the user talked since the last s seconds
        """
        from common import debug
        if self.last_talked is None:
            return False
        delta = timedelta(0, t)
        debug("Last talk: %s\nDelai:%s\nDelta:%s\n" % (str(self.last_talked), str(t), str(delta)))
        if datetime.now() - delta > self.last_talked:
            return False
        return True