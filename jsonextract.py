import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_980731.json"

print('Retrieving', url)
input = urllib.request.urlopen(url, context=ctx)
data = input.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

total = 0
for item in js["comments"]:
    result = item["count"]
    total = result + total
print(total)
