#include <stdio.h>
#include <stdlib.h>

int main(int ac, char *ag[])
{
	int i, j;
	char **str;

	for (i = 0; ag[i]; i++)
	{}

	*str = malloc(100);

	for (j = 0; str[j]; j++)
	{
		str[j] = ag[j];
	}

	printf("la cantidad de carateres es  = %d", j);
        return (0);
}
