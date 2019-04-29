import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class binary {
	static void printAns(char c) {
		if(c == '0') {
			System.out.println("binary");
		}else {
			System.out.println("decimal");
		}
	}
	
	static ArrayList<String> regionMap;
	static int[][] visited;
	static int r, c;
	
	static boolean check(int x, int y, char target) {
		return !(y<0 || x<0 || y>=r || x>=c)
				&& visited[y][x] == 0
				&& regionMap.get(y).charAt(x) == target;
	}
	
	public static void main(String[] args) throws IOException {
		class Point{
			int x, y;
			public Point(int x, int y) {this.x = x; this.y = y;}
		}
		BufferedReader br = new BufferedReader( 
                new InputStreamReader(System.in)); 
		String in = br.readLine();
		r = Integer.parseInt(in.split(" ")[0]);
		c = Integer.parseInt(in.split(" ")[1]);
	
		regionMap = new ArrayList<>();
		for(int i = 0; i < r; i++) {
			regionMap.add(br.readLine());
		}
		
		int n = Integer.parseInt(br.readLine());
	
		visited = new int[r][c];

		for(int i = 1; i <= n; i++) {
			String[] arr = br.readLine().split(" ");
			int y1 = Integer.parseInt(arr[0]) - 1;
			int x1 = Integer.parseInt(arr[1]) - 1;
			int y2 = Integer.parseInt(arr[2]) - 1;
			int x2 = Integer.parseInt(arr[3]) - 1;
			
			if (regionMap.get(y1).charAt(x1) != regionMap.get(y2).charAt(x2)) {
				System.out.println("neither");
				continue;
			}
			
			if(visited[y1][x1] != 0
				|| visited[y2][x2] != 0) {

				if(visited[y1][x1] == 0 || visited[y2][x2] == 0) {
					System.out.println("neither");
				} else if(visited[y1][x1] == visited[y2][x2]) {
					printAns(regionMap.get(y1).charAt(x1));
				} else {
					System.out.println("neither");
				}
			} else {
				char target = regionMap.get(y1).charAt(x1);
				Queue<Point> queue = new LinkedList<Point>();
				visited[y1][x1] = i;
				queue.add(new Point(x1,y1));
				
				while(!queue.isEmpty()) {
					Point p = queue.poll();
					int x = p.x;
					int y = p.y;
					if(check(x+1, y, target)) {
						visited[y][x+1] = i;
						queue.add(new Point(x+1,y));
					}
					if(check(x-1, y, target)) {
						visited[y][x-1] = i;
						queue.add(new Point(x-1,y));
					}
					if(check(x, y-1, target)) {
						visited[y-1][x] = i;
						queue.add(new Point(x,y-1));
					}
					if(check(x, y+1, target)) {
						visited[y+1][x] = i;
						queue.add(new Point(x,y+1));
					}
				}
				if(visited[y2][x2] == 0) {
					System.out.println("neither");
				} else {
					printAns(regionMap.get(y1).charAt(x1));
				}
			}
		}
	
	}
}
