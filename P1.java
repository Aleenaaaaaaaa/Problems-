import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt(); // number of integers
        
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            System.out.println(num);
        }
        
        sc.close();
    }
}
