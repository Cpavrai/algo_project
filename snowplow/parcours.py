from __future__ import division
import average

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

def parcours(this_list, show=True):
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

	if show:
		print("Distance from new : {0}".format(total_distance))
		print("Average for new : {0:.2f}".format(average.compute(res)))
	return res


def default_parcours(this_list, show=True):
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
	if show:
		print("Distance totale from default : {0}".format(total_distance))
		print("Average for default : {0:.2f}".format(average.compute(res)))
	return res