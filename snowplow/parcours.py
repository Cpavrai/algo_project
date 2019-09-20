import numpy
import time

def average(this_list):
	res = 0

	for house in this_list:
		res += abs(house)
	return res / len(this_list)

def parcours(this_list):
	'''
		return list of sorted houses in the relevant order.
	'''
	# print("Distance from new : {0}".format(total_distance))
	# print("Average for new : {0}".format(total_distance / len(this_list)))
	return this_list


def default_parcours(this_list):
	'''
		same as parcours, but not optimized (used for comparing)
		it will just reach the nearest point
	'''

	# initialize the result with the first house
	tmp_list = list(this_list)
	res = []
	x = 0
	distance = 0
	total_distance = 0

	while len(tmp_list) > 0:
		distance = abs(tmp_list[0] - x)
		tmp_distance = tmp_list[0]
		for house in tmp_list:
			if distance > abs(house - x):
				distance = abs(house - x)
				tmp_distance = house
		total_distance += abs(distance)
		res.append(tmp_distance)
		x = tmp_distance
		tmp_list.remove(x)
	print("Distance from default : {0}".format(total_distance))
	print("Average for default : {0}".format(total_distance / len(this_list)))
	return res

randlist = numpy.random.normal(0,1000,1000)

d_p = default_parcours(randlist)

n_p = parcours(randlist)

print("Is it 90% worth ? : {0}".format(average(d_p)/average(n_p)<0.9))