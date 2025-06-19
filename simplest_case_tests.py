import Surface_confined_inference as sci
import os
import subprocess
fileloc="/users/hll537/ME_tests/data_files_hard/synthetic_data/currents"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("data_files_hard/saved_class_simple")
evaluator.file_list=files

ax_int=sci.AxInterface(name="simplest_case_hard", 
                        independent_runs=20, 
                        num_iterations=80, 
                        max_run_time=48, 
                        results_directory="data_files_hard/simplest_case",
                        num_cpu=16, 
                        simulate_front=True, 
                        email="henry.lloyd-laney@york.ac.uk", 
                        in_cluster=True, 
                        project="chem-electro-2024", 
                        rclone_directory="gdrive:simple_synthetic", GB_ram=10)
ax_int.setup_client(evaluator)
#ax_int.experiment()
ax_int.restart(start_point="pool")
