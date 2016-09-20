import requests
import pico
from orionsdk import SwisClient

npm_server = '172.19.2.65'
username = 'admin'
password = ''

verify = False

def solarwindsQuery():
    if not verify:
        from requests.packages.urllib3.exceptions import InsecureRequestWarning

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    swis = SwisClient(npm_server, username, password)


    results = swis.query("SELECT TOP 5 NodeID, DisplayName FROM Orion.Nodes")

    return_string = "Query Test: " + results

    for row in results['results']:
        return_string.push("{NodeID:<5}: {DisplayName}".format(**row))

    return return_string