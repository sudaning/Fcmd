#!/usr/bin/env python
# -*- coding: utf-8 -*- 

if __name__ == '__main__':

	from optparse import OptionParser
	usage = "usage: \n\tpython %prog [options]" + \
		"\nFor example: " + \
		"\n\tpython %prog -s 114.119.11.59 -u root -p root -n 18682099276"
	parser = OptionParser(usage=usage, version="%prog V1.0")
	parser.add_option('-s', '--host', dest='host', default='114.119.11.59',help="SSH IP. default:'%default'")
	parser.add_option('-u', '--user', dest='user', default='root', help="SSH port. default:'%default'")
	parser.add_option('-p', '--password', dest='password', default='root', help="SSH password. default:'%default'")
	
	parser.add_option('-l', '--lib', dest='lib', metavar="lib", default='lib', help='lib directory [default: %default]')
	
	#目前注册的profile是供鼎尖的sipphone使用的，默认的名字是sipp
	parser.add_option('-f', '--profile', dest='profile', default="sipp", help="profile. default:'%default'")
	parser.add_option('-n', '--num', dest='num', default='', help="number. default:'%default'")

	(options, args) = parser.parse_args()

	# 需要的库文件目录
	import os,sys
	run_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
	sys.path.append(os.path.join(run_path, options.lib))
	from base import color_str, ProcBar

	try:
		from pyssh import Ssh

		sys.stdout.write("logining server %s@%s ..." % (options.user, options.host))
		sys.stdout.flush()
		p = ProcBar().start()
		ssh = Ssh(options.host, username = options.user, password = options.password)
		p.stop()
		print(color_str("OK", "green"))

		sys.stdout.write("searching number %s ..." % color_str(options.num or "[all]" , "sky_blue"))
		p = ProcBar().start()
		stdin, stdout, stderr = ssh.exec_command('/usr/local/freeswitch/bin/fs_cli -x "sofia status profile %s reg %s"' % (options.profile, options.num))
		p.stop()
		print(color_str("OK", "green"))
		for l in stdout.readlines():
			sys.stdout.write(l)

	except Exception as err:
		if 'p' in locals().keys():
			p and p.stop()
		print(color_str(str(err), "red"))
		sys.exit(1)









