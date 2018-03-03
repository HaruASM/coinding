"""
The flask application package.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))

from flask import Flask
import TradingSystem

app = Flask(__name__)
trading= TradingSystem.TradingSystem()

import HelloFlask.views
