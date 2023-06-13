import numpy as np
import pylab as plt
import math
import itasca as it
from scipy.constants import inch

from load import blast, apply_gas_force, pressure


ct = 3e-4 # characteristic time
cp = 1e6  # characteristic pressure

material = "SS_ParallelBondedFINE-mat.p3sav"
hole_radius = 1.5*inch/2.0

c=104

pmult = 1.25
rmult = 2.0
rise_time = ct * rmult
peak_pressure = cp * pmult
pressure_decay_time = 5*ct
decay = -math.log(0.5)/pressure_decay_time

blast.setup(material, rise_time, peak_pressure,
            decay, hole_radius, c, "fine3")

blast.run(rise_time + 1.5e-3)

it.command("save basefine3{}_{}.p3sav".format(c,0))
blast.save()
