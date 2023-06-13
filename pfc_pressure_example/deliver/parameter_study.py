import numpy as np
import pylab as plt
import math
import itasca as it
from scipy.constants import inch

from load import blast, apply_gas_force, pressure

ct = 3e-4 # characteristic time
cp = 1e6  # characteristic pressure

material = "SS_ParallelBonded-mat.p3sav"

hole_radius = 1.5*inch/2.0

prefix = "a"
c=0
for pmult in [0.75, 1.0, 1.25, 1.5, 2.0]:
    for rmult in [0.1,0.5,1,2,10]:
        rise_time = ct * rmult
        peak_pressure = cp * pmult
        pressure_decay_time = 5*ct
        decay = -math.log(0.5)/pressure_decay_time

        blast.setup(material, rise_time, peak_pressure,
                    decay, hole_radius, c, prefix)
        run_time = rise_time + 1.5e-3
        print "running case {} for {}".format(c, run_time)
        blast.run(run_time)
        blast.save()
        c += 1
