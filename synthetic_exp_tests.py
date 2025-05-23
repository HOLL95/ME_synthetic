import Surface_confined_inference as sci
import os
import subprocess
subprocess.run(["rm -rf results && rm -rf slurm_logs"], shell=True)
fileloc="/users/hll537/ME_tests/synthetic_data/data_files"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("saved_class")
evaluator.file_list=files

ax_int=sci.AxInterface(name="test", independent_runs=5, num_iterations=10, max_run_time=2, num_cpu=10, simulate_front=False, email="henry.lloyd-laney@york.ac.uk", in_cluster=True, project="chem-electro-2024", rclone_directory="gdrive:automated_testing", GB_ram=16)
ax_int.setup_client(evaluator)
ax_int.experiment()
#ax_int.run_bulk_simulation(0, 300)
