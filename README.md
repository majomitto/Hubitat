# Hubitat
Hubitat elevation related stuff

Quick and easy solution for users with running RPi (e.g. for OpenVPN purposes).
Tested on Rapsberian (RPi3 - python3) out of the box:

open terminal
create folder structure in home/pi: home/pi/scripts/cgi-bin
goto /home/pi/scripts/cgi-bin
create python script sendmail.py
$ sudo nano sendmail.py

Sender and receiver can be dynamic same like subject and body

set execution rights
$ sudo chmod +x sendmail.py

goto /home/pi/scripts/

run CGI HTTP sever (details on 20.20. CGIHTTPServer — CGI-capable HTTP request handler — Python 2.7.17rc1 documentation)
$ python -m CGIHTTPServer 8000

server MUST be started from /home/pi/scripts/ to be able find sendmail.py script

gmail setup:
I've created additional gmail account for this purpose xxxxhub@gmail.com
Allow less secure apps access for this account: https://myaccount.google.com/lesssecureapps?pli=1

Open browser on local network with this URL (use ip-address of RPi):
http://192.168.x.x:8000/cgi-bin/sendmail.py?subject=Hub+Warning&body=Motion+sensor+in+the+kitchen+has+been+activated
email should appear in receiver inbox.
You can check the log in terminal where server is running:


In Rule machine use HTTP GET request with upper URL link to send email according to trigger.
