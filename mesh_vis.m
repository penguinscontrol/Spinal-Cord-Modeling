clear;clc;
close all;
system_id_old;
comsol_file = 'E:\Google Drive\CSP\testbed\COMSOL Trial\pieces';
fem = mphload([comsol_file '.mph']);
geom = 'geom1';

get_geom_names;

%% View Geometry
nice_colors = parula(21);

f1 = rfig();
ax = gca;
hold on;

% Plot neuron
% [tree, name, path] = load_tree([tempdata_address 'model_tree.neu']);
% plot_tree(tree{1},[1 0 0]);
% hold on;
% plot_tree(tree{2},[1 0 0]);

%mphplot(fem,'pg2');
%mphplot(fem,'pg3');
%edges
mphviewselection(fem,geom,el_edge, ...
    'entity', 'edge', ...
    'parent',ax, ...
    'facealpha', 0, ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', [0 0 0], ...
    'edgecolor', [0 0 0] ...
    );

%faces
mphviewselection(fem,geom,el_dom, ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 1, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(1,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );

% Plot GM

%edges
mphviewselection(fem,geom,gm_edge, ...
    'entity', 'edge', ...
    'parent',ax, ...
    'facemode', 'off', ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', [0 0 0], ...
    'edgecolor', [0 0 0] ...
    );

%faces
mphviewselection(fem,geom,gm_dom(1:6), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.05, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(1,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );
%faces
mphviewselection(fem,geom,gm_dom(7:end), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.4, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(1,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );

% Plot WM

%edges
mphviewselection(fem,geom,wm_edge, ...
    'entity', 'edge', ...
    'parent',ax, ...
    'facemode', 'off', ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', [0 0 0], ...
    'edgecolor', [0 0 0] ...
    );

%faces
mphviewselection(fem,geom,wm_dom(1:6), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.05, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(5,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );
%faces
mphviewselection(fem,geom,wm_dom(7:end), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.4, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(5,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );

% CSF

%faces
mphviewselection(fem,geom,csf_dom(1:6), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.05, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(10,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );
%faces
mphviewselection(fem,geom,csf_dom(7:end), ...
    'entity', 'domain', ...
    'parent',ax, ...
    'facealpha', 0.4, ...
    'facecolor', [1 0 0], ...
    'facecolorselected', nice_colors(10,:), ...
    'geommode', 'off', ...
    'edgemode', 'on', ...
    'edgecolorselected', 'k', ...
    'edgecolor', 'k' ...
    );

%%
view(2);
campos([5e3 -5e3 -50e3]);
camtarget([0e3 0e3 10e3]);
camroll(45);
zoom(1.2);
title('Mesh');
xlabel('x (um)');
ylabel('y (um)');
zlabel('z (um)');
print('-dpng',[tempdata_address 'mesh_view']);