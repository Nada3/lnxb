#!/bin/python
#-*-coding: utf-8-*-

import ConfigParser
import shutil
import sys
import os

import config
import utils

if not utils.check_requirements():
	print '[*] Your system does not satisfy our requirements, you need Python2.X and a Linux system to install lnxb'
	sys.exit(1)

if not utils.check_installation():
	install = utils.yes_no_question('[*] %s seems to not be installed on your system, install now (yes/no) ? ' % config.__NAME__)
	if install == 'no': sys.exit(1)

	if os.getuid() != 0:
		print '[*] %s need to be run as root to be installed' % config.__NAME__
		sys.exit(1)

	print '[*] Creating folders...'
	for folder in config.INITIALISATION_CONSTANTS['FOLDERS']:
		print '\t -%s' % (folder % config.__FULLNAME__)
		if os.path.exists(folder % config.__FULLNAME__):
			clean = utils.yes_no_question('[*] Some %s files seems to be already installed clean old installation and continue (yes/no) ?' % config.__NAME__)
			if clean == 'no': sys.exit(1)
			else: shutil.rmtree(folder % config.__FULLNAME__)
		os.mkdir(folder % config.__FULLNAME__)

	print '[*] Set default configuration... (%s)' % (config.INITIALISATION_CONSTANTS['RULES'] % config.__FULLNAME__)
	cfg = ConfigParser.RawConfigParser()
	for rule in config.INITIALISATION_CONSTANTS['DEFAULT_CONFIGURATION']:
		if len(rule) == 0: cfg.add_section(rule[0])
		else:
			print '[%s] %s = %s' % rule
			cfg.set(rule[0], rule[1], rule[2])
	
