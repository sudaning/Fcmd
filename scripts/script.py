#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from fcmd import RegUser, Cmd

if __name__ == '__main__':

	from optparse import OptionParser
	usage = "usage: \n\tpython %prog [options]" + \
		"\nFor example: " + \
		"\n\tpython %prog -s 114.119.11.59 -u root -p root -n 18682099276"
	parser = OptionParser(usage=usage, version="%prog V1.0")
	parser.add_option('-s', '--host', dest='host', default='114.119.11.59',help="SSH IP. default:'%default'")
	parser.add_option('-u', '--user', dest='user', default='root', help="SSH port. default:'%default'")
	parser.add_option('--port', dest='port', default=2022, type='int', help="SSH port. default:'%default'")
	parser.add_option('-p', '--password', dest='password', default='root', help="SSH password. default:'%default'")

	parser.add_option('-f', '--profile', dest='profile', default="sipp", help="profile. default:'%default'")
	parser.add_option('-n', '--num', dest='num', default='', help="number. default:'%default'")
	parser.add_option('-c', '--cmd', dest='cmd', default='', help="command. default:'%default'")

	(options, args) = parser.parse_args()

	if options.cmd:
		with Cmd(debug=True) as c:
			c.login(host=options.host, port=options.port, user=options.user, password=options.password)
			c.run(cmd=options.cmd)
			c.show()
	else:
		with RegUser(debug=True) as reguser:
			reguser.login(host=options.host, port=options.port, user=options.user, password=options.password)
			reguser.run(profile=options.profile, number=options.num)
			reguser.show()