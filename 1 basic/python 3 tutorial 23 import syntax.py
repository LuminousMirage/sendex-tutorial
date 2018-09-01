##abbreviate import name statistics to s
##import statistics as s

##directly import variance from statistics, abbreviate as v and mean
from statistics import variance as v, mean

##import everything from statistics
##from statistic import *

example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
##if using abbreviate import statistics name s
##var = s.variance(example_list)

##use import method variance from statistics as v
var = v(example_list)
##use import method mean from statistics
mea = mean(example_list)

print(var)
print(mea)