import urllib.request
url = urllib.request.urlopen('https://www.google.com/')
print (url.geturl())
#'https://www.google.com/'

print (url.info())
#<http.client.HTTPMessage object at 0x7fddc2de04e0>

header = url.info()
print (header.as_string())
#('Date: Tue, 17 Jan 2017 11:23:58 GMT\n'
# 'Expires: -1\n'
# 'Cache-Control: private, max-age=0\n'
# 'Content-Type: text/html; charset=ISO-8859-1\n'
# 'P3P: CP="This is not a P3P policy! See '
# 'https://www.google.com/support/accounts/answer/151657?hl=en for more info."\n'
# 'Server: gws\n'
# 'X-XSS-Protection: 1; mode=block\n'
# 'X-Frame-Options: SAMEORIGIN\n'
# 'Set-Cookie: '
# 'NID=80=tYjmy0JY6flsSVj7DPSSZNOuqdvqKfKHDcHsPIGu3xFv41LvH_Jg6LrUsDgkPrtM2hmZ3j9V76pS4K_cBg7pdwueMQfr0DFzw33SwpGex5qzLkXUvUVPfe9g699Qz4cx9ipcbU3HKwrRYA; '
# 'expires=Sat, 24-Dec-2016 18:21:19 GMT; path=/; domain=.google.com; HttpOnly\n'
# 'Alternate-Protocol: 443:quic\n'
# 'Alt-Svc: quic=":443"; ma=2592000; v="34,33,32,31,30,29,28,27,26,25"\n'
# 'Accept-Ranges: none\n'
# 'Vary: Accept-Encoding\n'
# 'Connection: close\n'
# '\n')

print (url.getcode())
#200


# Downloading a File
import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
response = urllib.request.urlopen(url)
data = response.read()
with open('test.zip', 'wb') as fobj:
    fobj.write(data)

import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
tmp_file, header = urllib.request.urlretrieve(url)
with open('test.zip', 'wb') as fobj:
    with open(tmp_file, 'rb') as tmp:
        fobj.write(tmp.read())

import urllib.request
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
urllib.request.urlretrieve(url, '/home/mike/Desktop/blog.zip')
#('/home/mike/Desktop/blog.zip',
# <http.client.HTTPMessage object at 0x7fddc21c2470>)


# Specifying Your User Agent
import urllib.request
user_agent = ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'http://www.whatsmyua.com/'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(request) as response:
    with open('/home/mdriscoll/Desktop/user_agent.html', 'wb') as out:
        out.write(response.read())