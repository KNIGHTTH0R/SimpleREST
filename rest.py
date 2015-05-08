#!/usr/bin/env python

import web
import xml.etree.ElementTree as ET


tree = ET.parse('artists.xml')
root = tree.getroot()

urls = (
	"/artists", "list_artists",
	"/artists/(.*)" , "get_artist"
)

app = web.application(urls, globals())

class list_artists:
	def GET(self):
		output = 'artists:[';
		for child in root:
			print 'child', child.tag, child.attrib
			output += str(child.attrib) + ','
		output += ']';
		return output

		
class get_artist:
	def GET(self,artist):
		print "artist %d", artist
		for child in root:
			if child.attrib['id'] == artist:
				return str(child.attrib)
								
if __name__ == "__main__":
	app.run();