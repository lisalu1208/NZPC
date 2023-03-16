/* A small rural bus service wants some data on passenger usage of some of their less popular routes.  They want to be able to use appropriately sized buses and to set the frequency of the service to meet demand. 
From the data provided, you are to work out the total number of passengers carried on the service, and the highest number of passengers on board at any time. 

Input:
The first line of input contains the route number consisting of up to 5 characters (which may include letters). 
The next line contains a single non-negative integer, the number of passengers on the bus when it departed. 
Remaining lines of input consist of two non-negative integers, separated by a space.  This represents the number of passengers who got on, and the number who got off at a stop, in that order.  The last line will contain 0 0.  This line should not be processed.

None of the numeric values will be higher than 80.

Output (Three lines):
Route <route number>: the route number read from the input
Total <passenger total>: the total number of passengers who got on the bus.
Highest <passenger highest>: the maximum number of passengers on the bus at one time.
*/

import java.util.Scanner;

public class BusService {
    public static void main(String[] args) {
        // Declare variables
        String line = "";
        String routeNum = "";
        int passengerNum = 0;
        int maxTotal = 0;
        int total = 0;
        Scanner sc = new Scanner(System.in);
        try{
            // Read in the first line
            line = sc.nextLine();
            if (line.length()>5){
                System.exit(0);
            }
            else{
                routeNum = line;
            }
            // Read in the second line
            line = sc.nextLine();
            try{
                passengerNum = Integer.parseInt(line);
                checkNumber(passengerNum);
                total = passengerNum;
            }
            catch (Exception ex){
                ex.printStackTrace();
            }
            // While it is not the end of the reading
            line = sc.nextLine();
            while (!(line.equals("0 0"))){
                String[] splitArray = line.split(" ");
                if (splitArray.length !=2){
                    System.out.println("Please input valid numbers: <num of passengers got on> <num of passengers got off>");
                    System.exit(0);
                }
                int gotOn = Integer.parseInt(splitArray[0]);
                checkNumber(gotOn);
                passengerNum += gotOn;
                total += gotOn;
                int gotOff = Integer.parseInt(splitArray[1]);
                checkNumber(gotOff);
                total -= gotOff;
                if (total> maxTotal){
                    maxTotal = total;
                }
                line = sc.nextLine();
            }
            System.out.println("Route  "+routeNum);
            System.out.println("Total  "+passengerNum);
            System.out.println("Highest  "+maxTotal);
        }
        catch (Exception ex){
            ex.printStackTrace();
        }
        
    }
    
    public static void checkNumber(int num){
        if (num > 800 || num < 0){
            System.out.println("Please input valid numbes (0 < num <= 800)");
            System.exit(0);
        }
    }
}