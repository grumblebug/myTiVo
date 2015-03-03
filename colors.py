#!/Python27/python

# Experimental
import os
import shutil
import cgi
import cgitb
cgitb.enable()

# Get the submitted form data
form = cgi.FieldStorage()
colorval = form.getvalue('colorlist')

# Set the source and destination files
sourcefile = "content/%s" % colorval
destinfile = "content/main.css"

#See if the files exist
# li = [sourcefile, destinfile]
#for checkfile in li:
#    try:
#        with open ('checkfile') as file:
#          pass
#        except IOError as e:
#            print "Content-type:text/html\r\n\r\n"
#            print "<html>"
#            print "<head>"
#            print "<title>Exception</title>"
#            print """<link rel="stylesheet" href="/main.css" type="text/css">"""
#            print "<body>"
#            print "<img src=stop.png><h3>Unable to find %s </3>" % checkfile
#            print "</body>"
#            print "</html>"

# Copy the new color scheme file to main.css
copyfile(sourcefile, destinfile)
k
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "</head>"
print """<body onload="goBack()" />"""
print "</body>"
print "</html>"