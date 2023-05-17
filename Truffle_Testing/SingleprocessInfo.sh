echo "Running...  [CTRL C to stop]"
while true; do
{
    date >> SingleprocessInfo.log
    python3 SingleprocessInfo.py >> SingleprocessInfo.log
    sleep 2
    tail -n 150 SingleprocessInfo.log | sponge SingleprocessInfo.log
} 2>&1 | tee -a SingleprocessInfo.log >/dev/null
done
