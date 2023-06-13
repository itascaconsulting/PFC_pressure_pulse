
# Fragmentation of intact rock by pressure pulse with PFC3D

![Fragment shapes resulting from loading at different peak pressures
and rise times.](./results.png)
Fragment shapes resulting from loading at different peak pressures
and rise times.


PFC3D is used to investigate the response of rock blocks to chemically
induced pressure pulses. Numerical experiments are conducted on 25 cm
cubes of rock with 3.8 cm diameter cylindrical cavities (holes). The
holes extend the length of the cube or are limited to the middle 7.8
cm of the cube. The cavities are filled with a chemical mixture in
which the reaction is initiated. The pressure resulting from the
reaction fragments the rock block. Itasca's discrete element software
PFC3D is used to represent the rock and model the fracturing process.
The Itasca material-modeling support package (Potyondy, 2016) is used
to create specimens of spherical-grain parallel-bonded synthetic
material, which are subject to explosive loading. Three specimens are
created, a coarse-grained 25 by 25 by 10 cm box, a fine-grained 25 by
25 by 10 cm box, and a coarse-grained 25 cm cube. The coarse models
have an average particle diameter of 8.5 mm and the fine model has an
average particle diameter of 4.25 mm. The coarse model particle
diameters were chosen to result in a specimen with approximately
10,000 particles.

Each specimen consists of a packing of spherical particles connected
by parallel bonds. Table 1 gives the material microproperties. The
essential micro properties are density (1960 kg/m3), modulus (1.5e9
Pa), normal to shear stiffness ratio (1.5), cohesion (20e6 Pa) and
tensile strength (1e6 Pa). A full description of all the
microproperties in Table 1 is given in (Potyondy, 2016). These
microproperties give rise to the following macroscopic properties: a
Young’s modulus of 1.82e9 Pa, a (static) direct tensile strength of
0.74e6 Pa and an unconfined compressive strength of 3.4e6 Pa. The
material specimens are created without a hole. The material specimens
are initially under zero stress.

# How to run this model

These data files use a combination of the PFC material modeling
support package and the PFC Python programming environment. Python is
a programming environment which is embedded in PFC3D. More information
about Python can be found in the PFC3D manual in the scripting
section.

Running master.p3dat creates all the material specimens and runs all
the cases described in the report.

The data files in the folder coarse_box/ are used to generate the
coarse specimen for this parameter study. The folder fine_box/ contains
the files that create the fine specimen, and the folder cube/
contains the files for the dimensional specimen. In these folders the
specimen geometry is defined in mvParams.p3dat and the material
properties are defined in mpParams.p3dat. Running the file
myMatGen.p3dvr in these folders creates the model save.

The folder fistSrc/ contains the files which define the material
modeling support package. Changing these files is typically
unnecessary. Note that this work was conducted with a development
version of the material modeling support package: version fistPkg21b.
The release version, fistPkg21, should have identical behavior.

The file load.py is a Python module which defines the hole excavation
and pressure loading procedure. It is not necessary to call load.py
directly, the Python files described below import functions from this
module.

The file parameter_study.py runs the 25 case parameter study. The
files base_fine.py and base3d.py run the fine model and 3D model.
These files define the hole radius, peak pressure and pressure decay
time.
