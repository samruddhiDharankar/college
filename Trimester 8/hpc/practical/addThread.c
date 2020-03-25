#include<stdio.h>
#include<omp.h>
int a,b,id,result;
scanf("%d",a);
scanf("%d",b);

int main()
{
#pragma omp parallel
	{
	id=omp_get_thread_num();
	if(id==0)
		{
			result+=a*a;	
		}
	else if(id==1)
		{
			result+=b*b;	
		}	
	else if(id==2)
		{
			result+=4*a*b;	
		}	
	else if(id==3)
		{
			result-=b*b*b;	
		}
	}
	printf("RESULT IS:%d",result);
}
