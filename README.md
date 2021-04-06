# Efficient-Growth-Chart
Sum of heights of a Growth Chart in O(n) time in Python, full documentation and testing is included.
A growth chart can capture a value that increases over time (e.g. tree height or number of vaccinations administered).

Informally, a growth chart is a non-empty n by n grid where each column is a non-empty tower of 'X' characters topped by '.' characters. The heights of the towers are non-decreasing from left to right (no tower is taller than the tower to its right). We will represent a growth chart using a list of list of strings. A formal data definition is given in the code.

We want to sum the heights of all the towers that are not taller than some threshold. (This could be used to calculate the total compound interest earned on some principal amount of money.)

The function sum_to(GC, threshold) consumes a growth chart GC and non-negative integer threshold. The function returns the sum of the heights of each column with a height that is less than or equal to threshold. The function must run in O(n) time where n is the length of GC.
