#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _expsynr_reg();
extern void _hh1_reg();
extern void _hh2_reg();
extern void _hh3_reg();
extern void _motoneuron_reg();
extern void _motoneuron2_reg();
extern void _nap_reg();

modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," expsynr.mod");
fprintf(stderr," hh1.mod");
fprintf(stderr," hh2.mod");
fprintf(stderr," hh3.mod");
fprintf(stderr," motoneuron.mod");
fprintf(stderr," motoneuron2.mod");
fprintf(stderr," nap.mod");
fprintf(stderr, "\n");
    }
_expsynr_reg();
_hh1_reg();
_hh2_reg();
_hh3_reg();
_motoneuron_reg();
_motoneuron2_reg();
_nap_reg();
}
