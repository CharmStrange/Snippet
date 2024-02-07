#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int x;
    int y;
} Position;

typedef struct {
    Position ma_position;
    Position hunter_position;
} Maehunter;

Position find_kok() {
    Position kok_position;
    kok_position.x = rand() % 200 - 100;
    kok_position.y = rand() % 200 - 100;
    printf("Kok found at position: (%d, %d)\n", kok_position.x, kok_position.y);
    return kok_position;
}

void chase(Position *ma_position, Position kok_position) {
    // Assume Ma flies towards the kok
    *ma_position = kok_position;
    printf("Ma flying towards the kok...\n");
}

void catch_kok() {
    // Assume Ma catches the kok
    printf("Ma catches the kok!\n");
}

void hunt(Maehunter *maehunter) {
    Position kok_position = find_kok();
    chase(&(maehunter->ma_position), kok_position);
    catch_kok();
}

int main() {
    srand(time(NULL)); // Initialize random seed

    Maehunter maehunter;
    maehunter.ma_position.x = 0;
    maehunter.ma_position.y = 0;
    maehunter.hunter_position.x = 0;
    maehunter.hunter_position.y = 0;

    hunt(&maehunter);

    return 0;
}
