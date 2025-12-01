#!/bin/bash
# Usage: ./runner_c.sh /path/to/code.c

CODE_FILE="$1"

if [ ! -f "$CODE_FILE" ]; then
  echo "Error: C code file not found."
  exit 1
fi

gcc "$CODE_FILE" -o temp_executable
if [ $? -ne 0 ]; then
  exit 1
fi

./temp_executable
rm -f temp_executable
