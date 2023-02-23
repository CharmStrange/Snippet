#include <stdio.h>
#include <math.h>
#define EPSILON 0.0001

double func(double x){
    return //type f(x);
}

void bisection(double a,double b){
    if(func(a)*func(b)>=0){
        printf("NO");
        return;
    }
    
    double c=a;
    while((b-a)>=EPSILON){
        c=(a+b)/2;
        if(func(c)*func(a)<0){
            b=c;
        }
        else{
            a=c;
        }
    }
    
    printf("%lf", c);
}

int main(void){
    double //range a= , b= ;
    bisection(a,b);
    return 0;
}