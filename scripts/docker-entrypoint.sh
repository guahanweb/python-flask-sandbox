#!/bin/bash

# if we need to run anything in the background:
# /bin/script &
# pid=$!

# we want to be sure to clean up the process on exit
# trap "kill $pid" SIGINT SIGTERM EXIT

# start up the actual python app for testing
cd /app
python app.py
echo "done... cleaning up!"