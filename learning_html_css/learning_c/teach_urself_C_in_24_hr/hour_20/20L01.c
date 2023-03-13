/* 20L01.c; Referencing a union */
#include <stdio.h>
#include <string.h>

main(void)
{
	union menu {
		char name[23];
		double price;
	} 	dish;

	printf("The content assigned to the union separately:\n");
	/* reference name */
	strcpy(dish.name, "Sweet and sour chicken");
	printf("Dish Name: %s\n", dish.name);
	/* reference price */
	dish.price = 9.95;
	printf("Dish Price: %5.2f\n", dish.price);

	return 0;
}
