from __future__ import division

import numpy
import math

def average(this_list):
	'''
		computes average distance done by snowplow
		and returns it
	'''
	distance = 0
	tmp_house = 0
	total_res = 0

	for house in this_list:
		distance += abs(house - tmp_house)
		total_res += distance
		tmp_house = house
	return total_res / len(this_list)

def density(this_list):
	if len(this_list) == 1:
		return 1
	return len(this_list) / abs(this_list[-1] - this_list[0])

def get_most_worth(this_list, index):
	'''
		return the most worth point to access to
	'''
	supp_list = filter(lambda x : x > index, this_list)
	less_list = filter(lambda x : x < index, this_list)

	if len(supp_list) == 0:
		return less_list[-1]
	elif len(less_list) == 0:
		return supp_list[0]

	next_point = supp_list[0]
	less_point = less_list[-1]

	next_dist = abs(next_point - index)
	less_dist = abs(less_point - index)

	if density(supp_list) / next_dist < density(less_list) / less_dist:
		return less_list[-1]
	else:
		return supp_list[0]

def parcours(this_list):
	'''
		return list of sorted houses in the relevant order.
	'''
	tmp_list = list(this_list)
	tmp_list.sort()
	total_distance = 0
	tmp_distance = 0
	res = []

	while len(tmp_list) > 0:
		if len(tmp_list) == 1:
			next_nb = tmp_list[0]
		else:
			next_nb = get_most_worth(tmp_list, tmp_distance)
		total_distance += abs(next_nb - tmp_distance)
		tmp_distance = next_nb
		res.append(next_nb)
		# We get this point out from the list
		tmp_list.remove(next_nb)

	print("Distance from new : {0}".format(total_distance))
	print("Average for new : {0:.2f}".format(average(res)))
	return res


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
	print("Distance totale from default : {0}".format(total_distance))
	print("Average for default : {0:.2f}".format(average(res)))
	return res

randlist = numpy.random.normal(0,1000,1000)
# randlist = [-15, -10, -12, 3, -1, 11]

d_p = default_parcours(randlist)
n_p = parcours(randlist)
# print("Default : {0}".format(d_p))
# print("Ours    : {0}".format(n_p))

print("Is it 90% worth ? : {0} [{1:.2f} %]".format(average(n_p)/average(d_p)<0.9, average(n_p)/average(d_p) * 100))