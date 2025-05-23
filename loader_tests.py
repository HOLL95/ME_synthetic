import os
import numpy as np
import Surface_confined_inference as sci
with open(os.path.join("results", "pareto_points", "parameters.txt"), "r") as f:
            param_values = np.loadtxt(f, skiprows=1)
            f.seek(0)
            params = f.readline().strip().split()[1:]
chunk_size=300
index=0
for i in range(index*chunk_size, ((index+1)*chunk_size)):
            print(i-1, param_values.shape[0])
            if param_values.shape[0]-1<i:
             break
            parameters=dict(zip(params, param_values[i,:]))

