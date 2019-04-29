import java.util.Scanner;

public class B {
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		int[][] board = new int[4][4];
		boolean[][] marked = new boolean[4][4];
		for(int r = 0; r < 4; r++){
			for(int c = 0; c < 4; c++){
				board[r][c] = sc.nextInt();
			}
		}
		
		int bla = sc.nextInt();
		switch(bla){
			case 0: //left
				for(int i = 0; i < 4; i++){
					for(int r = 0; r < board.length; r++){
						for(int c = 0; c < board[0].length - 1; c++){
							if(board[r][c] == 0 || (board[r][c+1] == board[r][c] && !marked[r][c+1] && !marked[r][c])){
								if(board[r][c+1] == board[r][c] && board[r][c] != 0) marked[r][c] = true;
								else if(board[r][c] == 0){
									marked[r][c] = false;
									marked[r][c+1] = true;
								}
								board[r][c] = board[r][c+1] + board[r][c];
								board[r][c+1] = 0;
							}
						}
					}
				}
				break;
			case 1: //up
				for(int i = 0; i < 4; i++){
					for(int c = 0; c < board[0].length; c++){
						for(int r = 0; r < board.length - 1; r++){
							if(board[r][c] == 0 || (board[r+1][c] == board[r][c] && !marked[r+1][c] && !marked[r][c])){
								if(board[r+1][c] == board[r][c] && board[r][c] != 0) marked[r][c] = true;
								else if(board[r][c] == 0){
									marked[r][c] = marked[r+1][c];
									marked[r+1][c] = false;
								}
								board[r][c] = board[r+1][c] + board[r][c];
								board[r+1][c] = 0;
							}
						}
					}
				}
				break;
			case 2: //right
				for(int i = 0; i < 4; i++){
					for(int r = 0; r < board.length; r++){
						for(int c = board.length - 1; c > 0; c--){
							if(board[r][c] == 0 || (board[r][c-1] == board[r][c] && !marked[r][c-1] && !marked[r][c])){
								if(board[r][c-1] == board[r][c] && board[r][c] != 0) marked[r][c] = true;
								else if(board[r][c] == 0){
									marked[r][c] = marked[r][c-1];
									marked[r][c-1] = false;
								}
								board[r][c] = board[r][c-1] + board[r][c];
								board[r][c-1] = 0;
							}
						}
					}
				}
				break;
			case 3: //down
				for(int i = 0; i < 4; i++){
					for(int c = 0; c < board[0].length; c++){
						for(int r = board[0].length - 1; r > 0; r--){
							if(board[r][c] == 0 || (board[r-1][c] == board[r][c] && !marked[r-1][c] && !marked[r][c])){
								if(board[r-1][c] == board[r][c] && board[r][c] != 0) marked[r][c] = true;
								else if(board[r][c] == 0){
									marked[r][c] = marked[r-1][c];
									marked[r-1][c] = false;
								}
								board[r][c] = board[r-1][c] + board[r][c];
								board[r-1][c] = 0;
							}
						}
					}
				}
				break;
		}
		for(int r = 0; r < board.length; r++){
			for(int c = 0; c < board[0].length; c++){
				System.out.print(board[r][c] + " ");
			}
			System.out.println();
		}
		
	}
}
