"""
Author: Pruthvi Kumar BK
Email: pruthvikumar.123@gmail.com
Date: June 18, 2018

This is the main file for Gunicorn. This file contains all the routes to respective scraper methods.

PS: chart_data_extractor must be marked as source directory for imports to be functional.
"""

import falcon
from falcon_cors import CORS
from middlewares.logCapture import PersistApiCalls
from route_handlers.handleDefaultRoute import HandleDefaultRoute
from route_handlers.conductExtraction import ConductExtraction

cors = CORS(allow_all_origins=['http:localhost:8000']) # Allow CORS for this endpoint.
app = falcon.API(middleware=[cors.middleware, PersistApiCalls()])

app.add_route('/', HandleDefaultRoute())
app.add_route('/v1/chartDataExtractor', ConductExtraction())
