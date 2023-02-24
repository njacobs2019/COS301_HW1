#!/bin/bash

echo "Running 002"
python3 ../calcx.py < in002.txt > output.txt
diff output.txt out002.txt
rm output.txt

echo "Running 101"
python3 ../calcx.py < in101.txt > output.txt
diff output.txt out101.txt
rm output.txt

echo "Running 102"
python3 ../calcx.py < in102.txt > output.txt
diff output.txt out102.txt
rm output.txt

echo "Running 103"
python3 ../calcx.py < in103.txt > output.txt
diff output.txt out103.txt
rm output.txt

echo "Finished all tests"