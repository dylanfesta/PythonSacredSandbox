# Make sure you activated the local environment before you proceed!

# now, parameter 4 can take 10 different values
# let's say I want to run all 10 values both in regime 1
# and regime 2. However 20 parallel processes are too many!
# I split them in two cycles of 10 each

for i in {0..9}
do
    python3 ./running_the_simulation.py with regime_1 parameter_4_idx=$i withbugs=1 &
done

wait
echo -e '\n\nFirst bactch completed! Now moving to second!!!\n\n'

for i in {0..9}
do
    python3 ./running_the_simulation.py with regime_2 parameter_4_idx=$i withbugs=1 &
done

wait
echo -e '\n\nSecond bactch completed!\n\n'


