import Surface_confined_inference as sci
import os
import subprocess
fileloc="/users/hll537/ME_tests/data_files/synthetic_data/currents"
files=[os.path.join(fileloc, x) for x in os.listdir(fileloc)]
evaluator=sci.BaseMultiExperiment.from_directory("data_files/saved_class")
evaluator.file_list=files

data= {
'Ru_1': 0.33816362816901946,
'Ru_2': 0.37991003421694947,
'gamma_1': 0.6289683009049969,
'gamma_2': 0.3446262824108437,
'alpha': 0.5406295529019174,
'CdlE3': 0.5450656563040658,
'CdlE2': 0.6369692505997406,
'E0': 0.4763047855393138,
'CdlE1': 0.6258527992051286,
'k0': 0.4974184890352945,
"Cdl":0.6685053583638796

}
best=[data[x] for x in evaluator._all_parameters]
print(evaluator.optimise_simple_score(best))

