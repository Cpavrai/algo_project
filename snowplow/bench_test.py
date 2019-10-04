import numpy
import parcours
import average

nb_true = 0
for i in xrange(0,10):
	randlist = numpy.random.normal(0,1000,1000)
	d_p = parcours.default_parcours(randlist, False)
	n_p = parcours.parcours(randlist, False)
	worth_ratio = average.compute(n_p)/average.compute(d_p)
	print("Is it 90% worth ? : {0} [{1:.2f} %]"
		.format(worth_ratio < 0.9, worth_ratio * 100.0))
	if worth_ratio < 0.9:
		nb_true += 1

if nb_true > 5:
	print("Success : [{0} / 10]".format(nb_true))
else:
	print("Not success : [{0} / 10]".format(nb_true))
