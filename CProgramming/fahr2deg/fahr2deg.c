#include <stdio.h>

int main(){

    int fahrenheit, celsius;

    printf("Enter temp in Fahrenheit - Integer input required:");
    scanf("%d", &fahrenheit);
    celsius = (fahrenheit - 32)/1.8; //impilicitly converted to int data-type 
                                    //despite the literal double 1.8
    printf("\n %d fahrenheit is %d celsius.\n", fahrenheit, celsius);
    return 0;
}