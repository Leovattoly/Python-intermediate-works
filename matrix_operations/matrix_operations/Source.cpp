#include <iostream> 

using namespace std;

#define N 4 

// This function multiplies  
// mat1[][] and mat2[][], and  
// stores the result in res[][] 
void multiply(int mat1[][N],
	int mat2[][N],
	int res[][N])
{
	int i, j, k;
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
		{
			res[i][j] = 0;
			for (k = 0; k < N; k++)
				res[i][j] += mat1[i][k] *
				mat2[k][j];
		}
	}
}
// This function adds A[][] and B[][], and stores  
// the result in C[][]  
void add(int A[][N], int B[][N], int C[][N])
{
	int i, j;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = A[i][j] + B[i][j];
}

// This function stores transpose of A[][] in B[][] 
void transpose(int A[][N], int B[][N])
{
	int i, j;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			B[i][j] = A[j][i];
}

// This function substract A[][] and B[][], and stores  
// the result in C[][]  
void substract(int A[][N], int B[][N], int C[][N])
{
	int i, j;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++)
			C[i][j] = A[i][j] - B[i][j];
}
// Driver Code 
int main()
{
	int i, j;
	int res[N][N]; // To store result 
	int res2[N][N]; // To store result 

	int A[N][N] = { {1, 1, 1, 1},
					  {2, 2, 2, 2},
					  {3, 3, 3, 3},
					  {4, 4, 4, 4} };

	int B[N][N] = { {1, 1, 1, 1},
					  {2, 2, 2, 2},
					  {3, 3, 3, 3},
					  {4, 4, 4, 4} };
	int C[N][N] = { {1, 1, 1, 1},
					  {2, 2, 2, 2},
					  {3, 3, 3, 3},
					  {4, 4, 4, 4} };

	transpose(C, res);

	multiply(B, res, res2);
	transpose(A, res);
	add(res, res2, res);
	
	cout << "Result matrix D is \n";
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
			cout << res[i][j] << " ";
		cout << "\n";
	}
	add(res, B, res);
	transpose(res, res2);
	multiply(C, res2, res);
	substract(res, A, res2);

	cout << "\nResult matrix E is \n";
	for (i = 0; i < N; i++)
	{
		for (j = 0; j < N; j++)
			cout << res2[i][j] << " ";
		cout << "\n";
	}



	return 0;
}