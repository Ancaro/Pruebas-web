import urllib2

try:
	f=urllib2.urlopen("http://mejarando.la")
	print f.read()
	f.close()
except HTTPError, e:
	print "Jueputaaa"
	print e.code
except URLError, e:
	print "Jueputaaa"
	print e.code