#!/bin/bash

#script to keep running the performance test
echo "Running...  [CTRL C to stop]"
while [ true ]; do
{
date
./performance.py
sleep 2
} >> ./performance.log
done
