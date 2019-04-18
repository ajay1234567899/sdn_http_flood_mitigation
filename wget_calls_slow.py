import os
import time
for i in range(1000):
    os.system('wget -O - 10.0.0.6')
    time.sleep(3)