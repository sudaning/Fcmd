#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from freg import RegUser

if __name__ == '__main__':

	from optparse import OptionParser
	usage = "usage: \n\tpython %prog [options]" + \
		"\nFor example: " + \
		"\n\tpython %prog -s 114.119.11.59 -u root -p root -n 18682099276"
	parser = OptionParser(usage=usage, version="%prog V1.0")
	parser.add_option('-s', '--host', dest='host', default='114.119.11.59',help="SSH IP. default:'%default'")
	parser.add_option('-u', '--user', dest='user', default='root', help="SSH port. default:'%default'")
	parser.add_option('-p', '--password', dest='password', default='root', help="SSH password. default:'%default'")

	#目前注册的profile是供鼎尖的sipphone使用的，默认的名字是sipp
	parser.add_option('-f', '--profile', dest='profile', default="sipp", help="profile. default:'%default'")
	parser.add_option('-n', '--num', dest='num', default='', help="number. default:'%default'")

	(options, args) = parser.parse_args() 

	reguser = RegUser(debug=True)
	reguser.login(host=options.host, user=options.user, password=options.password)
	reguser.run(profile=options.profile, number=options.num)
	reguser.show()