/* 10L06.c: Breaking anninfinite loop */
#include <stdio.h>

main()
{
	int c;

	printf("Enter a character:\n(enter x to exit)\n");
	while (c != 'x') {
	   c = getc (stdin) ;
	   if (c == 'x')
		break;
}
	printf("Break the infinite while loop. Bye!\n");
	return 0;
}
