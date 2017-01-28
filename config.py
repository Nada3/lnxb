__NAME__ = 'lnxb'
__VERSION__ = '0.1'
__FULLNAME__ = '%s-%s' % (__NAME__, __VERSION__)

REQUIRED_FILES = (
	'/etc/%s/',
	'/etc/%s/rules.conf',
)

DEFAULT_CONFIGURATION = (
	('settings'),
	('settings', 'SetBackupFolder', '/etc/%s/backups/'),
	('settings', 'SetBackupTimeout', '60'),
	('settings', 'DataOverwriting', 'true'),
	('settings', 'DataCompression', 'false'),
	('settings', 'DataCompressionType', 'plain'),

	('backup_0'),
	('backup_0', 'BackupId', '0'),
	('backup_0', 'BackupPath', '/home/'),
	('backup_0', 'BackupType', 'folder'),
	('backup_0', 'Recursive', 'false'),
)

INITIALISATION_CONSTANTS = {
	'DEFAULT_CONFIGURATION': DEFAULT_CONFIGURATION,
	'INSTALLATION_LOG': '/etc/%s/install.log',
	'FOLDERS': ('/etc/%s/', '/etc/%s/backups/'),
	'RULES': '/etc/%s/rules.conf',
}
