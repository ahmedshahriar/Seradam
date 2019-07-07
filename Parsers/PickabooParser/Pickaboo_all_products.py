
from functions import *


#get Smart Phones Categories
smartphone_categories = get_smartphone_categories()

#get All Smart Phones Lists
for smartphone_categoriy in smartphone_categories:
    get_smartphone_list(smartphone_categoriy)



#get Feature Phones Categories
featurephone_categories = get_featurephone_categories()

#get All Feature Phones Lists
for featurephone_categoriy in featurephone_categories:
    get_featurephone_list(featurephone_categoriy)




#get Laptop Categories
loptop_categories = get_laptop_categories()

#get All Laptop lists
for category in loptop_categories:
    get_laptop_list(category)


print('done')