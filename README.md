# Disclaimer - The author will not take any responsibilty if you misuse it in any way. This code is only for educational purpose.

It steals facebook login cookies from firefox's cookie database[cookies.sqlite] and sends the cookie data back to the attacker.
After stealing the cookies it also removes the cookies from the DB so that the victim will not be able to end that particular
session and the attacker can continue to use it till the victim changes his password or ends all his session from the account settings tab.

This is not a full fledged malware code, It's just a demo to show how easily someone can hack into your account without even 
entering your login info.
You can code it in your own language of choice and make it more advanced and stealth.
Still, it's antivirus detection ratio is 0 or say it's FUD because it does not contain any virus signatures nor does
it perform any such malicious activity which the antivirus can find malicious.

The code is written in python and you can make changes and convert it into a single executable by using pyInstaller.
It sends the data back to the attacker using a PHP code hosted on a website.
It's a simple cookie logger php script which I have included here.
 
It's full description is here:  http://hackwhiz.com/2015/01/facebook-cookie-stealing-and-session-hijacking/

How to setup:

1.setup the cookie logger PHP script on your webhost.

2.change the url field in the malware code.

3.Execute the malware code.

Note: It only works if the user has selected remember me and is currently logged in into his FB account from firefox web browser. 
