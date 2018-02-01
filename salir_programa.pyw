#!/usr/bin/python34
# -*- coding: utf-8 -*-
"""
Este módulo tiene las instrucciones para salir del programa
"""
__author__ = "Alejandro Othoniel Gomez Chavez"
__copyright__ = "Copyright 2017 AOGCH"
__credits__ = "Mar Bran S.A. de C.V."

__licence__= "Open Code"
__version__ = "0.1"
__maintainer__ = "Alejandro Othoniel Gomez Chavez"
__email__ = "agomez@marbran.com.mx"
__status__ = "Developer"

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
class salir:
    def __init__(self):
        sys.exit(1)