#include <iostream>

void simple(int* arr, int len, int* ret) {
    int num = 1;
    for (auto i = 0; i < len; i++)
        num *= arr[i];
    for (auto i = 0; i < len; i++)
        ret[i] = num/arr[i];
}

int main() {
    int arr[5] {1,2,3,4,5};
    int ret[5] {0,0,0,0,0};
    simple(arr, 5, ret);

    for (auto i : ret)
        std::cout << i << " ";
    std::cout << "\n";
    return 0;
}
