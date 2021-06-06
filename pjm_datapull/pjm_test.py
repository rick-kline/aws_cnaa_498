########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{xxxxxxxxxxx}',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.pjm.com')
    conn.request("GET", "/api/v1/act_sch_interchange/metadata?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except urllib.error as e:
    print(e.error)

####################################