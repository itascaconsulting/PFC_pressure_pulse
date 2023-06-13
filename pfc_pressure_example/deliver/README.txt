PFC3D version 5.00.23 or greater is required to run these models.

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
