#%%
import pickle
import jsonpickle
import os

#%%

data_folder = 'DataStorage'

assert os.path.exists(data_folder),f"Directory {data_folder} does not exist!!!"

# list all subfolders
os.listdir(data_folder)


#%%

# now for all saved simulations print ID, print info label, and warn if there is 
# no binary file saved and if the simulation status is not complete.

for mydir in os.listdir(data_folder):
  # if does not contain config.json, move on
  configfile = os.path.join(data_folder,mydir,'config.json')
  if not os.path.exists(configfile):
    continue
  configdict = jsonpickle.decode(open(configfile,'r').read())
  print(f"ID {mydir}  - Label {configdict['label']}")
  runfile = os.path.join(data_folder,mydir,'run.json')
  rundict = jsonpickle.decode(open(runfile,'r').read())
  if not rundict["status"] == "COMPLETED":
    print(f"WARNING: run {mydir} did not complete!!!")
  if rundict['artifacts'] == []:
    print(f"WARNING: run {mydir} did not save any binary file!!!")


# %%
# Here I just show the good runs, and I show their final score

for mydir in os.listdir(data_folder):
  # if does not contain config.json, move on
  configfile = os.path.join(data_folder,mydir,'config.json')
  runfile = os.path.join(data_folder,mydir,'run.json')
  if not os.path.exists(configfile):
    continue
  configdict = jsonpickle.decode(open(configfile,'r').read())
  rundict = jsonpickle.decode(open(runfile,'r').read())
  if rundict['artifacts'] == []:
    continue
  # okay, now they should ALL be good
  # this returns the first element returned by the main function
  score = rundict['result'][0]
  print(f"ID {mydir}  - score {score:.2f}")
  # this also shows stuff I saved during the simulation
  # using _run['info']['my_notes'] = ...
  infodict = jsonpickle.decode(open(os.path.join(data_folder,mydir,'info.json'),'r').read())
  print(infodict['my_notes'])



# %%
