import java.util.Scanner;

public class A {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		
		long m = sc.nextLong();
		long n = sc.nextLong();
		int t = sc.nextInt();
		
		long c = 1;
		switch(t){
			case 1: //O(n!)
				for(int i = 1; i <= n; i++){
					c *= i;
					if(c > m || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				}
				System.out.println("AC");
				System.exit(0);
				break;
			case 2: //2^n
				for(int i = 0; i < n; i++){
					c *= 2;
					if(c > m  || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				}
				System.out.println("AC");
				System.exit(0);
				break;
			case 3:
				for(int i = 0; i < 4; i++){
					c *= n;
					if(c > m || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				}
				System.out.println("AC");
				System.exit(0);
				break;
			case 4:
				for(int i = 0; i < 3; i++){
					c *= n;
					if(c > m  || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				}
				System.out.println("AC");
				System.exit(0);
				break;
			case 5:
				for(int i = 0; i < 2; i++){
					c *= n;
					if(c > m || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				}
				System.out.println("AC");
				System.exit(0);
				break;
			case 6:
				double f = n * (Math.log(n)/Math.log(2));
				long i = 2;
				int i2 = 1;
				while(i < n){
					i*=2;
					i2++;
				}
				c *= i2;
					
					if(f > m || c < 0){
						System.out.println("TLE");
						System.exit(0);
					}
				
				System.out.println("AC");
				System.exit(0);
				break;
			case 7:
				c = n;
				if(c > m || c < 0){
					System.out.println("TLE");
					System.exit(0);
				}
				
				System.out.println("AC");
				System.exit(0);
				break;
		}
	}
}
