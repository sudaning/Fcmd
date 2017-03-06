#Welcome to Freg
![](https://travis-ci.org/sudaning/Freg.svg?branch=master)
![](https://img.shields.io/pypi/v/pyFreg.svg)
![](https://img.shields.io/badge/python-3.5-green.svg)
![](https://img.shields.io/badge/python-2.7-green.svg)
![](https://img.shields.io/badge/docs-stable-brightgreen.svg?style=flat)
![](https://img.shields.io/github/stars/sudaning/Freg.svg)
![](https://img.shields.io/github/forks/sudaning/Freg.svg)

##Introduction

Freg is a pure Python library designed to show the information about what you specify user on [FREESWITCH](https://freeswitch.org/).
In [/scripts](https://github.com/sudaning/Freg/tree/master/scripts) , there are some scripts written by me for daily use.

##Installation
1. Via **pip**  
```pip install pyFreg```  
2. Via **easy_install**  
```easy_install pyFreg```  
3. From **source**(recommend)   
```python setup.py install```  

##upgrading
1. Via **pip**  
```pip install --upgrade pyFreg```

##Examples
```python
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

	#目前注册的profile默认的名字是sipp
	parser.add_option('-f', '--profile', dest='profile', default="sipp", help="profile. default:'%default'")
	parser.add_option('-n', '--num', dest='num', default='', help="number. default:'%default'")

	(options, args) = parser.parse_args() 

	reguser = RegUser(debug=True)
	reguser.login(host=options.host, user=options.user, password=options.password)
	reguser.run(profile=options.profile, number=options.num)
	reguser.show()
```

##From the author
**Welcome to use Freg (●'◡'●)ﾉ♥**  
If you find any bug, please report it to me by opening a issue.
Freg needs to be improved, your contribution will be welcomed.




