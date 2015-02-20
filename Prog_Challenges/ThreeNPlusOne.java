import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main
{
	public static final int ARR_LEN = 3000000;
	static int[] length = new int[ARR_LEN];
	public static void main(String[] args) throws IOException
	{
		//Get the input
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String line = null;
		while((line = br.readLine()) != null)
			sb.append(line).append(" ");
		StringTokenizer st = new StringTokenizer(sb.toString());
		
		//Initialize the array
		for(int i = 0; i < ARR_LEN; i++)
			length[i] = 0;
		length[1] = 1;
		length[2] = 2;
		
		//Limits of computation
		while(st.hasMoreTokens())
		{
			int a, b, upper, lower;
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			upper = a > b? a : b;
			lower = a < b? a : b;
			int max = 0; // Compute the max cycle length
			int temp;
			for(int i = lower; i <= upper; i++)
			{
				//System.out.println("ComputeCycleLength (" + i + ")");
				temp = computeCycleLength2(i);
				max = temp > max? temp : max;
			}
			System.out.println(a + " " + b + " " + max);
			//System.out.println(Arrays.toString(length));
		}
		System.exit(0);
	}
	
	public static int computeCycleLength(int n)
	{
		if(n < ARR_LEN)
		{
			if(length[n] != 0)
				return length[n];
			else
			{
				int tmp, next;
				if(n % 2 == 0)
					next = n / 2;
				else 
					next = 3 * n + 1;
				tmp = 1 + computeCycleLength(next);
				if(next > ARR_LEN)
					return tmp;
				else
				{
					length[next] = tmp;
					return tmp;
				}
			}
		}
		else
		{
			int tmp, next;
			if(n % 2 == 0)
				next = n / 2;
			else 
				next = 3 * n + 1;
			tmp = 1 + computeCycleLength(next);
			if(next > ARR_LEN)
				return tmp;
			else
			{
				length[next] = tmp;
				return tmp;
			}
		}
	}
	
	public static int computeNext(int n)
	{
		int tmp, next;
		if(n % 2 == 0)
			next = n / 2;
		else 
			next = 3 * n + 1;
		tmp = 1 + computeCycleLength(next);
		if(next > ARR_LEN)
			return tmp;
		else
		{
			length[next] = tmp;
			return tmp;
		}
	}
	
	public static int computeCycleLength2(int n)
	{
		if(n < ARR_LEN && length[n] != 0)
		{
			//System.out.println("    if : ComputeCycleLength(" + n + ")");
			return length[n];
		}
		else
		{
			//System.out.println("    else : ComputeCycleLength(" + n + ")");
			int nxt, tmp;
			if(n % 2 == 0)
				nxt = n / 2;
			else
				nxt = 3 * n + 1;
			tmp =  1 + computeCycleLength2(nxt);
			if(n < ARR_LEN)
			{	
				//System.out.println("Write at : " + nxt);
				length[n] = tmp;
			}
			return tmp;
		}
	}
}
