import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] dp = new int[n+1][3];

        StringTokenizer st;
        for (int i=1; i<=n; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            dp[i][0] = Math.max(dp[i-1][1], dp[i-1][2]) + l;
            dp[i][1] = Math.max(dp[i-1][0], dp[i-1][2]) + m;
            dp[i][2] = Math.max(dp[i-1][0], dp[i-1][1]) + r;
        }

        int result = dp[n][0];
        result = (dp[n][1] > result)? dp[n][1] : result;
        result = (dp[n][2] > result)? dp[n][2] : result;

        System.out.println(result);
    }
}