from urllib.parse import urlparse
result = urlparse('https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa')
print (result)
#ParseResult(scheme='https', netloc='duckduckgo.com', path='/', params='', query='q=python+stubbing&t=canonical&ia=qa', fragment='')

print (result.netloc)
#'duckduckgo.com'

print (result.geturl())
#'https://duckduckgo.com/?q=python+stubbing&t=canonical&ia=qa'

print (result.port)
#None


# Submitting a Web Form
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'q': 'Python'})
data
#'q=Python'

url = 'http://duckduckgo.com/html/'
full_url = url + '?' + data
response = urllib.request.urlopen(full_url)
with open('results.html', 'wb') as f:
    f.write(response.read())