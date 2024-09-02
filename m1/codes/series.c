#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>

#include "libs/geofun.h"
#include "libs/matfun.h"
int main(){
double **A,**B,**C ;
double x,y;
A=createMat(2,1);
B=createMat(2,1);
C=createMat(2,1);
A[0][0]=0;
A[1][0]=-35;
B[0][0]=-12;
B[1][0]=0;
C[0][0]=A[0][0]-B[0][0];
C[1][0]=A[1][0]-B[1][0];
FILE *file =fopen("output.dat","w");
if (file==NULL)  {
	printf("Error opening file!\n");
	return 1;
}
x= atan(C[0][0]/C[1][0]);
y= x*(180.0/M_PI);
fprintf(file,"The value of x is %lf\n",x);
fprintf(file,"The value of y is %lf\n",y);
fclose(file);

freeMat(A,2);
freeMat(B,2);
return 0;
}
