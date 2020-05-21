#!/usr/bin/env python3
import statistics
A_GRADE_FENCE = .4
B_GRADE_FENCE = .6

def calc_ratio(label, file_name, col1, col2):
	file_handle = open(file_name)
	ratios = []

	for line in file_handle:
		split_words = line.split(',')
		num1 = float(split_words[col1])
		num2 = float(split_words[col2])

		if num2 == 0:
			print("cannot divide by 0 for identifier:", split_words[0])
			continue

		ratio = num1 / num2
		ratios.append(ratio)

	file_handle.close()
	return statistics.mean(ratios)

def get_grade(ratio_average):
	if ratio_average <= A_GRADE_FENCE:
		return "A"
	elif ratio_average <= B_GRADE_FENCE:
		return "B"

	return "C"

def calc_score(compression_ratio, tension_ratio, num_carbon_steel_beams):
	return ((compression_ratio * 1000) + (tension_ratio * 1000)) * (1 + (.01 * num_carbon_steel_beams))

compression_ratio = calc_ratio("compression", "bridge_test_output.csv", 5, 6)
print("Your average compression ratio is:", round(compression_ratio, 3), "which results in a grade of:", get_grade(compression_ratio))

tension_ratio = calc_ratio("tension", "bridge_test_output.csv", 8, 9)
print("Your average tension ratio is:", round(tension_ratio, 3), "which results in a grade of:", get_grade(tension_ratio))

print("Your final score is:", calc_score(compression_ratio, tension_ratio, 0))
