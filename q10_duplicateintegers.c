#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[10] = {5, 9, 0, -11, -1, 5, 17, 8, 117, 5};
    int unq = 10;

    // 5 9 0 -11 -1 17 8 117
    // 8 unique numbers

    // Calculate # of unique numbers by subtracting 1 for
    // every duplicate found.
    for (int i = 0; i < 10; i = i + 1) {
        for (int j = 0; j < i; j++) {
            if (arr[i] == arr[j]) {
                unq -= 1;
                break;
            }
        }
    }
    printf("%d unique numbers\n", unq);

    // Create a new array to contain unique numbers.
    int pos = 0;
    int* dup = malloc(sizeof(int) * 10);

    for (int i = 0; i < unq; i++)
        dup[i] = 0;

    for (int i = 0; i < 10; i++) {
        bool in_arr = false;
        for (int j = 0; j <= pos; j++) {
            if (arr[i] == dup[j])
                in_arr = true;
        }
        if (!in_arr) {
            dup[pos] = arr[i];
            pos++;
        }
    }

    printf("%d %d\n", pos, unq);
    if (pos < unq) {
        dup[pos] = 0;
        pos++;
    }

    for (int i = 0; i < pos; i++)
        printf("%d ", dup[i]);

    return 0;
}
