import LFPy
import numpy as np
from neuron import h
from mpi4py import MPI
from neuronpy.util import spiketrain
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection

class Network(object):
    '''prototype population class'''

    def __init__(self, POPULATION_SIZE,
                 cellParameters,
                 populationParameters,
                 synapseParameters,
                 ):
        '''
        class initialization

        POPULATION_SIZE :       int, number of cells
        cellParameters :        dict
        populationParameters :  dict
        synapseParameters :     dict

        '''
        #set one global seed, ensure all randomizations are set on RANK 0 in script!
        np.random.seed(12345)
        self._POPULATION_SIZE = POPULATION_SIZE
        self._synapseParameters = synapseParameters

        self.cellPositions = {}
        self.cellRotations = {}
        self.cellMorphologies = {}

        #MPI stuff we're using
        self.COMM = MPI.COMM_WORLD
        self.SIZE = self.COMM.Get_size()
        self.RANK = self.COMM.Get_rank()

        #sync threads
        self.COMM.Barrier()
    #
    def run(self):
        '''execute the proper simulation and collect simulation results'''
        #produce simulation results on each RANK
        self.results = self.distribute_cellsims()

        #collect all simulation results on RANK 0
        if self.RANK == 0:
            for i in range(1, self.SIZE):
                result = self.COMM.recv(source=MPI.ANY_SOURCE)      #receive from ANY rank
                self.results.update(result)                         #collect
        else:
            self.COMM.send(self.results, dest=0)                    #send to RANK 0
            self.results = None                                     #results only exist on RANK 0

        self.COMM.Barrier()  #sync MPI threads

        #collect all cell locations on RANK 0
        if self.RANK == 0:
            for i in range(1, self.SIZE):
                thesePositions = self.COMM.recv(source=MPI.ANY_SOURCE)      #receive from ANY rank
                for key, value in thesePositions.iteritems():
                    self.cellPositions[key].append(value)

        else:
            self.COMM.send(self.cellPositions, dest=0)                    #send to RANK 0
            self.cellPositions = None                                     #results only exist on RANK 0
        #print("Just ended Run!")
        self.COMM.Barrier()  #sync MPI threads
    #
    def distribute_cellsims(self):
        '''Will distribute and run cell simulations across ranks'''
        #start unique cell simulation on every RANK,
        #and store the cell objects in dicts indexed by cellindex
        results = {}
        for cellindex in range(self._POPULATION_SIZE):
            if divmod(cellindex, self.SIZE)[1] == self.RANK:
                results.update({cellindex : self.cellsim(cellindex)})
        return results
    #
    def cellsim(self, cellindex):
        '''main cell simulation procedure'''
        raise NotImplementedError("cellsim() is not implemented.")

    def plot_network(self):
        '''plot cell traces'''
        print("At the beginning of plot_network! Cell positions are: ")
        print(self.cellPositions)
        if self.RANK == 0:
            fig = plt.figure(figsize=(12, 8))

            ax = fig.add_axes([0.05, 0.05, 0.9, 0.9],
                        aspect='equal', frameon=False,
                        xticks=[], xticklabels=[], yticks=[], yticklabels=[])

            for cellindex in range(self._POPULATION_SIZE):
                cells = self.create_cells(cellindex)
                for key, value in cells.iteritems():
                    zips = []
                    for x, z in value.get_idx_polygons():
                        #zips.append(list(zip(x, z)))
                        zips.append(zip(x, z))

                    polycol = PolyCollection(zips,
                                    edgecolors='none', closed = False,
                                    facecolors='bgrcmykbgrcmykbgrcmyk'[cellindex])
                                    #zorder = self.cellPositions[key][cellindex][2])
                    ax.add_collection(polycol)
            ax.plot()
            plt.show()
            '''ax.plot(self.electrodeParameters['x'],
                    self.electrodeParameters['z'],
                    marker='o', color='g', clip_on=False, zorder=0)
            ax = fig.add_axes([0.5, 0.55, 0.40, 0.4])
            for key, value in list(self.results.items()):
                tvec = np.arange(value['somav'].size) * \
                                        self.cellParameters['timeres_python']
                ax.plot(tvec, value['somav'],
                        label = 'cell %i' % key)
            leg = ax.legend()
            #ax.set_xlabel('time (ms)')
            ax.set_ylabel('$V_{soma}$ (mV)')
            ax.set_title('somatic potentials')
            ax = fig.add_axes([0.5, 0.075, 0.40, 0.4])
            cax = fig.add_axes([0.91, 0.075, 0.02, 0.40])
            im = ax.pcolormesh(tvec, self.electrodeParameters['z'], self.LFP,
                           cmap='spectral_r',
                           vmin = -abs(self.LFP).max(),
                           vmax = abs(self.LFP).max())
            ax.axis(ax.axis('tight'))
            cbar = plt.colorbar(im, cax=cax)
            cbar.set_label('LFP (mV)')
            ax.set_title('superimposed LFP')
            ax.set_xlabel('time (ms)')
            ax.set_ylabel('$z$ ($\mu$m)')'''
        fig.savefig('example_mpi.pdf', dpi=300)

    #
    def create_cells(self, cellindex):
        """Create and layout N cells in the network."""
        raise NotImplementedError("create_cells() is not implemented.")
    #
    def connect_cells(self, cells, cellindex):
        """Connect cell i to cell i + N."""
        raise NotImplementedError("connect_cells() is not implemented.")
    #

    def simulate(self,cells):
        """Run the simulation"""
