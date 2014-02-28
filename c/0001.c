/*
 * Multiples of 3 and 5
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5,
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <stdio.h>

#define UPPER_BOUND 1000


int
sum_of_multiples()
{
	int sum = 0;
	int i = 1;
	int j = 0;
	for (j = 0; j < UPPER_BOUND - 1; j++, i++) {
		if ((i % 3 == 0) || (i % 5 == 0)) {
			sum += i;
		}
	}

	return sum;
}

int
main(int argc, char *argv[])
{
	printf("The sum of multiples is %d.\n", sum_of_multiples());

	return 0;
}
