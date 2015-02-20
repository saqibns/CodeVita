import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


class Main
{

	public static void main(String[] args) throws IOException
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		String line;
		int count = 0;
		while(m != 0 && n != 0)
		{
			count++;
			int[][] matrix = new int[m][n];
			for(int i = 0; i < m; i++)
			{
				line = br.readLine();
				for(int j = 0; j < n; j++)
				{
					if(line.charAt(j) == '.')
						matrix[i][j] = 0;
					else
						matrix[i][j] = -1;
				}
			}
			fillMatrix(matrix, m, n);
			System.out.println("Field #" + count + ":");
			printMatrix(matrix, m, n);
			System.out.println();
			st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
		}
		System.exit(0);
	}
	
	//Divide the entire process into two sub-parts. One deals with the boundaries.
	//The other deals with the inside sub-matrix
	
	public static void fillMatrix(int[][] matrix, int m , int n)
	{
		//Call boundary method
		operateOnBoundary(matrix, m, n);
		//Call inside method
		operateInside(matrix, m, n);
	}
	
	public static void operateOnBoundary(int[][] matrix, int m, int n)
	{
		topRow(matrix, m, n);
		bottomRow(matrix, m, n);
		leftColumn(matrix, m, n);
		rightColumn(matrix, m, n);
	}
	
	public static void topRow(int[][] matrix, int m, int n)
	{
		//Coordinates for neighbours
				int[] abs = {0, 0, 1, 1, 1};
				int[] ord = {-1, 1, 0, -1, 1};
				
				int[] abs2 = {0, 1, 1};
				int[] ord2 = {1, 0, 1};
				
				//Top Row
				//Top Left Corner
				if(matrix[0][0] == -1)
				{
					for(int i = 0; i < 3; i++)
					{
						if(matrix[abs2[i]][ord2[i]] != -1)
						matrix[abs2[i]][ord2[i]] += 1;
					}
				}
				
				//Mid Cells
				for(int i = 1; i < n - 1; i++)
				{
					if(matrix[0][i] == -1)
					{
							for(int j = 0; j < 5; j++)
							{
								if(matrix[abs[j]][i + ord[j]] != -1)
								matrix[abs[j]][i + ord[j]] += 1;
							}
					}
				}
				
				//Top Right Corner
				abs2 = new int[]{0, 1, 1};
				ord2 = new int[]{-1, 0, -1};
				if(matrix[0][n - 1] == -1)
				{
					for(int i = 0; i < 3; i++)
					{
						if(matrix[abs2[i]][n - 1 + ord2[i]] != -1)
						matrix[abs2[i]][n - 1 + ord2[i]] += 1;
					}
				}
	}

	public static void bottomRow(int[][] matrix, int m, int n)
	{
		//Coordinates for neighbours
		int[] abs = {0, 0, -1, -1, -1};
		int[] ord = {-1, 1, 0, -1, 1};
		
		int[] abs2 = {0, -1, -1};
		int[] ord2 = {-1, 0, -1};
		
		//Bottom Row
		
		if(matrix[m - 1][n - 1] == -1)
		{
			for(int i = 0; i < 3; i++)
			{
				if(matrix[m - 1 + abs2[i]][n - 1 + ord2[i]] != -1)
					matrix[m - 1 + abs2[i]][n - 1 + ord2[i]] += 1;
			}
		}
		
		for(int i = 1; i < n - 1; i++)
		{
			if(matrix[m - 1][i] == -1)
			{
					for(int j = 0; j < 5; j++)
					{
						if(matrix[m - 1 + abs[j]][i + ord[j]] != -1)
							matrix[m - 1 + abs[j]][i + ord[j]] += 1;
					}
			}
		}
		
		abs2 = new int[] {0, -1, -1};
		ord2 = new int[] {1, 0, 1};
		
		if(matrix[m - 1][0] == -1)
		{
			for(int i = 0; i < 3; i++)
			{
				if(matrix[m - 1 + abs2[i]][ord2[i]] != -1)
					matrix[m - 1 + abs2[i]][ord2[i]] += 1;
			}
		}
	}
	
	public static void leftColumn(int[][] matrix, int m, int n)
	{
		//Coordinates for neighbours
		int[] abs = {0, 0, 1, 1, 1};
		int[] ord = {-1, 1, 0, -1, 1};
		
		//Left Column
		
		for(int i = 1; i < m - 1; i++)
		{
			if(matrix[i][0] == -1)
			{
					for(int j = 0; j < 5; j++)
					{
						if(matrix[i + ord[j]][abs[j]] != -1)
							matrix[i + ord[j]][abs[j]] += 1;
					}
			}
		}
	}
	
	public static void rightColumn(int[][] matrix, int m, int n)
	{
		//Coordinates for neighbours
				int[] abs = {0, 0, -1, -1, -1};
				int[] ord = {-1, 1, 0, -1, 1};
				
				//Left Column
				
				for(int i = 1; i < m - 1; i++)
				{
					if(matrix[i][n - 1] == -1)
					{
							for(int j = 0; j < 5; j++)
							{
								if(matrix[i + ord[j]][n - 1 + abs[j]] != -1)
									matrix[i + ord[j]][n - 1 + abs[j]] += 1;
							}
					}
				}
	}
	public static void operateInside(int[][] matrix, int m, int n)
	{
		//Co-ordinates for neighbours
		int[] x_n = {0, 0, -1, -1, -1, 1, 1, 1};
		int[] y_n = {-1, 1, -1, 0, 1, -1, 0, 1};
		for(int i = 1; i < m - 1; i++)
		{
			for(int j = 1; j < n - 1; j++)
			{
				if(matrix[i][j] == -1)
				{
					for(int k = 0; k < 8; k++)
					{
						if(matrix[i + x_n[k]][j + y_n[k]] != -1)
							matrix[i + x_n[k]][j + y_n[k]] += 1;
					}
				}
			}
		}
	}
	
	public static void printMatrix(int[][] matrix, int m, int n)
	{
		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(matrix[i][j] != -1)
					System.out.print(matrix[i][j]);
				else
					System.out.print("*");
				
			}
			System.out.println();
		}
	}

}
