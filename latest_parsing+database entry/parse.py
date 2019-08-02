import time
start = time.time()

from ryans import *
from startech import *

startech_parse_all_laptop()
# ryans_parse_all_laptop()

# ryans_analyze_processor("AMD Ryzen 3 2200U")


time_elapsed_ryans = round((time.time()-start))
print("total time : {} seconds",time_elapsed_ryans)
