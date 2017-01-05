#!/usr/bin/python3
types = ['deb']
websites = ['https://mirror.tuna.tsinghua.edu.cn/ubuntu/']
dists = ['xenial', 'xenial-updates', 'xenial-security']
repos = ['main', 'restricted', 'universe', 'multiverse']


for t in types:
	for w in websites:
		for d in dists:
			line = "{} {} {}".format(t,w,d)
			for r in repos:
				line += ' ' + r
			print(line)

