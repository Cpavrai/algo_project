import numpy
import parcours
import average

randlist = numpy.random.normal(0,1000,1000)

d_p = parcours.default_parcours(randlist)
n_p = parcours.parcours(randlist)

print("Is it 90% worth ? : {0} [{1:.2f} %]".format(average.compute(n_p)/average.compute(d_p)<0.9, average.compute(n_p)/average.compute(d_p) * 100))