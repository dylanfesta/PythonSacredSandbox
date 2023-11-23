#%%
from sacred import Experiment
import pickle
import time,os
import numpy as np

import random
import string

"""
Imagine we have a long and nasty simulation to run. The simulation 
depends on three parameters, is slow, and produces a large output.
"""

#%%

# create an experiment object
ex = Experiment("long_nasty_experiment")

# Create an observer, to store the results
# for simplicity, I choose a local folder
# (but I could also indicate a remote folder)
from sacred.observers import FileStorageObserver
ex.observers.append(FileStorageObserver('DataStorage'))

@ex.config
def default_config():
  withbugs = 0
  parameter_1 = 1.0
  parameter_2 = 0.0
  parameter_3 = np.NAN
  parameter_4_idx = -1
  label = 'default'
  notes = 'Default configuration! Is this a test?!'
  
@ex.named_config
def regime_1():
  parameter_2 = -1.0
  parameter_3 = 10.0
  parameter_4_idx = 0
  label = 'the_regime_1'
  notes = 'I am trying the regime 1'

@ex.named_config
def regime_2():
  parameter_2 = 30.0
  parameter_3 = 90.0
  parameter_4_idx = 1
  label = 'the_regime_2'
  notes = 'I am trying the regime 2'

# the argument of the main function MUST contain ALL parameters
# defined in the configuration.

@ex.automain
def run(parameter_1, parameter_2, parameter_3, parameter_4_idx,
          label,notes,withbugs,_seed,_run):
  # the last parameter is picked from a fixed list of values
  parameter_4_vec = np.linspace(-3,3,10)
  parmeter_4 = parameter_4_vec[parameter_4_idx]
  print('parameter_1 = ', parameter_1)
  print('parameter_2 = ', parameter_2)
  print('parameter_3 = ', parameter_3)
  print('parameter_4_idx = ', parameter_4_idx)
  # long and nasty run
  print('Now running intensive computations...')
  time.sleep(60)
  if withbugs==1:
    if np.random.rand() < 0.17:
      raise ValueError('OH NO! TERRIBLE ERROR!!!  X-(  Nothing can be saved!')
  print('Run completed! Now storing the results')
  # lots of data !
  data_stuff1 = np.random.rand(100,100)*parameter_1
  data_stuff2 = np.random.rand(100,100)*parameter_2
  data_stuff3 = np.random.rand(100,100)*parameter_3
  # and some summary statistics
  my_score = np.random.rand()
  great_success = (my_score > 0.5)
  # save it in a dictionary
  dict_save = {'data_stuff1':data_stuff1,
                'data_stuff2':data_stuff2,
                'data_stuff3':data_stuff3,
                'my_score':my_score,
                'great_success':great_success}
  # save it in a pickle file
  # to avoid clashes, add random string to it
  random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
  filename = 'binary_storage_'+label+random_string+'.pkl'
  with open(filename,'wb') as f:
    pickle.dump(dict_save,f)
  print('Results stored in ',filename)
  # now, you can keep the file, or just store it internally, through the observer
  _run.add_artifact(filename)
  # since the observer has it, I can delete the local copy
  os.remove(filename)
  # I can also store stuff like this
  _run.info['my_notes'] = notes + ' -  success: ' + str(great_success)
  # the returned values are also stored 
  # ... but keep them small! Vectors etc all go in the artifacts
  return my_score,great_success


  
  
  