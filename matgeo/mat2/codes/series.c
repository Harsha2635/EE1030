#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<sys/socket.h>
#include "libs/matfun.h"
#include "libs/geofun.h"
int main(){
	double **A,**B,**C;
	float mag;
	A = createMat(2,1);
	B = createMat(2,1);
	C = createMat(2,1);
	A[0][0]=-5;
	A[1][0]=0;
	B[0][0]=0;
	B[1][0]=12;
	C[0][0]=A[0][0]+B[0][0];
	C[1][0]=A[1][0]+B[1][0];
	FILE *file =fopen("output.dat","w");
	if (file == NULL) {
		printf("Error opening file!\n");
		return 1;
	}
	mag = sqrt(C[0][0]*C[0][0]+C[1][0]*C[1][0]);
	fprintf(file,"%f",mag);
	fclose(file);
	freeMat(A,2);
	freeMat(B,2);
	return 0;
}
