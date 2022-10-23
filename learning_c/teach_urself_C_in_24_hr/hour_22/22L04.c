/* 22L04.c: Redirecting a standard stream */
#include <stdio.h>

enum {SUCCESS, FAIL,
	STR_NUM = 4};

void StrPrint(char **str);
int ErrorMsg(char *str);

main(void)
{
	char *str[STR_NUM] = {
		"Be bent, and you willl remain straight.",
		"Be vacant, and you will reamin full.",
		"Be worn, and you will remain vew.",
		"--- by Lao Tzu"};
	char filename[]= "LazoTzu.txt";
	int reval = SUCCESS;

	StrPrint(str);
	if (freopen(filename, "w", stdout) == NULL){
		reval = ErrorMsg(filename);
	} else {
		StrPrint(str);
		fclose(stdout);
	}
	return reval;
}
/* function definition */
void StrPrint(char **str)
{
	int i;

	for ( i=0; i<STR_NUM; i++)
		printf("%s\n", str[i]);
}
/* function definition */
int ErrorMsg(char *str)
{
	printf("Cannot open %s.\n", str);
	return FAIL;
}
