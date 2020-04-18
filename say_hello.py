import os, sys

file_path = os.path.join(sys.path[0], 'hello.txt')
log_file = open(file_path, 'a')
log_file.write('Hello world\n')
log_file.close()
