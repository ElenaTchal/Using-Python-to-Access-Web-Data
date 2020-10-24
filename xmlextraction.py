# There is something off somewhere between lines 16 and 20. It outputs the answer but prints for infinity or until program termination and I can't figure out why.

import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = "http://py4e-data.dr-chuck.net/comments_980730.xml"
    if len(address) < 1: break

    uh = urllib.request.urlopen(address, context=ctx)
    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    counts_strings = [count.text for count in counts]
    counts_integers = [int(i) for i in counts_strings]

print("Sum: ", sum(counts_integers))

