// Implement a circular buffer.

#include <iostream>

class cbuf {
private:
    int* data;
    int read = 0;
    int write = 0;
    int length;
    bool locked = true;

public:
    cbuf(int len) {
        data = new int[len];
        length = len;
    }

    void write_dat(int i) {
        data[write] = i;
        if (locked == false && write == read)
            read++;
        write++;
        if (write == length)
            write = 0;
        if (read == length)
            read = 0;
        locked = false;
    }

    int read_dat() {
        if (locked)
            return NULL;
        int tmp = data[read];
        read++;
        if (read == length)
            read = 0;
        if (read == write)
            locked = true;
        return tmp;
    }

    void print() {
        for (auto i = 0; i < length; i++)
            std::cout << data[i] << " ";
        std::cout << "\n";
    }
};

int main() {
    cbuf MB {cbuf(10)};
    for (auto i = 0; i < 17; i++)
        MB.write_dat(i);
    MB.print();

    std::cout << "\ndata test\n";
    for (auto i = 0; i < 20; i++)
        std::cout << MB.read_dat() << " ";
    std::cout << "\n";
    MB.write_dat(65); MB.write_dat(104);
    MB.print();
    std::cout << MB.read_dat() << "\n";
    std::cout << MB.read_dat() << "\n";
    return 0;
}
