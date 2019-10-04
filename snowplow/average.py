def compute(this_list):
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
