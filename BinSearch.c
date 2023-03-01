#include <stdio.h>
#define SIZE 10
int binary_search(int list[], int n, int key);

int main(){
    int key;
    key=0;
    int grade[SIZE]={0, 8, 19, 33, 57, 77, 78, 89, 92, 94};

    return 0;
}

int binary_search(int list[], int n, int key){
    int low, high, middle;
    low=0;
    high=n-1;

    while(low<=high){
        middle=(low+high)/2;
        if(key==list[middle])
            return middle;
        else if(key>list[middle])
            low=middle+1;
        else
            high=middle-1;
    }

    return -1;
}