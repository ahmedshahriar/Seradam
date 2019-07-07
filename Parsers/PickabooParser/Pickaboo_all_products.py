
import time
from functions import *


start = time.time()

get_mobile_list()

get_mobileAccessories_list()


get_computer_list()


get_computerAccessories_list()


get_gaming_console_list()

end = time.time()
print("time elapsed : ",end="")
print(end-start)
print('done')