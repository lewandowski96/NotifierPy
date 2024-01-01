import subprocess
import time

while True:
    subprocess.run(['python3.10', "runner.py"])
    time.sleep(900)
