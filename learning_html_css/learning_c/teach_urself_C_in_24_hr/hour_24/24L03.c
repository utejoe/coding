/* 24L03.c: The driver file */
#include "24L02.h"     /* include header file */

main(void)
{
	int ch;

	printf("Enter a for adding, d for deleting,\n");
	printf("p for displaying, and q for exit:\n");
	while ((ch=getchar()) != 'q'){
		main_interface(ch);   /* process input from the user */
	}
	
	list_node_free();
	printf("\nBye!\n");

	return 0;
}
