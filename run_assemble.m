clear;clc;close all;

ppn = 1e2+1;
inl = 100;% how many times longer is a paranode than a node?
diam = log(random('logn', 9, 0.2, 10, 1));
%diam = [9,5];
start_offset = 0:5:100;
%start_offset = 0;
file_list = {'5M mesh\no_root_um',...
    '5M mesh\one_root_um',...
    '5M mesh\move_root_um',...
    '5M mesh\one_root_um_altel',...
    '5M mesh\move_root_um_altel'...
};
tag_list = {'straight, root omitted',...
    'straight, root explicit',...
    'aligned, root explicit',...
    'straight, root explicit, alternative electrode',...
    'aligned, root explicit, alternative electrode'...
};
points_list = {'axon_centers.csv',...
    'axon_centers.csv',...
    'moved_axon_centers.csv',...
    'axon_centers.csv',...
    'moved_axon_centers.csv'...
};
for a = 1:length(file_list)
    assemble_voltages(file_list{a},tag_list{a},...
        points_list{a},diam,start_offset, inl, ppn,0);
end