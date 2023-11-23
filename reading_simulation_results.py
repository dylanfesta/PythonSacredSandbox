#%%
import numpy as np
import pickle
import jsonpickle
import os
#%%

# reads the simulation details, and stores them in three separate
# sub-dictionaries
def read_stuff(datafolder,id):
  def read_json(filename):
    filepath = os.path.join(datafolder,'%d'%id,filename)
    return jsonpickle.decode(open(filepath,'r').read())
  rundict = read_json('run.json')
  infodic = read_json('info.json')
  configdic = read_json('config.json')
  # also , read what was printed on terminal
  cout_path = os.path.join(datafolder,'%d'%id,'cout.txt')
  cout_txt = open(cout_path,'r').read()
  return {'run':rundict,'info':infodic,
            'config':configdic,'cout':cout_txt}

# this reads the ONE binary save that was produced by the run
def read_binary_artifact(datafolder,id):
  stuff = read_stuff(datafolder,id)
  # WARNING: we assume there is only one artifact per run!
  artifact_name = stuff['run']['artifacts'][0]
  filepath = os.path.join(datafolder,'%d'%id,artifact_name)
  return pickle.load(open(filepath,'rb'))

# %%
data_folder = 'DataStorage'
id_to_read = 15

out1 = read_stuff(data_folder,id_to_read)


print(
f"""
Run {id_to_read} was executed on
{out1['run']['start_time']}
""")  

print(
f"""
Here is what was printed for run {id_to_read}
on the terminal:
-----------------------------
{out1['cout']}
-----------------------------
""")

print(
f"""
Here is what run {id_to_read}
returned :
{out1['run']['result']}
""")

# %%

out_big_arrays = read_binary_artifact(data_folder,id_to_read)
# %%
# now you can retrieve the large matrices too
for key in out_big_arrays.keys():
  print(key)
#%%
#########
# ... and here you can start making plots, etc
