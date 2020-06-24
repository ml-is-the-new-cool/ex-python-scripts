def swap_variables_without_temp_var(val1, val2):
	""" Swap two variables without using a temporary variable.
	
	Example :
	a = 3, b = 5

	a = 3 + 5 = 8
	b = 8 - 5 = 3
	a = 8 - 3 = 5
	"""
	val1 = val1 + val2
	val2 = val1 - val2
	val1 = val1 - val2
	
	return val1, val2

a = 3
b = 5
print(f"Before ({a}, {b})\nAfter  {swap_variables_without_temp_var(a, b)}")
