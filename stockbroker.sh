#!/bin/bash

# Check if a parameter is provided
if [ "$#" -eq 1 ]; then
    # Process the file provided as an argument
    python3 -m src/main.py "$1"
else
    # Start interactive mode
    echo -n "$ "
    while read -r line; do
        if [ "$line" == "exit" ]; then
            break
        fi
        python3 src/main.py -c "$line"
        echo -n "$ "
    done
fi