clear; clc; close all;
format long

system_id;

tic

fprintf('cell 1');

nrncommand = [nrniv_dir...
    ' -nobanner'...
    ' testing_all.hoc -c quit()'];
system(nrncommand);

RG_E_v = cell(1,20);
RG_F_v = cell(1,20);

PF_E_v = cell(1,20);
PF_F_v = cell(1,20);

MN_E_v = cell(1,20);
MN_F_v = cell(1,20);

Iab_E_v = cell(1,20);

Ia_E_v = cell(1,20);
Ia_F_v = cell(1,20);

Ib_E_v = cell(1,20);
Ib_F_v = cell(1,20);

for b = 0:19

    RG_E_v{b+1} = textread(sprintf('RG_E_v_%d.txt',b),'%f');
    RG_F_v{b+1} = textread(sprintf('RG_F_v_%d.txt',b),'%f');

    MN_E_v{b+1} = textread(sprintf('MN_E_v_%d.txt',b),'%f');
    MN_F_v{b+1} = textread(sprintf('MN_F_v_%d.txt',b),'%f');

    PF_E_v{b+1} = textread(sprintf('PF_E_v_%d.txt',b),'%f');
    PF_F_v{b+1} = textread(sprintf('PF_F_v_%d.txt',b),'%f');

    INRG_E_v{b+1} = textread(sprintf('INRG_E_v_%d.txt',b),'%f');
    INRG_F_v{b+1} = textread(sprintf('INRG_F_v_%d.txt',b),'%f');

    Ib_E_v{b+1} = textread(sprintf('Ib_E_v_%d.txt',b),'%f');
    Ib_F_v{b+1} = textread(sprintf('Ib_F_v_%d.txt',b),'%f');

    Ia_E_v{b+1} = textread(sprintf('Ia_E_v_%d.txt',b),'%f');
    Ia_F_v{b+1} = textread(sprintf('Ia_F_v_%d.txt',b),'%f');

    Iab_E_v{b+1} = textread(sprintf('Iab_E_v_%d.txt',b),'%f');

end

pop_name = sprintf('pop_test_tau1200.mat');
save([tempdata_address pop_name]);

rasters_population(tempdata_address, pop_name, 0.025, 15000);
plot_population(tempdata_address,pop_name, 0.025, 15000);

rasters_pf_motoneurons(tempdata_address,pop_name, 0.025, 15000);
plot_pf_motoneurons(tempdata_address,pop_name, 0.025, 15000);

toc
