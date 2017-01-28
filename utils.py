import platform
import os

import config

def check_requirements():
	return (platform.system() == 'Linux' and platform.python_version_tuple()[0] == '2')

def check_installation():
	for required_file in config.REQUIRED_FILES:
		if not os.path.exists(required_file):
			return False
	return True

def yes_no_question(prompt):
	ret = ''
	while not ret:
		ret = raw_input(prompt).lower()
		if ret != 'yes' and ret != 'no':
			ret = ''
	return ret
