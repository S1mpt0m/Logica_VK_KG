#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void shell(int* items, int count) {
    int i, j, gap, k;
    int x, a[5] = { 9, 5, 3, 2, 1 };
    for (k = 0; k < 5; k++) {
        gap = a[k];
        for (i = gap; i < count; ++i) {
            x = items[i];
            for (j = i - gap; x < items[j] && j >= 0; j = j - gap)
                items[j + gap] = items[j];
            items[j + gap] = x;
        }
    }
}

void qs(int* items, int left, int right) {
    int i, j, x, y;
    i = left; j = right;
    x = items[(left + right) / 2];
    do {
        while (items[i] < x && i < right) i++;
        while (x < items[j] && j > left) j--;
        if (i <= j) {
            y = items[i];
            items[i] = items[j];
            items[j] = y;
            i++; j--;
        }
    } while (i <= j);
    if (left < j) qs(items, left, j);
    if (i < right) qs(items, i, right);
}

void print_time(const char* name, clock_t start, clock_t end) {
    printf("%s took %f seconds\n", name, (double)(end - start) / CLOCKS_PER_SEC);
}
int compare(const int* i, const int* j)  // qsort
{
    return *i - *j;
}
int main() {
    const int SIZE = 60000;
    int random_array[SIZE], sorted_array[SIZE], reversed_array[SIZE], mixed_array[SIZE];

    for (int i = 0; i < SIZE; ++i) {
        random_array[i] = rand() % SIZE;
        sorted_array[i] = i;
        reversed_array[i] = SIZE - i;
        mixed_array[i] = (i < SIZE / 2) ? i : SIZE - i;
    }

    clock_t start, end;

    // Shell Sort
    start = clock();
    shell(random_array, SIZE);
    end = clock();
    print_time("Shell Sort on Random Array", start, end);

    start = clock();
    shell(sorted_array, SIZE);
    end = clock();
    print_time("Shell Sort on Sorted Array", start, end);

    start = clock();
    shell(reversed_array, SIZE);
    end = clock();
    print_time("Shell Sort on Reversed Array", start, end);

    start = clock();
    shell(mixed_array, SIZE);
    end = clock();
    print_time("Shell Sort on Mixed Array", start, end);

    // Quick Sort
    start = clock();
    qs(random_array, 0, SIZE - 1);
    end = clock();
    print_time("Quick Sort on Random Array", start, end);

    start = clock();
    qs(sorted_array, 0, SIZE - 1);
    end = clock();
    print_time("Quick Sort on Sorted Array", start, end);

    start = clock();
    qs(reversed_array, 0, SIZE - 1);
    end = clock();
    print_time("Quick Sort on Reversed Array", start, end);

    start = clock();
    qs(mixed_array, 0, SIZE - 1);
    end = clock();
    print_time("Quick Sort on Mixed Array", start, end);

    start = clock();
    qsort(random_array, SIZE, sizeof(int),( int(*)(const void*, const void*)) compare);
    end = clock();
    print_time("Qsort on random Array", start, end);

    start = clock();
    qsort(sorted_array, SIZE, sizeof(int), (int(*)(const void*, const void*)) compare);
    end = clock();
    print_time("Qsort on sorted Array", start, end);

    start = clock();
    qsort(reversed_array, SIZE, sizeof(int), (int(*)(const void*, const void*)) compare);
    end = clock();
    print_time("Qsort on reversed Array", start, end);

    start = clock();
    qsort(mixed_array, SIZE, sizeof(int), (int(*)(const void*, const void*)) compare);
    end = clock();
    print_time("Qsort on mixed Array", start, end);

    return 0;
}
