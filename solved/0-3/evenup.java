import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solitaire {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int cardsLeft = 0;
		
		ArrayList<Integer> consecutiveNums = new ArrayList<Integer>();
		
		boolean even = Integer.parseInt(st.nextToken()) % 2 == 0 ? true : false;
		int consec = 1;
		
		for(int i = 1; i < n; i++){
			if((Integer.parseInt(st.nextToken()) % 2 == 0) == even){
				consec++;
			}else{
				even = !even;
				cardsLeft += consec % 2;
				consecutiveNums.add(consec % 2);
				consec = 1;
			}
		}
		cardsLeft += consec % 2;
		consecutiveNums.add(consec % 2);
		
		for(int i = 0; i < consecutiveNums.size(); i++){
			if(consecutiveNums.get(i) == 0){
				int dl = 0;
				int dr = 0;
				while(true){
					while(i+dr+1 < consecutiveNums.size() && consecutiveNums.get(i+dr) == 0){
						dr++;
					}
					while(i-dl-1 >= 0 && consecutiveNums.get(i-dl) == 0){
						dl++;
					}
					if((dr + dl) % 2 == 0 && consecutiveNums.get(i-dl) == 1 && consecutiveNums.get(i+dr) == 1){
						consecutiveNums.set(i-dl, 0);
						consecutiveNums.set(i+dr, 0);
						cardsLeft -= 2;
						if(cardsLeft <= 0){
							System.out.println(0);
							System.exit(0);
						}
					}else{
						break;
					}
				}
			}
		}
		System.out.println(cardsLeft);
	}
}
