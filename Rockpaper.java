import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) {
        String[] choices = {"rock", "paper", "scissors"};
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        System.out.print("Enter rock, paper, or scissors: ");
        String user = sc.next().toLowerCase();
        String comp = choices[rand.nextInt(3)];

        System.out.println("Computer chose: " + comp);

        if (user.equals(comp)) {
            System.out.println("It's a tie!");
        } else if ((user.equals("rock") && comp.equals("scissors")) ||
                   (user.equals("paper") && comp.equals("rock")) ||
                   (user.equals("scissors") && comp.equals("paper"))) {
            System.out.println("You win!");
        } else {
            System.out.println("Computer wins!");
        }

        sc.close();
    }
}
