#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os,sys
from neko import color_str, ProcBar, Ssh

class RegUser:

	def __init__(self, debug=False):
		self.__debug = debug

	def login(self, host='', user='root', password=''):
		self.__host = host
		self.__user = user
		self.__password = password
		self.__ssh = None

		try:
			if self.__debug:
				p = ProcBar().start("logining server %s@%s ..." % (user, host))
			self.__ssh = Ssh(host, username=user, password=password)
			if self.__debug:
				p.stop(color_str("OK", "green"))
		except Exception as err:
			if 'p' in locals().keys():
				p and p.stop(color_str(str(err), "red"))
			raise Exception(str(err))
			return False

		return True

	def run(self, profile='internal', number=''):
		if self.__debug:
			p = ProcBar().start("searching number %s on profile %s ..." % (color_str(number or "[all]" , "sky_blue"), color_str(profile, "yellow")))
		try:
			stdin, self.__out, stderr = self.__ssh.exec_command('/usr/local/freeswitch/bin/fs_cli -x "sofia status profile %s reg %s"' % (profile, number))
		except Exception as err:
			if 'p' in locals().keys():
				p and p.stop(color_str(str(err), "red"))
			return False
		if self.__debug:
			p.stop(color_str("OK", "green"))

	def show(self):
		for l in self.__out.readlines():
			sys.stdout.write(l)
