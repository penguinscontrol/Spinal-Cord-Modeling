# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from neuron import h
import numpy
from math import sin, cos

class Cell(object):
    """Generic cell template."""
    def __init__(self):
        self.x, self.y, self.z = 0, 0, 0
        self.synlist = [] #### NEW CONSTRUCT IN THIS WORKSHEET
        self.create_sections()
        self.build_topology()
        self.build_subsets()
        self.define_geometry()
        self.define_biophysics()
        self.create_synapses()
    #
    def create_sections(self):
        """Create the sections of the cell. Remember to do this
        in the form::
            h.Section(name='soma', cell=self)
        """
        raise NotImplementedError("create_sections() is not implemented.")
    #
    def build_topology(self):
        """Connect the sections of the cell to build a tree."""
        raise NotImplementedError("build_topology() is not implemented.")
    #
    def define_geometry(self):
        """Set the 3D geometry of the cell."""
        raise NotImplementedError("define_geometry() is not implemented.")
    #
    def define_biophysics(self):
        """Assign the membrane properties across the cell."""
        raise NotImplementedError("define_biophysics() is not implemented.")
    #
    def create_synapses(self):
        """Subclasses should create synapses (such as ExpSyn) at various
        segments and add them to self.synlist."""
        pass # Ignore if child does not implement.
    #
    def build_subsets(self):
        """Build subset lists. This defines 'all', but subclasses may
        want to define others. If overridden, call super() to include 'all'."""
        self.all = h.SectionList()
        self.all.wholetree(sec=self.soma)
    #
    def connect2target(self, target, thresh=10):
        """Make a new NetCon with this cell's membrane
        potential at the soma as the source (i.e. the spike detector)
        onto the target passed in (i.e. a synapse on a cell).
        Subclasses may override with other spike detectors."""
        nc = h.NetCon(self.soma(1)._ref_v, target, sec = self.soma)
        nc.threshold = thresh
        return nc
    #
    def is_art(self):
        """Flag to check if we are an integrate-and-fire artificial cell."""
        return 0
    #
    def set_position(self, x, y, z):
        """
        Set the base location in 3D and move all other
        parts of the cell relative to that location.
        """
        for sec in self.all:
            for i in range(int(h.n3d())):
                h.pt3dchange(i,
                        x - self.x + h.x3d(i),
                        y - self.y + h.y3d(i),
                        z - self.z + h.z3d(i),
                        h.diam3d(i))
        self.x, self.y, self.z = x, y, z
    #
    def rotateZ(self, theta):
        """Rotate the cell about the Z axis."""
        rot_m = numpy.array([[sin(theta), cos(theta)], [cos(theta), -sin(theta)]])
        for sec in self.all:
            for i in range(int(h.n3d())):
                xy = numpy.dot([h.x3d(i), h.y3d(i)], rot_m)
                h.pt3dchange(i, xy[0], xy[1], h.z3d(i), h.diam3d(i))