import random
import string

import requests
import cherrypy
from orionsdk import SwisClient



class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="splunkQuery">
              <button type="submit">Splunk</button>
            </form>

            <form method="get" action="solarwindsQuery">
              <button type="submit">Solarwinds</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def splunkQuery(self):
        baseurl = 'http://172.19.2.60:8089'
        userName = 'api_user'
        password = 'Vertafore1'

        return_object = requests.get("{}{}".format(baseurl, '/services/apps/local'), auth=(userName, password))
        return return_object.text


    @cherrypy.expose
    def solarwindsQuery(self):
        npm_server = '172.19.2.65'
        username = 'admin'
        password = ''
        verify = False

        if not verify:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        swis = SwisClient(npm_server, username, password)
        results = swis.query("SELECT TOP 5 NodeID, DisplayName FROM Orion.Nodes")
        return_list = []

        for row in results['results']:
            return_list.append("{NodeID:<5}: {DisplayName}".format(**row))

        return ''.join(return_list)


if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())






































# import os, os.path
# import random
# import string
# import cherrypy
# import pico
# import pico.client
#
#
#
#
# class StringGenerator(object):
#     @cherrypy.expose
#     def index(self):
#         return """ <!DOCTYPE html>
#  <html>
#     <head>
#       <script src="https://cdnjs.cloudflare.com/ajax/libs/react/0.13.3/react.js"></script>
#       <script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
#       <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js"></script>
#
#         <script src="/pico/client.js"></script>
#     <script>
#         pico.client.load("splunk");
#         pico.client.load("solarwinds");
#     </script>
#
#     </head>
#     <body>
#
#
#       <div id="splunk_result"></div>
#       <script>
#         splunk.splunkQuery(function(response){
#             document.getElementById('splunk_result').innerHTML = response;
#         });
#       </script>
#       <script type="text/babel" src="static/js/SplunkResult.js"></script>
#
#       <div id="solarwinds_result"></div>
#       <script>
#         splunk.solarwindsQuery(function(response){
#             document.getElementById('solarwinds_result').innerHTML = response;
#         });
#       </script>
#       <script type="text/babel" src="static/js/SolarwindsResult.js"></script>
#     </body>
#  </html>"""
#
#     @cherrypy.expose
#     def generate(self, length=8):
#         some_string = ''.join(random.sample(string.hexdigits, int(length)))
#         cherrypy.session['mystring'] = some_string
#         return some_string
#
#     @cherrypy.expose
#     def display(self):
#         return cherrypy.session['mystring']
#
#
# if __name__ == '__main__':
#     conf = {
#         '/': {
#             'tools.sessions.on': True,
#             'tools.staticdir.root': os.path.abspath(os.getcwd())
#         },
#         '/static': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': './public'
#         }
#     }
#     cherrypy.quickstart(StringGenerator(), '/', conf)
#
#
#
#







# import cherrypy
#
# class Root(object):
#     @cherrypy.expose
#     def index(self):
#         return "Splunk & Solarwinds API Queries"
#
# if __name__ == '__main__':
#     conf = {
#         '/static': {
#             'tools.staticdir.on': True,
#             'tools.staticdir.dir': '/home/site/static',
#             'tools.staticdir.index': 'index.html'
#         }
#     }
#     # Warning: binds to all network interfaces
#     cherrypy.config.update({'server.socket_host': '0.0.0.0'})
#     cherrypy.quickstart(Root(), '/')