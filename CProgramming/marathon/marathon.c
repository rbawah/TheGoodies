#include <stdio.h>

int main(){

    int miles = 26, yards = 385;
    double kilometers;

    //printf("Enter temp in Fahrenheit - Integer input required:");
    //scanf("%d", &fahrenheit);
    kilometers = 1.609*(miles - yards/1760.0); //impilicitly converted to int data-type 
                                    //despite the literal double 1.8
    printf("\n A marathon is %f kilometers.\n", kilometers);
    return 0;
}