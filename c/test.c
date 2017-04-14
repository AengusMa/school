#include<stdio.h>
main()
{
	int i,j,k;
	for(i=1;i<=4;i++)
	{
		for(j=1;j<=4;j++)
		{
			if(i>=j)
			{
				k = i+j;
				printf("%d+%d=%d ",i,j,k);
			}
		}
		printf("\n");
	}
}

