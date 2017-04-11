#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os,sys
from neko import color_str, ProcBar, Ssh

class FCmd:

	def __init__(self, debug=False):
		self.__ssh = None
		self.__debug = debug
		self.__out = None

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		if exc_tb:
			return False
		else:
			self.__del__()

	def __del__(self):
		self.__ssh = None

	def login(self, host='', port=22, user='root', password=''):
		self.__host = host
		self.__user = user
		self.__password = password

		try:
			p = ProcBar().start("logining server %s@%s:%d ..." % (user, host, port))
			self.__ssh = Ssh(host, port, username=user, password=password)
			p.stop(color_str("OK", "green"))
		except Exception as err:
			if 'p' in locals().keys():
				p and p.stop(color_str(str(err), "red"))
			raise Exception(str(err))
			return False

		return True

	def run(self, exe = '/usr/local/freeswitch/bin/fs_cli -x', cmd = ''):
		stdin, self.__out, stderr = self.__ssh.exec_command('%s "%s"' % (exe, cmd))

	def show(self):
		if self.__out:
			for l in self.__out.readlines():
				sys.stdout.write(l)
