/* 10L05.c Adding the break statement */
#include <stdio.h>

main()
{
	int day;

	printf("Please enter a single digit for a day\n");
	printf("(within the range of 1 to 7):\n");
	day = getchar();
	switch (day){
		case '1':
		   printf("Day 1 is Sunday.\n");
		   break;
		case '2':
		   printf("Day 2 is Monday.\n");
		case '3':
                   printf("Day 3 is Tuesday.\n");
		case '4':
                   printf("Day 4 is wednesday.\n");
		case '5':
                   printf("Day 5 is Thursday.\n");
		case '6':
                   printf("Day 6 is Friday.\n");
		case '7':
                   printf("Day 7 is Saturday.\n");
		   break;
		default:
		   printf("The digit is not within the range of 1 to 7.\n");
		   break;
}
return 0;
}
