def power_set(sett):

	final = list()
	if len(sett) == 0:
		return [[]]

	else:
		first = sett[0]
		rest_sets = power_set(sett[1:])
		for sets in rest_sets:
			copy = list(sets)
			copy.append(first)
			final.append(copy)
		final.extend(rest_sets)

		return final


print(power_set([1, 2]))
