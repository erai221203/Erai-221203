import numpy
#Quantile
values = [13,21,21,40,42,48,55,72]
x = numpy.quantile(values,[0,0.25,0.5,0.75,1])
print(x)
#Percentile:
x = numpy.percentile(values, 65)
print(x)
