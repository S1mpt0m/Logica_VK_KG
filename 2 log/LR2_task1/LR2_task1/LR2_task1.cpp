#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void multiplyMatrices(int N, int** a, int** b, int** c) {
    int i, j, r, elem_c;
    clock_t start, end;
    double cpu_time_used;

    start = clock(); // начало отсчета времени

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            elem_c = 0;
            for (r = 0; r < N; r++) {
                elem_c += a[i][r] * b[r][j];
            }
            c[i][j] = elem_c;
        }
    }

    end = clock(); // конец отсчета времени

    cpu_time_used = ((double)(end - start)) / CLOCKS_PER_SEC; // время выполнения в секундах

    printf("Time for matrix multiplication of size %d: %f seconds\n", N, cpu_time_used);
}

int main(void) {
    int Ns[] = { 100, 200, 400, 1000, 2000, 4000, 10000 }; // Размеры матриц, 4000 и 10000 могут быть слишком большими для стека
    int i, j, k, N;

    for (k = 0; k < sizeof(Ns) / sizeof(Ns[0]); k++) {
        N = Ns[k];

        int** a = (int**)malloc(N * sizeof(int*));
        int** b = (int**)malloc(N * sizeof(int*));
        int** c = (int**)malloc(N * sizeof(int*));

        for (i = 0; i < N; i++) {
            a[i] = (int*)malloc(N * sizeof(int));
            b[i] = (int*)malloc(N * sizeof(int));
            c[i] = (int*)malloc(N * sizeof(int));
        }

        // Инициализация матриц a и b
        srand((unsigned int)time(NULL));
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++) {
                a[i][j] = rand() % 100 + 1;
                b[i][j] = rand() % 100 + 1;
            }
        }

        // Умножение матриц
        multiplyMatrices(N, a, b, c);

        // Очистка памяти
        for (i = 0; i < N; i++) {
            free(a[i]);
            free(b[i]);
            free(c[i]);
        }
        free(a);
        free(b);
        free(c);
    }

    return 0;
}
