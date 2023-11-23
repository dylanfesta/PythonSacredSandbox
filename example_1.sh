# Make sure you activated the local environment before you proceed!

# Here I can run the two regimes I specified in parallel
python3 ./running_the_simulation.py with regime_1 &
python3 ./running_the_simulation.py with regime_2 

wait

# or I can customize the parameters for each regime

python3 ./running_the_simulation.py with regime_1 parameter_2=999.99
