import subprocess
import time

output = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE)
stdout = output.communicate()
print(stdout)
