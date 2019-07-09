
from functions import *
from time import time

start = time()

get_laptop_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)

get_tablet_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)

get_components_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)


get_monitor_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)

get_storage_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)


get_Photography_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)


get_network_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)


get_AudioVideo_list()
time_elapsed_ryans = round((time()-start)/60)
print("running time : {}",time_elapsed_ryans)


get_accessories_list()

time_elapsed_ryans = round((time()-start)/60)
print("total time : {} minutes",time_elapsed_ryans)