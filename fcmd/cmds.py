#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os,sys
from cmd import FCmd
from neko import color_str, ProcBar

class RegUser(FCmd):

	def run(self, profile='internal', number=''):
		p = ProcBar().start("searching number %s on profile %s ..." % (color_str(number or "[all]" , "sky_blue"), color_str(profile, "yellow")))
		try:
			FCmd.run(self, cmd="sofia status profile %s reg %s" % (profile, number))
		except Exception as err:
			p and p.stop(color_str(str(err), "red"))
			return False
		p.stop(color_str("OK", "green"))

