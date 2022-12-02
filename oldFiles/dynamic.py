from time import sleep
import sys

# for i in range(10):
#     sys.stdout.write("\rTime remaining: {} Seconds".format(i))
#     sys.stdout.flush()
#     sleep(1)
import shutil

def get_terminal_columns():
   print(shutil.get_terminal_size().columns)
get_terminal_columns()