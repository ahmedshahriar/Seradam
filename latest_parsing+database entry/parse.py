from time import time
start = time()

from ryans import *
from startech import *

startech_all_laptop()
ryans_all_laptop()


time_elapsed_ryans = round((time()-start))
print("total time : {} seconds",time_elapsed_ryans)
