import subprocess
import random
import time
subprocess.run("clear")
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#prova funzinoe di compilazione
def compile_cpp(cpp, binary, safe=False):
	compilation_process = 1
	print("Compiling "  + cpp + ":", end=" ", flush=True)
	if safe:
		compilation_process = subprocess.run(
			["g++",	"-std=c++17",	"-Wshadow",	"-Wall", "-o",	binary, cpp, "-g", "-fsanitize=address", "-fsanitize=undefined",	"-D_GLIBCXX_DEBUG"],
			capture_output = True,
			text = True)
	else:
		compilation_process = subprocess.run(
			["g++", "-o", binary, cpp],
			capture_output = True,
			text = True)
	if compilation_process.returncode != 0:
		print(bcolors.FAIL + "\tCompilation failed. \n" + bcolors.ENDC, compilation_process.stderr)
		exit(1)
	print(' '*(15-len(cpp)), bcolors.OKGREEN + "\tComiplation completed \n" + bcolors.ENDC, flush=True)
	return compilation_process

gen_compile = compile_cpp("generator.cpp", "gen", False)
check_compile = compile_cpp("checker.cpp", "check", False)
correct_compile = compile_cpp("correct.cpp", "correct", True)
wrong_compile = compile_cpp("wrong.cpp", "wrong", True)


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
	start_correct_time = time.time()
	correct_execution = subprocess.run(
		"./correct",
		input = gen_execution.stdout.decode(),
		capture_output = True,
		text = True)
	end_correct_time = time.time()
	correct_time = round(end_correct_time-start_correct_time, 3)
	if correct_execution.returncode != 0:
		print("Correct soltuion's execution failed :\n", correct_execution.stderr)
	file_output_correct = open("files/correct_output.txt", "w+")
	file_output_correct.write(correct_execution.stdout)
	file_output_correct.close()
	
	#Run Wrong Solution
	start_wrong_time = time.time()
	wrong_execution = subprocess.run(
		"./wrong",
		input = gen_execution.stdout.decode(),
		capture_output = True,
		text = True,
		timeout = time_limit)
	end_wrong_time = time.time();
	wrong_time = round(end_wrong_time-start_wrong_time, 3)
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
	print(bcolors.BOLD + "Testcase " + str(t) + ": " + bcolors.ENDC + bcolors.OKBLUE + "\tCorrect Output." + bcolors.ENDC + 
				"\t\tExecution Time: " + bcolors.OKGREEN + "correct.cpp: " +bcolors.ENDC + str(correct_time) + "s\t" + bcolors.FAIL
				+ "wrong.cpp: " + bcolors.ENDC + str(wrong_time) + "s\n", flush = True)
	
# #Remove unnecessary files
subprocess.run(["unlink", "correct"])
subprocess.run(["unlink", "wrong"])
subprocess.run(["unlink", "gen"])
