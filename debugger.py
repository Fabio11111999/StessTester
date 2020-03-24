import subprocess
import random
subprocess.run("clear")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Compile Generator:
gen_compile = subprocess.run(
	["g++", "-o", "gen", "generator.cpp"],
	capture_output = True,
	text = True)
if gen_compile.returncode != 0:
	print(bcolors.FAIL + "Generator's compilation failed: \n" + bcolors.ENDC, gen_compile.stderr)
	exit(1)
print(bcolors.OKGREEN + "Successfully Compiled generator.cpp" + bcolors.ENDC, flush = True)

#Compile checket
check_compile = subprocess.run(
	["g++", "-o", "check", "checker.cpp"],
	capture_output = True,
	text = True)
if check_compile.returncode != 0:
	print(bcolors.FAIL + "Checker's compilation failed: \n" + bcolors.ENDC, check_compile.stderr)
	exit(1)
print(bcolors.OKGREEN + "Successfully Compiled checker.cpp" + bcolors.ENDC, flush = True)

#Compile Correct Solution:
correct_compile = subprocess.run(
	["g++",
	"-std=c++17",	"-Wshadow",	"-Wall",	"-o",
	"correct", "correct.cpp",
	"-g", "-fsanitize=address",
	"-fsanitize=undefined",
	"-D_GLIBCXX_DEBUG"],
	capture_output = True,
	text = True)
if correct_compile.returncode != 0:
	print(bcolors.FAIL + "Correct solution's compilation failed: \n" + bcolors.ENDC, correct_compile.stderr)
	exit(1)
print(bcolors.OKGREEN + "Successfully Compiled correct.cpp" + bcolors.ENDC, flush = True)

#Compile Wrong Solution
wrong_compile = subprocess.run(
	["g++",
	"-std=c++17",	"-Wshadow",	"-Wall",	"-o",
	"wrong", "wrong.cpp",
	"-g", "-fsanitize=address",
	"-fsanitize=undefined",
	"-D_GLIBCXX_DEBUG"],
	capture_output = True,
	text = True)
if wrong_compile.returncode != 0:
	print(bcolors.FAIL + "Wrong solution's compilation failed:\n" + bcolors.ENDC, wrong_compile.stderr)
	exit(1)
print(bcolors.OKGREEN + "Successfully Compiled wrong.cpp" + bcolors.ENDC, flush = True)


print("\n\n", flush = True)
T = int(input("Enter the number of testcases: "))
print("\n\n", flush = True)
time_limit = int(input("Enter a Time Limit for wrong.cpp (in seconds): "))
print("\n\n", flush = True)

for t in range (1, T + 1):
	#TestCase:
	#Run Generator
	seed = random.randint(1,1000000000)
	gen_execution = subprocess.run(["./gen", str(seed)], capture_output = True)
	if gen_execution.returncode != 0:
		print("Generator's execution failed: \n", gen_execution.stderr)
		exit(1)
	file_input = open("files/input.txt", "w+")
	file_input.write(gen_execution.stdout.decode())
	file_input.close()
		
	#Run Correct Solution
	correct_execution = subprocess.run(
		"./correct",
		input = gen_execution.stdout.decode(),
		capture_output = True,
		text = True)
	if correct_execution.returncode != 0:
		print("Correct soltuion's execution failed :\n", correct_execution.stderr)
	file_output_correct = open("files/correct_output.txt", "w+")
	file_output_correct.write(correct_execution.stdout)
	file_output_correct.close()
	
	#Run Wrong Solution
	wrong_execution = subprocess.run(
		"./wrong",
		input = gen_execution.stdout.decode(),
		capture_output = True,
		text = True)
	if wrong_execution.returncode != 0:
		print("Wrong soltuion's execution failed :\n", wrong_execution.stderr)
	file_output_wrong = open("files/wrong_output.txt", "w+")
	file_output_wrong.write(wrong_execution.stdout)
	file_output_wrong.close()
	#Run Checker
	check_execution = subprocess.run("./check")
	if check_execution.returncode != 0:
		print(bcolors.BOLD + "Testcase " + str(t) + ": " + bcolors.ENDC + bcolors.FAIL + "Wrong Output." + bcolors.ENDC, flush = True)
		subprocess.run(["unlink", "correct"])
		subprocess.run(["unlink", "wrong"])
		subprocess.run(["unlink", "gen"])
		subprocess.run(["unlink", "check"])
		exit(0)
	print(bcolors.BOLD + "Testcase " + str(t) + ": " + bcolors.ENDC + bcolors.OKBLUE + "Correct Output." + bcolors.ENDC, flush = True)
	
# #Remove unnecessary files
subprocess.run(["unlink", "correct"])
subprocess.run(["unlink", "wrong"])
subprocess.run(["unlink", "gen"])
