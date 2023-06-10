


from whispercpp import Whisper
w = Whisper.from_pretrained("tiny.en")
output = w.transcribe_from_file("./samples/gb0.wav")
print(output)






















# import subprocess
# import psutil

# binary_path = './command'
# model_path = './models/ggml-base.bin'
# n_threads = '8'

# try:
#     # Run the C++ binary and capture its output in real-time
#     process = subprocess.Popen([binary_path, '-m', model_path, '-t', n_threads], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

#     # Get the parent process ID
#     parent_pid = process.pid

#     # Get the parent process object
#     parent_process = psutil.Process(parent_pid)

#     # Iterate over all child processes recursively
#     for child_process in parent_process.children(recursive=True):
#         # Print the process ID and command line
#         print(f"Process ID: {child_process.pid}")
#         print(f"Command Line: {' '.join(child_process.cmdline())}")
#         print()

#     # Read and print the output line by line
#     for line in process.stdout:
#         print(line.strip())

#     # Wait for the process to finish
#     process.wait()

# except subprocess.CalledProcessError as e:
#     # An error occurred while running the binary
#     print(f"Error: {e.returncode}, {e.output.strip()}")















# import subprocess

# binary_path = './command'
# model_path = './models/ggml-base.bin'
# n_threads = '8'

# try:
#     # Run the C++ binary and capture its output
#     output = subprocess.check_output([binary_path, '-m', model_path, '-t', n_threads], stderr=subprocess.STDOUT)
    
#     # Decode the output from bytes to string
#     output = output.decode('utf-8').strip()
    
#     # Print the output
#     print(output)
    
# except subprocess.CalledProcessError as e:
#     # An error occurred while running the binary
#     print(f"Error: {e.returncode}, {e.output.decode('utf-8').strip()}")


# import subprocess

# binary_path = './command'
# model_path = './models/ggml-base.bin'
# n_threads = '8'

# try:
#     # Run the C++ binary and capture its output in real-time
#     process = subprocess.Popen([binary_path, '-m', model_path, '-t', n_threads], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    
#     # Read and print the output line by line
#     for line in process.stdout:
#         print(line.strip())

#     # Wait for the process to finish
#     process.wait()

# except subprocess.CalledProcessError as e:
#     # An error occurred while running the binary
#     print(f"Error: {e.returncode}, {e.output.strip()}")




# import ctypes

# # Load the shared library
# cpp_lib = ctypes.CDLL('./cpp_wrapper.so')

# # Define the argument and return types of the function
# cpp_lib.invokeCppFunction.argtypes = [ctypes.c_int]
# cpp_lib.invokeCppFunction.restype = ctypes.c_char_p

# def call_cpp_main(input):
#     # Call the C++ function and convert the returned C string to Python string
#     result = cpp_lib.invokeCppFunction(input).decode('utf-8')
#     return result

# # Test the function
# output = call_cpp_main("-m ./models/ggml-base.bin -t 8")
# print(output)  # Output: 10





# import subprocess

# def run_cpp_binary():
#     # Replace 'binary_path' with the actual path to your compiled C++ binary
#     # binary_path = '/path/to/your/binary'
#     binary_path = 'command'
#     model_path='./models/ggml-base.bin'

#     # Prompt the user to enter input
#     # user_input = input("Enter input: ")
#     user_input = f"-m {model_path} -t 8"
    
#     # Run the C++ binary and capture its output
#     process = subprocess.Popen([binary_path],
#                                stdin=subprocess.PIPE,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE)

#     # Send user input to the binary
#     process.stdin.write(user_input.encode())
#     process.stdin.close()

#     # Poll for the output while the process is running
#     while process.poll() is None:
#         output = process.stdout.readline().decode('utf-8').strip()
#         if output:
#             print(output)

#     # Process remaining output after the process completes
#     remaining_output = process.stdout.read().decode('utf-8').strip()
#     if remaining_output:
#         print(remaining_output)

#     # Check for errors
#     if process.returncode != 0:
#         error_output = process.stderr.read().decode('utf-8').strip()
#         print(f"Error: {process.returncode}, {error_output}")

# run_cpp_binary()


# def run_cpp_binary():
#     # Replace 'binary_path' with the actual path to your compiled C++ binary
#     binary_path = 'command'
#     model_path='./models/ggml-base.bin'
    
#     try:
#         # Prompt the user to enter input
#         # user_input = input("Enter input: ")
#         user_input = f"-m {model_path} -t 8"
        
#         # Run the C++ binary and capture its output
#         output = subprocess.check_output([binary_path], input=user_input.encode(), stderr=subprocess.STDOUT)
        
#         # Decode the output from bytes to string
#         output = output.decode('utf-8').strip()
        
#         # Print the output
#         print(output)
        
#     except subprocess.CalledProcessError as e:
#         # An error occurred while running the binary
#         print(f"Error: {e.returncode}, {e.output.decode('utf-8').strip()}")
        
# run_cpp_binary()










# import subprocess

# def run_cpp_command():
  

#     try: 
#         result = subprocess.Popen(f".././command -m ./models/ggml-base.bin -t 8", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

#         while result.poll() is None:
#             output = result.stdout.readline().decode().strip("\n")
#             print(output)
#     except KeyboardInterrupt:
#         print("")
#         print("exit. ")

#     except:
#         print("Error while uploading!")
#         exit() 

# run_cpp_command() 
