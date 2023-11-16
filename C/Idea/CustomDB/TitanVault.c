#include <stdio.h>
#include <stdlib.h>
#define DONE 0

struct structure{
    short header;
    int data_int;
    double data_double;
};

void DynamicAllocation(int size){
    struct structure* s;
    s = malloc(sizeof(struct structure));

    struct structure* Array = (struct structure*)malloc(sizeof(struct structure) * size);
    
}

int main() {
    DynamicAllocation(5);
   return DONE; 
}
