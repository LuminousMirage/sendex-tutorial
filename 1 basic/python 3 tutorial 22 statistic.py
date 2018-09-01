##statistics module comes with an assortment of goodies: Mean, median, mode, standard deviation, and variance
import statistics
example_list = [4,6,2,6,7,8,2,5,6,8,4,6,7,2,2]
##finding the mean
mea = statistics.mean(example_list)
print(mea)
##finding the median
med = statistics.median(example_list)
print(med)
##finding the standard deviation
dev = statistics.stdev(example_list)
print(dev)
##finding the variance
var = statistics.variance(example_list)
print(var)