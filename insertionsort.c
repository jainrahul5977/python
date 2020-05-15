#include<stdio.h>
int *insertionsort(int * , int);
void main()
{
    int arr[]={ 12,4,433,34,78,2,45,23};
   int  *a=insertionsort(arr , 8);
    for(int i=0;i<8;i++)
    {
        printf("%d   " , *(a+i));
    }

}
int * insertionsort(int * a , int size)
{
    int key;
    for (int j=1;j<size;j++)
    {
        key=a[j]; int i=j-1;
        while( i>=0 && a[i]>key)
        {
            a[i+i]=a[i];
            i--;
        }
        a[i+1]=key;

    }
    return a;
}