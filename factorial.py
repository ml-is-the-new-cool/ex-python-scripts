#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def exponential(base: int, exponent: int) -> float:
	"""Recursive power function.
	"""
	if exponent < 0:
		if base == 0:
			raise ValueError("You can't raise 0 to the power of a negative number.")
		return 1.0 / exponential(base, -exponent)

	if exponent == 0:
		return 1.0

	half_exponent = exponential(base, int(exponent / 2))
	if exponent % 2 == 0:
		return half_exponent * half_exponent

	return base * half_exponent * half_exponent #exponential(base, exponent - 1)

if __name__ == "__main__":
	import sys
	print(exponential(int(sys.argv[1]), int(sys.argv[2])))
