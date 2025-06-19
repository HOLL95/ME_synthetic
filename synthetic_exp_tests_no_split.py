import Surface_confined_inference as sci
import os
import subprocess
fileloc="/users/hll537/ME_tests/data_files/synthetic_data/currents"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("data_files/saved_class_no_split")
evaluator.file_list=files

ax_int=sci.AxInterface(name="test", 
                        independent_runs=20, 
                        num_iterations=80, 
                        max_run_time=48, 
                        results_directory="data_files/no_split_results",
                        num_cpu=2, 
                        simulate_front=True, 
                        email="henry.lloyd-laney@york.ac.uk", 
                        in_cluster=True, 
                        project="chem-electro-2024", 
                        rclone_directory="gdrive:no_split_synthetic", GB_ram=10)
ax_int.setup_client(evaluator)
#ax_int.experiment()
ax_int.restart(start_point="rclone")

