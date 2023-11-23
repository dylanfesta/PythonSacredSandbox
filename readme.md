
# Example on the usage of Python, virtual environments and Sacred

## Creating and restoring a new virtual environment

This creates an environment in the folder `.venv` the dot in front makes it a hidden folder (so it will be automatically ignored by git).

```
python -m venv .venv
```

Now activate it:
```
source .venv/bin/activate
```

Then install stuff (just the essential for this demo)
```
pip install numpy sacred
```
(here you can install anything you need)


To store this virtual environment, run
```
pip freeze > requirements.txt
```

In a new machine, you can reinitialize this same environment with these three commands:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Example of the use of sacred

Check the file `running_the_simulation.py` to get an idea of how parameters are handled and how/where they are saved. Then check `example_1.sh`. To run the example, first load the virtual environment, then run it with `bash ./example_1.sh`.

At this point, you can go in the data folder and see the files that are created and their contents. They are either dictionaries, or log files, or a single binary save of large data.

The simulation results are read in `reading_simulation_results.py`

How do you parallelize? Just use shell scripts as in `example_2_gobig.sh`.
