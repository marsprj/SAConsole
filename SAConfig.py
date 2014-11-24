import ConfigParser
import logging

def GetValue(key):
	# config file name
	cn = 'sa.ini'
	value = ''
	try:
		cp = ConfigParser.ConfigParser()  
		cp.read(cn)
		value = cp.get('global', key, 0)
	except ConfigParser.NoSectionError, e:
		logging.error(e)
	except ConfigParser.NoOptionError, e:
		logging.error(e)

	return value

def SetValue(key, value):
	# config file name
	cn = 'sa.ini'
	rcp = ConfigParser.RawConfigParser()
	rcp.add_section('global')
	rcp.set('global', key, value)
	with open(cn, 'wb') as configfile:
		rcp.write(configfile)