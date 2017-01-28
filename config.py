__NAME__ = 'lnxb'
__VERSION__ = '0.1'
__FULLNAME__ = '%s-%s' % (__NAME__, __VERSION__)

REQUIRED_FILES = (
	'/etc/%s/' % __FULLNAME__,
	'/etc/%s/rules.conf' % __FULLNAME__,
)

DEFAULT_CONFIGURATION = (
	('settings', 0),
	('settings', 'SetBackupFolder', '/etc/%s/backups/' % __FULLNAME__),
	('settings', 'SetBackupTimeout', '60'),
	('settings', 'SetBackupDatetime', '00h00'),
	('settings', 'DataOverwriting', 'true'),
	('settings', 'DataCompression', 'false'),
	('settings', 'DataCompressionType', 'plain'),

	('backup_0', 0),
	('backup_0', 'BackupId', '0'),
	('backup_0', 'BackupPath', '/home/'),
	('backup_0', 'BackupType', 'folder'),
	('backup_0', 'Recursive', 'false'),
)

INITIALISATION_CONSTANTS = {
	'DEFAULT_CONFIGURATION': DEFAULT_CONFIGURATION,
	'INSTALLATION_LOG': '/etc/%s/install.log' % __FULLNAME__,
	'FOLDERS': ('/etc/%s/' % __FULLNAME__, '/etc/%s/backups/' % __FULLNAME__),
	'RULES': '/etc/%s/rules.conf' % __FULLNAME__,
}
