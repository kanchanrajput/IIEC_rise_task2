#!/usr/bin/python3

import cgi
import subprocess

print("content-type:text/html")
print()

form = cgi.FieldStorage()
output_from_html = form.getvalue("x")


if "date" in output_from_html:
	cmd = "date"

elif "cal" in output_from_html:
	cmd = "cal"

elif ("editor" in output_from_html) or ("gedit" in output_from_html) or ("vim" in output_from_html):
	cmd = "gedit"
	if "vim" in output_from_html:
		cmd = "vim"

elif ("firefox" in output_from_html) or ("browser" in output_from_html):
	cmd = "firefox"
else :
	cmd = x

output = subprocess.getstatusoutput(cmd)
#print(output)

status = output[0]
out = output[1]
if status == 0:
	print(out)
else:
	print("some error occured")
	



	



	



