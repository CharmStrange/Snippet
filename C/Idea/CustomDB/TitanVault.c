#include <stdio.h>
#include <stdlib.h>

#define DONE 0

// 구조체의 멤버는 사용자가 정의
struct structure {
    short header;
    int data_int;
    double data_double;
};

struct Database {
    struct structure* Array;
    int size;
    int capacity;
};

void initializeDatabase(struct Database* db, int initialCapacity) {
    db->Array = (struct structure*)malloc(sizeof(struct structure) * initialCapacity);
    db->size = 0;
    db->capacity = initialCapacity;
}

void resizeDatabase(struct Database* db) {
    db->capacity *= 2;
    db->Array = (struct structure*)realloc(db->Array, sizeof(struct structure) * db->capacity);
}

void addToDatabase(struct Database* db, short header, int data_int, double data_double) {
    if (db->size == db->capacity) {
        resizeDatabase(db);
    }

    struct structure newEntry = {header, data_int, data_double};
    db->Array[db->size++] = newEntry;
}

void printDatabase(const struct Database* db) {
    printf("Database:\n");
    for (int i = 0; i < db->size; ++i) {
        printf("Entry %d: Header=%d, Data Int=%d, Data Double=%.2f\n", i + 1, db->Array[i].header,
               db->Array[i].data_int, db->Array[i].data_double);
    }
}

void freeDatabase(struct Database* db) {
    free(db->Array);
    db->size = 0;
    db->capacity = 0;
}

int main() {
    struct Database myDatabase;
    initializeDatabase(&myDatabase, 5);

    addToDatabase(&myDatabase, 1, 42, 3.14);
    addToDatabase(&myDatabase, 2, 99, 2.718);
    addToDatabase(&myDatabase, 3, 123, 1.618);

    printDatabase(&myDatabase);

    freeDatabase(&myDatabase);

    return DONE;
}
