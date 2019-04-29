import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Phone {
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		final class Node{
			boolean die = false;
			Node[] children = new Node[10];
		}
		BufferedReader br = new BufferedReader( 
                new InputStreamReader(System.in)); 

		int T = Integer.parseInt(br.readLine());
		for(int t = 0; t < T; t++) {
			// populate
			ArrayList<String> allNums = new ArrayList<>();
			
			Node root = new Node();
			//read input
			int N = Integer.parseInt(br.readLine());
			for(int i = 0; i < N; i++) {
				Node curr = root;
				String in = br.readLine();
				allNums.add(in);
				for(char c : in.toCharArray()) {
					int num = Integer.parseInt("" + c);
					if(curr.children[num] == null) {
						curr.children[num] = new Node();
					}
					curr = curr.children[num];
				}
				curr.die = true;
			}
			
			//System.out.println("Done");
			//check
			boolean flag = false;
			for(String in : allNums) {
				Node curr = root;
				for(int j = 0; j < in.length()-1; j++) {
					int num = in.charAt(j) - 48;
					if(curr.children[num].die) {
						flag = true;
						break;
					}
					curr = curr.children[num];
				}
				if(flag) break;
			}
			
			if(flag) {
				System.out.println("NO");
			}else {
				System.out.println("YES");
			}
		}
	}
}
