import itasca as it
import itasca.ballarray as ba
from vec import vec
import numpy as np
import pylab as plt
import math

class cube_blast(object):
    def __init__(self):
        pass
    def setup(self, material, rise_time, peak_pressure,
                 pressure_decay, hole_radius,case,prefix):
        it.command("""
        new
        res {savefile}
        ball attr damp 0
        ball ini disp 0
        ball delete range cyl end1 0 0 -100 end2 0 0 100 rad {hole_radius}
        contact prop dp_nratio 0.1
        contact prop dp_sratio 0.1
        ball prop dp_nratio 0.1
        ball prop dp_sratio 0.1
        """.format(savefile=material,hole_radius=hole_radius))

        self.case = case
        self.prefix = prefix
        self.rise_time = rise_time
        self.peak_pressure = peak_pressure
        self.pressure_decay = pressure_decay
        self.rad = float(ba.radius().mean())
        self.barea = self.rad**2 * math.pi

        x,y,z = ba.pos().T
        annulus = np.sqrt(x**2 + y**2) < (hole_radius + 2*self.rad)
        ba.set_extra(1, 1.0*annulus)
        # list of ball objects which will carry load
        self.load_balls = [it.ball.find(i) for i in ba.ids()[np.nonzero(annulus)[0]]]
        # initiall bonds
        self.initial_bond_list = set(((c.end1().id(), c.end2().id()) for c in \
                                 it.contact.list("mechanical") if
                                      (c.model()=='linearpbond' and
                                       c.prop("pb_state")==3)))

        self.starting_time = it.mech_age()
        self.data = []
        it.set_callback("apply_gas_force",1)

    def run(self, deltat):
        it.command("solve age {}".format(it.mech_age() + deltat))

    def save(self):
        it.command("save {}blast{}.p3sav".format(self.prefix, self.case))
        np.savetxt("{}blast{}.txt".format(self.prefix, self.case), self.data)

    def show(self):
        t,p,c = np.array(self.data).T
        plt.subplot(211)
        plt.plot(t,p)
        plt.subplot(212)
        plt.plot(t,c)
        plt.show()

def pressure(time):
    "hole gas pressure as a function of time since explosion start."
    if time <= blast.rise_time:
        return blast.peak_pressure * time/blast.rise_time
    else:
        tstar = time - blast.rise_time
        return blast.peak_pressure * math.exp(-blast.pressure_decay * tstar)


def apply_gas_force(*args):
    dtime = it.mech_age() - blast.starting_time
    press = pressure(dtime)
    magnitude = press * blast.barea
    for ball in blast.load_balls:
        direction = (ball.pos()*vec((1,1,0))).norm()
        ball.set_force_app(direction * magnitude)

def broken_bonds():
    current_bonds = set(((c.end1().id(), c.end2().id()) for c in \
                         it.contact.list("mechanical") if
                            (c.model()=='linearpbond' and
                             c.prop("pb_state")==3)))
    return blast.initial_bond_list - current_bonds


def show_cracks():
    cracks = broken_bonds()
    output = open("tmp.geom", "w")
    print >> output, "ITASCA GEOMETRY3D"
    print >> output, "NODES ; id x y z EXTRA 1 value"
    for i, c in enumerate(cracks):
        b1,b2 = c
        pos = 0.5*(it.ball.find(b1).pos() + it.ball.find(b2).pos())
        print >> output, "{} {} {} {} EXTRA 1 0".format(i+1,*pos)
    output.close()
    it.command("geom delete")
    it.command("geom import tmp.geom format geometry")
    return len(cracks)

# singleton
blast = cube_blast()
