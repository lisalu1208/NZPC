/*
problemC:
The Monty Hall problem is explained on Wikipedia as follows:
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others,
goats. You pick a door, say No.1, and the host, who knows what's behind the doors, opens another door, say No.3, which
has a goat. He then says to you, "Do you want to pick door No.2?" Is it to your advantage to switch your choice?

You win whatever is behind the door you choose. Probability theory says that to win the car your best chance is to
switch from your original choice, a theory you are to investigate in this problem.

Input:
The first line of input is a single integer, N (2 <= N <= 10), the number of games which follow. Each game consists of a
single line containing three characters, separated by spaces.
The first character is the door chosen by the contestant, 1, 2 or 3.
The second character is the door behind which is the car, also 1, 2 or 3.
The third character is S or R. S means the user chose to switch to the other unopened door, R that the user remains with
the original door. In the set of games, there will be at least one switch and at least one remain.

Output:
Does the user have a better record (% success) switching doors or remaining with the door originally chosen?
If switching proves the better option, output Switching is better.
If not switching proves the better option, output Switching is worse.
If neither option proves better, output No preference.
 */

import java.util.Scanner;

public class problemC {
    public static int numSwitchSuccess = 0, numSwitch = 0;
    public static int numRemainSuccess = 0, numRemain = 0;
    public static double rateSwitch = 0.0, rateRemain =0.0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
//        int numSwitchSuccess = 0, numSwitch = 0;
//        int numRemainSuccess = 0, numRemain = 0;
//        double rateSwitch = 0.0, rateRemain =0.0;
        try{
            int numGames = Integer.parseInt(sc.nextLine());
            for (int i = 1; i <= numGames; i++){
                String game = sc.nextLine();
                int contestantChoice = Integer.parseInt(game.split(" ")[0]);
                int car = Integer.parseInt(game.split(" ")[1]);
                String SorR = game.split(" ")[2];
                if (SorR.equals("S")){
                    numSwitch++;
                    if(contestantChoice != car){
                        numSwitchSuccess++;
                    }
                    rateSwitch = numSwitchSuccess * 100 / numSwitch;
                }
                else if (SorR.equals("R")){
                    numRemain++;
                    if(contestantChoice == car){
                        numRemainSuccess++;
                    }
                    rateRemain = numRemainSuccess * 100 / numRemain;
                }
            }
            if (rateRemain > rateSwitch) {
                System.out.println("Switching is worse");
            }
            else if (rateRemain < rateSwitch){
                System.out.println("Switching is better");
            }
            else{
                System.out.println("No preference");
            }
        }
        catch (Exception ex){
            ex.printStackTrace();
        }
    }
}
