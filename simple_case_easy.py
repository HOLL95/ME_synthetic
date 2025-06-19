import Surface_confined_inference as sci
import os
import subprocess
fileloc="data_files/even_easier_synthetic/currents/"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("data_files/saved_class_simple")

evaluator.file_list=files

ax_int=sci.AxInterface(name="simplest_case_easy", 
                        independent_runs=20, 
                        num_iterations=80, 
                        max_run_time=48, 
                        results_directory="data_files/scaled_results",
                        num_cpu=2, 
                        simulate_front=True, 
                        email="henry.lloyd-laney@york.ac.uk", 
                        in_cluster=True, 
                        project="chem-electro-2024", 
                        rclone_directory="gdrive:scaled_again", GB_ram=10)
ax_int.setup_client(evaluator)
ax_int.experiment()
#ax_int.restart(start_point="pool")
