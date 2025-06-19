import Surface_confined_inference as sci
import os
import subprocess
fileloc="/users/hll537/ME_tests/data_files/even_easier_synthetic/currents"
fileloc="data_files/even_easier_synthetic/currents/"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("data_files/saved_class_simple")
evaluator.file_list=files
data={'E0': -0.5, 'k0': 500, 'gamma': 8e-11, 'Ru': 500, 'Cdl': 0.00025, 'alpha': 0.55}
#data={'E0': -0.5, 'k0': 75, 'gamma': 8e-11, 'Ru': 500, 'Cdl': 0.00025, 'alpha': 0.55}
data={
    "gamma": 0.33333333333333326,
    "E0": 0.4999994999995,
    "alpha": 0.7777777777777777,
    "Cdl": 0.4999994999995,
    "k0": 0.49899799599198397,
    "Ru": 0.7500000000000003
    }
data={
        "Ru":0.4999994999995,
        "alpha":0.7500000000000003,
        "Cdl":0.49899799599198397,
        "k0":0.07499907499907499,
        "gamma":0.7777777777777777,
        "E0":0.4999999999999999
    }
data={
        'alpha':0.7500000000000003,
        'Ru':0.4999994999995,
        'gamma':0.7777777777777777,
        'E0':0.4999999999999999,
        'Cdl':0.24849699398797598,
        'k0':0.034999034999035,
    }
data={'alpha': 1.0, 'Cdl': 0.25167239803806307, 'k0': 0.07237526420339249, 'gamma': 0.7179099536056893, 'E0': 0.4965834624536818, 'Ru': 0.5694438833176155}
print({key:sci._utils.un_normalise(data[key], evaluator.boundaries[key]) for key in data.keys()})
best=[data[x] for x in evaluator._all_parameters]
print(evaluator.optimise_simple_score(best))

