import subprocess
import random
T=4
#Compile Generator:
gen_compile = subprocess.run(
	["g++", "-o", "gen", "generator.cpp"],
	capture_output=True,
	text=True)
if gen_compile.returncode!=0:
	print("Generator's compilation failed: \n'", gen_compile.stderr)
	exit(1)
	
#Compile Correct Solution:
correct_compile=subprocess.run(
	["g++",
	"-std=c++17",	"-Wshadow",	"-Wall",	"-o",
	"correct", "correct.cpp",
	"-g", "-fsanitize=address",
	"-fsanitize=undefined",
	"-D_GLIBCXX_DEBUG"],
	capture_output=True,
	text=True)
if correct_compile.returncode!=0:
	print("Correct solution's compilation failed: \n'", correct_compile.stderr)
	exit(1)

#Compile Wrong Solution
wrong_compile=subprocess.run(
	["g++",
	"-std=c++17",	"-Wshadow",	"-Wall",	"-o",
	"wrong", "wrong.cpp",
	"-g", "-fsanitize=address",
	"-fsanitize=undefined",
	"-D_GLIBCXX_DEBUG"],
	capture_output=True,
	text=True)
if wrong_compile.returncode!=0:
	print("Wrong solution's compilation failed: \n'", wrong_compile.stderr)
	exit(1)

for t in range (1, T+1):
	#TestCase:
	#Run Generator
	print("Testcase: ",t)
	seed=random.randint(1,1000000000)
	gen_execute=subprocess.run(["./gen", str(seed)], capture_output=True)
	if gen_execute.returncode!=0:
		print("Generator's execution failed: \n'", correct_compile.stderr)
		exit(1)
	#Run Correct Solution
	correct_execution=subprocess.run(
		"./correct",
		input=gen_execute.stdout.decode(),
		capture_output=True,
		text=True)
	print(correct_execution.stdout);
	#Run Wrong Solution
	wrong_execution=subprocess.run(
		"./wrong",
		input=gen_execute.stdout.decode(),
		capture_output=True,
		text=True)
	print(wrong_execution.stdout, flush=True);
