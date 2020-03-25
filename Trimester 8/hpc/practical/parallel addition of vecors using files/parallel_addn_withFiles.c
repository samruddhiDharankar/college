#include<stdio.h>
#include<stdlib.h>
#include<omp.h>

void filegenerator(int n, char *str) {
    FILE *fp;
    fp = fopen(str, "w");

    if ( fp == NULL ) { 
        printf(str, "%s file failed to open." ) ; 
    } 
    
    for(int i=0;i<n;i++) {
        int num = rand();
        fprintf(fp,"%d",num);
    }
   fclose(fp);

}

void addition(int n,char *str1, char *str2) {
    int a,b,c;
    char str3[20];
    FILE *fp1,*fp2,*fp3;
    fp1 = fopen(str1,"r");
    fp2 = fopen(str2,"r");
    fp3 = fopen(str3,"w");
    // #pragma omp parallel for 
        for(int i =0;i<n;i++) {
            fscanf(fp1,"%d", &a);
            fscanf(fp2,"%d", &b);
            c = a + b;
            fprintf(fp3,"%d",c);
        }
        printf("%d\t",c);

}


int main() {
    int n;
  
    printf("enter no of elements ");
    scanf("%d",&n);
    filegenerator(n,"abc.txt");
    filegenerator(n,"xyz.txt");
    addition(n,"abc.txt","xyz.txt");

}