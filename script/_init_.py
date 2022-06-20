# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 12:04:32 2022

@author: ASUS
"""

from fluidsim.solvers.ns2d.solver import Simul

params = Simul.create_default_params()
# Modify parameters as needed
sim = Simul(params)
sim.time_stepping.start()
