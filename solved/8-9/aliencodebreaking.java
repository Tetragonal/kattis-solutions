import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {

    public static int X;
    public static int N = 43;
    public static String ENC;

    public static final int MOD = (int) Math.pow(2,20);
    public static final int B = 10;
    public static final int B2 = 27;
    public static final BigInteger B_BIG = new BigInteger(""+B);

    public static final String ALPHABET = "ABCCDFGHIJKLMNOPQRSTUVWXYZ ";
    public static final int CACHE_NUM = 500;

    public static ArrayList<Long> values = new ArrayList<>();
    public static ArrayList<Long> values_cache = new ArrayList<>();
    public static ArrayList<Long> grid = new ArrayList<>();

    public static ArrayList<BigInteger> fastIntegerOutput(BigInteger a){
        ArrayList<BigInteger> ret = new ArrayList<>();
        if(a.compareTo(B_BIG) == -1){
            ret.add(a);
            return ret;
        }
        else{
            //BigInteger k = new BigInteger(""+Math.ceil(logBigInteger(a)));
            return ret;
        }
    }

    public static int encToOffset(char c){
        if(c == ' '){
            return 26;
        }
        return (c - 'A');
    }

    public static char charToAlphabet(char c, int offset){
        int conv;
        if(c >= '0' && c <= '9'){
            conv = c - '0';
        }
        else{
            conv = c - 'a' + 10;
        }
        conv = (conv + offset) % B2;
        if(conv == 26) return ' ';
        return (char)(conv + 'A');

    }

    public static BigInteger fastIntegerInput(String s){
        ArrayList<BigInteger> l = new ArrayList<>();
        for(int i = s.length()-1; i >= 0; i--){
            l.add(new BigInteger(""+Character.getNumericValue(s.charAt(i))));
        }
        BigInteger b = B_BIG;
        while(l.size() > 1){
            if(l.size() % 2 == 1){
                l.add(new BigInteger("0"));
            }
            ArrayList<BigInteger> l2 = new ArrayList<>();
            for(int i = 0; i < l.size()/2; i++){
                BigInteger x = l.get(2*i);
                BigInteger y = l.get(2*i+1);
                l2.add(x.add(b.multiply(y)));
            }
            b = b.pow(2);
            l = l2;
        }
        return l.get(0);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        N = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        ENC = in.readLine();

        long a = 0;
        for(int i = 0; i < MOD; i++){
            a = (a * 33 + 1) % MOD;
            values.add(a);
        }

        for(int i = 0; i < X; i++){
            long sum = 0;
            for(int j = 0; j < CACHE_NUM; j++){
                sum += values.get((i+j*X) % MOD);
            }
            values_cache.add(sum);
        }

        for(int i = X; i < MOD; i++){
            values_cache.add(
                    values_cache.get(i-X)
                    - values.get(i-X)
                    + values.get((i + (CACHE_NUM - 1) * X) % MOD)
            );
        }

        for(int i = 0; i < values_cache.size(); i++){
            values_cache.set(i, values_cache.get(i) % MOD);
        }

        for(int col = 0; col < X; col++){
            long sum = 0;
            for(long i = 0; i < X/CACHE_NUM; i++){
                long tmp = (i * CACHE_NUM) % MOD;
                tmp = ((tmp * X) + col) % MOD;
                sum += values_cache.get((int)tmp);
            }
            for(int i = X/CACHE_NUM*CACHE_NUM; i < X; i++){
                sum += values.get((int)(((long)i*X+col) % MOD));
            }
            grid.add(sum % MOD);
        }

        StringBuilder sb = new StringBuilder();
        for (long s : grid)
        {
            sb.append(""+s);
        }

        String s = sb.toString();

        BigInteger b = fastIntegerInput(s);

        String conv = b.toString(B2);

        sb = new StringBuilder();
        for(int i = 0; i < conv.length() && i < N; i++){
            sb.append(charToAlphabet(conv.charAt(i), encToOffset(ENC.charAt(i))));
        }

        String ans = sb.toString();
        System.out.println(ans);
    }
}
