# StressTester

This is a tool developed to debug and  to find corner cases in a specific C++ file stress testing it. All the files apart from ```debugger.py``` (the provided one) needs to be C++ files.

Stress testing a solution means making a certain amount of different tests and checking if one of them produced an output considered wrong. 
If the code tested produced a wrong output then the input, the output and the correct output are stored in the folder. 

## Requirements
- Python needs to be present on your machine.
- A Linux Operating system .

## Documentation: 

### List of Files:
In the folder are present several required files:
- ```debugger.py```: this is the main file, the one you should run to debug your solution. You don't need to modify this file. This file works on linux, python is required on your system.
- ```correct.cpp```: this is the "correct solution" that means that this cpp needs to print on `stdout` the correct output for the input that is read from `stdin`.
- ```wrong.cpp```: this is the "wrong solution", the one where you want to find a corner case. The file needs to read from ```stdin``` and write on ```stdout```.
- ```generator.cpp```: a file that takes a seed as its only argument and uses that seed for generating random values. The generated input will be written on ```stdout```.
- ```checker.cpp```: this file is the one that determines whether the output created by ```wrong.cpp``` is valid. When ```cheker.cpp``` is run in the folder will be present ```correct_output.txt``` and ```wrong_output.txt```: the outputs created by ```correct.cp``` and ```wrong.cpp```. If ```wrong_output.txt``` is considered correct then ```checker.cpp``` will return 0, otherwise a different value.  


### WorkFlow:
During the all execution of ```debugger.py``` if a return code different from 0 occurs than the execution in interrupted and the error is shown.
- ```generator.cpp```, ```correct.cpp``` and ```wrong.cpp``` are compiled.
- Several testcases are generated:
  - A random seed ```S``` is generated.
  - ```generator.cpp``` is executed taking ```S``` as argument, the input is redirected to ```input.txt```.
  - ```correct.cpp``` is executed redirecting ```input.txt``` as its ```stdin``` and is output (```stdout```) is redirected to ```correct_output.txt```.
   - ```wrong.cpp``` is executed redirecting ```input.txt``` as its ```stdin``` and is output (```stdout```) is redirected to ```wrong_output.txt```.
   - ```checker.cpp``` is executed, and if its return code is:
     - ```0``` then ```wrong.cpp``` produced a correct output for the current testcase.
     - different from `0` then the execution of ```debugger.py``` is interrupted and ```input.txt```, ```correct_output.txt``` and ```wrong_output.txt``` are kept in the folder.  
- All the temporary files are removed.
