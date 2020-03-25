# StressTester

This is a tool developed to debug and  to find corner cases in a specific C++ file stress testing it. All the files apart from ```debugger.py``` (the provided one) needs to be C++ files.

Stress testing a solution means making a certain amount of different tests and checking if one of them produced an output considered wrong. 
If the code tested produced a wrong output then the input, the wrong output and the correct output are stored in the folder. 

## Requirements
- Python needs to be present on your machine.
- A Linux Operating System .

## Documentation: 

### List of Files:
In the folder are present several required files:
- ```debugger.py```: this is the main file, the one you should run to debug your solution. You don't need to modify this file. This file works on linux, python is required on your system.
- ```correct.cpp```: this is the "correct solution" that means that this cpp needs to print on `stdout` the correct output for the input that is read from `stdin`.
- ```wrong.cpp```: this is the "wrong solution", the one where you want to find a corner case. The file needs to read from ```stdin``` and write on ```stdout```.
- ```generator.cpp```: a file that takes a seed as its only argument and uses that seed for generating a random test case. The generated input will be written on ```stdout```.
- ```checker.cpp```: this file is the one that determines whether the output created by ```wrong.cpp``` is valid. When ```cheker.cpp``` is run in the folder will be present ```files/correct_output.txt``` and ```files/wrong_output.txt```: the outputs created by ```correct.cpp``` and ```wrong.cpp```. If ```files/wrong_output.txt``` is considered correct then ```checker.cpp``` will return 0, otherwise a different value.  


### WorkFlow:
During the all execution of ```debugger.py``` if a return code different from 0 occurs than the execution in interrupted and the error is shown.
- ```generator.cpp```, ```correct.cpp``` ,```wrong.cpp``` and ```checker.cpp``` are compiled.
- The number of cases and the Time Limit for ```wrong.cpp``` are read in input.
- Several testcases are generated:
  - A random seed ```S``` is generated.
  - ```generator.cpp``` is executed taking ```S``` as argument, the output is redirected to ```files/input.txt```.
  - ```correct.cpp``` is executed redirecting ```files/input.txt``` as its ```stdin``` and is output (```stdout```) is redirected to ```files/correct_output.txt```.
   - ```wrong.cpp``` is executed redirecting ```files/input.txt``` as its ```stdin``` and is output (```stdout```) is redirected to ```files/wrong_output.txt```. If the execution time of ```wrong.cpp``` is greater than the time limit chosen by the user than the execution of ```debugger.py``` is interrupted and ```input.txt```, ```correct_output.txt``` and ```wrong_output.txt``` are kept in the folder ```files```.  
   - ```checker.cpp``` is executed, and if its return code is:
     - ```0``` then ```wrong.cpp``` produced a correct output for the current testcase.
     - different from `0` then the execution of ```debugger.py``` is interrupted and ```input.txt```, ```correct_output.txt``` and ```wrong_output.txt``` are kept in the folder ```files```.  
- All the temporary files are removed.

throughout the all execution the user will be able to see the result of each individual test, and some related information.
