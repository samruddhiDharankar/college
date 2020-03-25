#include<stdio.h>
#include<omp.h>

int main()
{
int id;
#pragma omp parallel for
	
	for(int i=0;i<11;i++)
		{
		id =omp_get_thread_num();
		printf("Hello World %d\n",id);
		}
	
}
