import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class MineSweeperBasic
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
			operateInside(matrix, m, n);
			System.out.println("Field #" + count + ":");
			printMatrix(matrix, m, n);
			
			st = new StringTokenizer(br.readLine());
			m = Integer.parseInt(st.nextToken());
			n = Integer.parseInt(st.nextToken());
			if(m != 0 && n != 0)
			System.out.println();
		}
		System.exit(0);
	}
	
	public static boolean checkBounds(int current, int lower, int upper)
	{
		if(current >= lower && current < upper)
			return true;
		else
			return false;
	}
	
	public static void operateInside(int[][] matrix, int m, int n)
	{
		//Co-ordinates for neighbours
		int[] x_n = {0, 0, -1, -1, -1, 1, 1, 1};
		int[] y_n = {-1, 1, -1, 0, 1, -1, 0, 1};
		int new_x, new_y;
		for(int i = 0; i < m; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(matrix[i][j] == -1)
				{
					for(int k = 0; k < 8; k++)
					{
						new_x = i + x_n[k];
						new_y = j + y_n[k];
						
						if(checkBounds(new_x, 0, m) && checkBounds(new_y, 0, n) && matrix[new_x][new_y] != -1)
							matrix[new_x][new_y] += 1;
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
