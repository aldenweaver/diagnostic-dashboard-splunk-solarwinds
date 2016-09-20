import requests
import pico

baseurl = 'http://172.19.2.60:8089'
userName = 'api_user'
password = 'Vertafore1'

def splunkQuery():
    return_object = requests.get("{}{}".format(baseurl, '/services/apps/local'), auth=(userName, password))
    return return_object.text