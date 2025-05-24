import Surface_confined_inference as sci
import numpy as np
import os
experiments_dict={}


dictionary_list=[
    {'E_start': np.float64(-0.8901199635261801), 'E_reverse': np.float64(-0.0006379235223668012), 'omega': np.float64(3.03471913390979), 'phase': np.float64(6.05269501468929), 'delta_E': np.float64(0.2672159297976847), 'v': np.float64(0.05953326889446427)},
    {'E_start': np.float64(-0.8900244598847762), 'E_reverse': np.float64(-0.0006520099910067856), 'omega': np.float64(9.104193706642272), 'phase': np.float64(5.682042161157082), 'delta_E': np.float64(0.22351633655321063), 'v': np.float64(0.059528212300390126)},
    {'E_start': np.float64(-0.8900404672710482), 'E_reverse': np.float64(-0.0006392975440194792), 'omega': np.float64(15.173686024700986), 'phase': np.float64(5.440366237427825), 'delta_E': np.float64(0.17876387449314424), 'v': np.float64(0.05953022016638514)},
]
FT_options=dict(Fourier_fitting=True,
                Fourier_window="hanning",
                top_hat_width=0.25,
                Fourier_function="abs",
                Fourier_harmonics=list(range(3, 10)), 
                dispersion_bins=[30],
                optim_list=["E0","k0","gamma","Ru", "Cdl","CdlE1","CdlE2","CdlE3","alpha"])
boundaries={
    "E0":[-0.6, -0.3],
    "k0":[1e-3, 1000],
    "gamma":[1e-11, 1e-10],
    "Ru":[1e-3, 1000],
    "Cdl":[1e-6, 5e-4],
    "CdlE1":[-1e-2, 1e-2],
    "CdlE2":[-1e-3, 1e-3],
    "CdlE3":[-1e-4, 1e-4],
    "alpha":[0.4, 0.6]
}
zero_ft=[-0.425, 100, 8e-11,100, 1.8e-4,  1e-5, 1e-5, -1e-6,0.5]
labels=["3_Hz", "9_Hz", "15_Hz"]
common={
    "Temp":278, 
    "N_elec":1,
    "area":0.036,
    "Surface_coverage":1e-10

}
for i in range(0, len(labels)):
    experiments_dict=sci.construct_experimental_dictionary(experiments_dict, {**{"Parameters":dictionary_list[i]}, **{"Options":FT_options}, "Zero_params":zero_ft}, "FTACV", labels[i], "280_mV")

v=sci.MultiExperiment(experiments_dict, common=common, synthetic=True, normalise=True, boundaries=boundaries)
v.group_list=[
           {"experiment":"FTACV",  "type":"ts", "numeric":{"Hz":{"lesser":10}, "mV":{"equals":280}}, "scaling":{"divide":["omega", "delta_E"]}},
           {"experiment":"FTACV", "type":"ft", "numeric":{"Hz":{"lesser":10}, "mV":{"equals":280}}, "scaling":{"divide":["omega", "delta_E"]}}, 
            {"experiment":"FTACV", "type":"ts", "numeric":{"Hz":{"equals":15}, "mV":{"equals":280}}, "scaling":{"divide":["omega", "delta_E"]}},
            {"experiment":"FTACV", "type":"ft", "numeric":{"Hz":{"equals":15}, "mV":{"equals":280}}, "scaling":{"divide":["omega", "delta_E"]}}]

v.seperated_parameters={x:[range(0, 2), range(2, 4)] for x in ["Ru","gamma"]}
sim_vals=[0.5+sci.un_normalise(np.random.rand(), [-1, 1])*0.2 for x in v._all_parameters]
with open("data_files/synthetic_data/param_values.txt","w" )as f:
    f.write("\n".join(["{0}:{1}".format(x,y) for x, y in zip(v._all_parameters, sim_vals)]))
sim_vals=v.evaluate(sim_vals)
for key in sim_vals.keys():
    cls=v.classes[key]["class"]
    current=sci._utils.add_noise(sim_vals[key], 0.01*max(np.abs(sim_vals[key])))
    if "SWV" in key:
        times=np.linspace(0, 1, len(sim_vals[key])+1)
        current=np.append(current, 0)
    else:
        times=cls.dim_t(v.classes[key]["times"])
    
    file=np.column_stack((times, cls.dim_i(current)))
    with open("data_files/synthetic_data/currents/{0}.txt".format(key) ,"w")as f:
        np.savetxt(f, file)
v.save_class("data_files/saved_class", include_data=True)
