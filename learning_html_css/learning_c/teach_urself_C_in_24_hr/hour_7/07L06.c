/* 07L06.c: Demonstrating neeted loops */
#include <stdio.h>

main()
{
	int i, j;

	for (i=1; i<=3; i++) {	/* outer loop */
	printf(" The start of iteration %d of the outer loop.\n", i);
	for (j=1; j<=4; j++) 	/* inner loop */
	printf("    Iteration %d of the inner loop.\n", j);
	printf("The end kf iteration %d of the outer loop.\n", i);	}
	return 0;
}
