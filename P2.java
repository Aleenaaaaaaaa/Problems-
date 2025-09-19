import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        int sum=0;
        while(N!=0)
        {
            
            int rev=N % 10;
            sum=sum + rev;
            N=N / 10;
        }
        System.out.println(sum);
    }
}
