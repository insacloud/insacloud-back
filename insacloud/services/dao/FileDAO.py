#!/usr/bin/env python
import sys
import urllib2
import os

sys.path.append("..")
import config
from config.import_config import config_FileDAO

def StorePoster(idEvent, urlPoster):
	# file to be written to
	path = config_FileDAO['posterStorageLocation']
	if not os.path.exists(path):
		os.makedirs(path)
		
	filename, file_extension = os.path.splitext(urlPoster)
		
	file = '%s/%s%s' % (path, idEvent, file_extension)
	
	response = urllib2.urlopen(urlPoster)

	#open the file for writing
	fh = open(file, "w")

	# read from request while writing to file
	fh.write(response.read())
	fh.close()
	
	print '-> stored poster as %s' % (file)
