
from functions import *

smartphone_categories = get_smartphone_categories()

featurephone_categories = get_featurephone_categories()

for featurephone_categoriy in featurephone_categories:
    get_featurephone_list(featurephone_categoriy)

for smartphone_categoriy in smartphone_categories:
    get_smartphone_list(smartphone_categoriy)


print('done')