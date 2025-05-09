#!/bin/bash

set -e

if [ "$#" -eq 1 ]; then
    # File input mode
    python3 -m src.main "$1"
else
    # Interactive mode using temp file
    echo "Interactive mode (type 'exit' to quit)"
    echo -n "$ "
    while IFS= read -r line; do
        if [[ "$line" == "exit" ]]; then
            break
        fi
        echo "$line" > .tmp_input.txt
        python3 -m src.main .tmp_input.txt
        echo -n "$ "
    done
    rm -f .tmp_input.txt
fi
