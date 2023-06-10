// Monk and Inversions
// Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size N*N 
//  for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells {{(i,j),(p,q)}} 
//  such that M[i][j] >M[p][q] & i<=p & j<=q
// .
// Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.
   

#include <iostream>
using namespace std;

int main()
{

	int t;
	cin >>t;

		for(int i=0; i<t; i++)
		{
			int size;
			cin >> size;
			int r = size;
			int c = size;
			int arr[r][c];

			for(int j=0; j<r; j++)
			{
				for(int k=0; k<c; k++)
				{
					cin >> arr[j][k];
				}
			}


			int count = 0;
			for(int j=0; j<r; j++)
			{
				for(int k=0; k<c; k++)
				{
					for(int l=j; l<r; l++)
					{
						for(int m=k; m<c; m++)
						{
							if(arr[j][k]>arr[l][m])
							{       
								count++;
							}
						}
					}
				}
			}
			cout << count << endl;
		} 
	return 0;
}
