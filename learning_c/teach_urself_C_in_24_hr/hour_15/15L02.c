/* 15L02.c: Functions with no arguments */
#include <stdio.h>
#include <time.h>

void GetDateTime(void);

main()
{
	printf("Before the GetDateTime() function is called.\n");
	GetDateTime();
	printf("After the GetDateTime() function is called.\n");
	return 0;
}
/* GetDateTime() definintion */
void GetDateTime(void)
{
	time_t now;

	printf("Within GetDateTime().\n");
	time(&now);
	printf("Current date and time is: %s\n",
		asctime(localtime(&now)));
}
/* The purpose of the program in 15L02.c is to show you how .to declare and
call a function without passing arguments */