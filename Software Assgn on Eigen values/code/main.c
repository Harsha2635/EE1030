#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

// Function prototypes
void qr_decomposition(complex double **A, complex double **Q, complex double **R, int rows, int cols);
double complex_norm(complex double *vec, int len);
void matrix_copy(complex double **dest, complex double **src, int rows, int cols);
void transpose_conjugate(complex double **mat, complex double **mat_conj, int rows, int cols);
void identity_matrix(complex double **mat, int size);
void compute_eigenvalues(complex double **A, int size);
void read_matrix(complex double **mat, int size);
void free_matrix(complex double **mat, int rows);
void print_matrix(complex double **mat, int rows, int cols);

int main() {
    int size;

    // Input size of the matrix
    printf("Enter the size of the square matrix: ");
    scanf("%d", &size);

    // Allocate memory for the matrix
    complex double **A = (complex double **)malloc(size * sizeof(complex double *));
    for (int i = 0; i < size; i++) {
        A[i] = (complex double *)malloc(size * sizeof(complex double));
    }

    // Input the matrix
    printf("Enter the elements of the matrix (real and imaginary parts):\n");
    read_matrix(A, size);

    // Compute and display eigenvalues
    compute_eigenvalues(A, size);

    // Free allocated memory
    free_matrix(A, size);

    return 0;
}

void read_matrix(complex double **mat, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            double real, imag;
            printf("Element [%d][%d]:\n", i + 1, j + 1);
            printf("  Real part: ");
            scanf("%lf", &real);
            printf("  Imaginary part: ");
            scanf("%lf", &imag);
            mat[i][j] = real + imag * I;
        }
    }
}

void compute_eigenvalues(complex double **A, int size) {
    // Allocate memory for matrices Q and R
    complex double **Q = (complex double **)malloc(size * sizeof(complex double *));
    complex double **R = (complex double **)malloc(size * sizeof(complex double *));
    complex double **temp = (complex double **)malloc(size * sizeof(complex double *));
    for (int i = 0; i < size; i++) {
        Q[i] = (complex double *)malloc(size * sizeof(complex double));
        R[i] = (complex double *)malloc(size * sizeof(complex double));
        temp[i] = (complex double *)malloc(size * sizeof(complex double));
    }

    const double tolerance = 1e-9;
    const int max_iterations = 100;

    // QR Algorithm
    for (int iter = 0; iter < max_iterations; iter++) {
        qr_decomposition(A, Q, R, size, size);

        // Compute A = R * Q
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                temp[i][j] = 0.0 + 0.0 * I;
                for (int k = 0; k < size; k++) {
                    temp[i][j] += R[i][k] * Q[k][j];
                }
            }
        }
        matrix_copy(A, temp, size, size);

        // Check for convergence
        double off_diag_norm = 0.0;
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i != j) {
                    off_diag_norm += cabs(A[i][j]);
                }
            }
        }
        if (off_diag_norm < tolerance) {
            break;
        }
    }

    // Output eigenvalues
    printf("Eigenvalues:\n");
    for (int i = 0; i < size; i++) {
        printf("  Eigenvalue %d: %.5f + %.5fi\n", i + 1, creal(A[i][i]), cimag(A[i][i]));
    }

    // Free allocated memory
    free_matrix(Q, size);
    free_matrix(R, size);
    free_matrix(temp, size);
}

void qr_decomposition(complex double **A, complex double **Q, complex double **R, int rows, int cols) {
    identity_matrix(Q, rows);
    matrix_copy(R, A, rows, cols);

    for (int k = 0; k < cols; k++) {
        complex double x[rows - k];
        for (int i = k; i < rows; i++) {
            x[i - k] = R[i][k];
        }

        double norm_x = complex_norm(x, rows - k);
        x[0] += (creal(x[0]) >= 0) ? norm_x : -norm_x;

        norm_x = complex_norm(x, rows - k);
        for (int i = 0; i < rows - k; i++) {
            x[i] /= norm_x;
        }

        for (int j = k; j < cols; j++) {
            complex double s = 0.0;
            for (int i = k; i < rows; i++) {
                s += R[i][j] * conj(x[i - k]);
            }
            for (int i = k; i < rows; i++) {
                R[i][j] -= 2.0 * s * x[i - k];
            }
        }

        for (int i = 0; i < rows; i++) {
            complex double s = 0.0;
            for (int j = k; j < rows; j++) {
                s += Q[i][j] * conj(x[j - k]);
            }
            for (int j = k; j < rows; j++) {
                Q[i][j] -= 2.0 * s * x[j - k];
            }
        }
    }
}

double complex_norm(complex double *vec, int len) {
    double sum = 0.0;
    for (int i = 0; i < len; i++) {
        sum += cabs(vec[i]) * cabs(vec[i]);
    }
    return sqrt(sum);
}

void identity_matrix(complex double **mat, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            mat[i][j] = (i == j) ? 1.0 + 0.0 * I : 0.0 + 0.0 * I;
        }
    }
}

void matrix_copy(complex double **dest, complex double **src, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

void free_matrix(complex double **mat, int rows) {
    for (int i = 0; i < rows; i++) {
        free(mat[i]);
    }
    free(mat);
}
