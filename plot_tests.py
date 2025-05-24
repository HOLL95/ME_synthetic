import Surface_confined_inference as sci
import os
import subprocess
classloc="/home/henryll/Documents/ME_synthetic/data_files/saved_class"
plot_class=sci.BaseMultiExperiment.from_directory(classloc)
dataloc="/home/henryll/Documents/ME_synthetic/data_files/synthetic_data/currents"
files=[os.path.join(dataloc, x) for x in os.listdir(dataloc)]
plot_class.file_list=files
plot_class.check_grouping()