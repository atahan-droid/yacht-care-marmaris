import urllib.request
try:
    # URL will redirect, we can catch the final url
    res = urllib.request.urlopen("https://maps.app.goo.gl/ZgwviNcpsyJQawpx8")
    print(res.geturl())
except Exception as e:
    print(e)
