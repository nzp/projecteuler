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

int *
get_multiples()
{
	/* Has to be static so that the caller can access it.
	 * Another way is for the caller to declare the array, or to
	 * malloc it.  This is the simplest for this purpose.
	 */
	static int multiples[UPPER_BOUND - 1];
	int c;
	for (c = 0; c < UPPER_BOUND - 1; c++) {
		multiples[c] = 0;
	}

	int i = 1;
	int j = 0;
	for (j = 0; j < UPPER_BOUND - 1; j++, i++) {
		if ((i % 3 == 0) || (i % 5 == 0)) {
			multiples[j] = i;
		}
	}

	return multiples;
}

int
sum_of_multiples(int *multiples)
{
	int i;
	int sum = 0;
	for (i = 0; i < UPPER_BOUND - 1; i++) {
		sum += multiples[i];
	}

	return sum;
}

int
main(int argc, char *argv[])
{
	int *mults = get_multiples();
	int sum = sum_of_multiples(mults);

	printf("The sum of multiples is %d.\n", sum);

	return 0;
}
