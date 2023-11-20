#include <stdio.h>
#include <stdlib.h>

#define DONE 0

// 구조체의 멤버는 사용자가 정의
struct structure {
    short header;
    int data_int;
    double data_double;
};

// 메인 데이터베이스 구조체
struct Database {
    struct structure* Array;
    int size;
    int capacity;
};

// 매개 변수 : 메인 데이터베이스와 데이터베이스 크기
void initialize_Database(struct Database* db, int initialCapacity) {
    db -> Array = (struct structure*)malloc(sizeof(struct structure) * initialCapacity);
    db -> size = 0;
    db -> capacity = initialCapacity;
}

// 가변적인 데이터베이스 구현의 핵심 함수
void resize_Database(struct Database* db) {
    db -> capacity *= 2;
    db -> Array = (struct structure*)realloc(db -> Array, sizeof(struct structure) * db -> capacity);
}

// 데이터베이스 내 구조체에 실제 데이터 삽입하는 함수
void add_To_Database(struct Database* db, short header, int data_int, double data_double) {
    if (db -> size == db -> capacity) {
        resize_Database(db);
    }

    struct structure new_structure = {header, data_int, data_double};
    db -> Array[db -> size++] = new_structure;
}

void print_Database(const struct Database* db) {
    printf("Database:\n");
    for (int i = 0; i < db -> size; ++i) {
        printf("structure %d: Header=%d, Data Int=%d, Data Double=%.2f\n", i + 1, db -> Array[i].header,
               db -> Array[i].data_int, db -> Array[i].data_double);
    }
}

void free_Database(struct Database* db) {
    free(db -> Array);
    db -> size = 0;
    db -> capacity = 0;
}

int main() {
    struct Database testDatabase;
    // 메인 데이터베이스와 초기 크기를 인자로 줌 
    initialize_Database(&testDatabase, 5);

    add_To_Database(&testDatabase, 1, 42, 3.14);
    add_To_Database(&testDatabase, 2, 99, 2.718);
    add_To_Database(&testDatabase, 3, 123, 1.618);

    print_Database(&testDatabase);

    free_Database(&testDatabase);

    return DONE;
}
