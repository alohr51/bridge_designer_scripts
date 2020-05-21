# Bridge Designer Scripts

Scripts that parse test output from the bridge designer

## bridge_calc.py

* Takes in a filename that holds csv data from the test output from the Bridge Designer application and calculates the compression ratio, tenstion ratio, and a final score.

## bridge_test_output.csv

* A sample csv file the `bridge_calc.py` takes in. We generated this file by copying the test output to the clipboard, pasting it into excel and exporting it as a .csv file. The top headers are also removed.
