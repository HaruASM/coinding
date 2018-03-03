"""
The flask application package.
"""


from flask import Flask
from TradingSystem import *


app = Flask(__name__)
trading= TradingSystem()

import HelloFlask.views
