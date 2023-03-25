#!/bin/bash

#script to keep running the performance test
# echo "Running...  [CTRL C to stop]"
# while [ true ]; do
# {
# date
# ./performance.py
# sleep 2
# } >> ./performance.log
# done


#script to keep running the performance test
echo "Running...  [CTRL C to stop]"
while [ true ]; do
{
date
./performance.py
sleep 2
tail -n 150 <(cat performance.log) | sponge performance.log
} 2>&1 | tee -a performance.log >/dev/null
done
