import java.util.Arrays;
import java.util.Scanner;

public class A1Paper {
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		long length = (long)Math.pow(2, 30-1);
		
		long tape = 0;
		
		double ratio = Math.pow(2, -3.0/4) / Math.pow(2, -5.0/4);
		
		int[] has = new int[31];
		int[] needed = new int[31];
		
		for(int i = 1; i < n; i++){
			has[i] = sc.nextInt();
		}
		int[] has2 = Arrays.copyOf(has, has.length);
		//System.out.println(Arrays.toString(has));
		
		needed[0] = 1;
		for(int i = 1; i < n; i++){
			needed[i] = Math.max(0, 2*needed[i-1]-has[i]);
			
			has[i-1] = has[i-1] + has[i]/2;
			has[i] = has[i] % 2;
		}
		
		for(int i = 0; i < n; i++){
			tape += length/Math.pow(ratio, i) * needed[i];
			/*
			if(length/Math.pow(ratio, i-1) * needed[i] != 0){
				System.out.println(i + " " + length/Math.pow(ratio, i-1) / Math.pow(2, 30-1) * Math.pow(2, -3.0/4));
			}
			*/
		}
		
		for(int i = n; i > 0; i--){
			has2[i-1] = has2[i-1] + has2[i]/2;
			has2[i] = has2[i] % 2;
		}
		
		if(has2[0] == 0){
			System.out.println("impossible");
		}else{
			System.out.println(tape / Math.pow(2, 30-1) * Math.pow(2, -3.0/4));
		}
		
		//System.out.println(Arrays.toString(has));
		//System.out.println(Arrays.toString(needed));
	}
}
