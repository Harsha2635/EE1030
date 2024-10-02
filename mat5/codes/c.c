#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("data.txt", "w");

    // Ellipse parameters
    double a = 3.0;  // Semi-major axis
    double b = 2.0;  // Semi-minor axis
    double h = 0.0, k = 0.0;  // Center at origin
    double V[2][2] = {{1.0/(a*a), 0}, {0, 1.0/(b*b)}};

    // Line parameters: x/3 + y/2 = 1 -> y = -2/3 * x + 2
    double slope = -2.0 / 3.0;
    double intercept = 2.0;

    // Writing data to the file in a simple format
    fprintf(file, "%.2f\n", a);
    fprintf(file, "%.2f\n", b);
    fprintf(file, "%.2f\n", h);
    fprintf(file, "%.2f\n", k);
    fprintf(file, "%.5f\n%.5f\n", V[0][0], V[0][1]);
    fprintf(file, "%.5f\n%.5f\n", V[1][0], V[1][1]);
    fprintf(file, "%.2f\n", slope);
    fprintf(file, "%.2f\n", intercept);

    fclose(file);
    return 0;
}

