import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open and read the web site file
url = "http://py4e-data.dr-chuck.net/comments_980728.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags (specific to this assignment)
spans = soup('span')

# Extract numbers from the span tags
spans_str = [span.text for span in spans]
# Make a new list with spans strings converted to integers
spans_int = [int(i) for i in spans_str]

print(sum(spans_int))
