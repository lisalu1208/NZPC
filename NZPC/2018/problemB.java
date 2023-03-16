/*
Natalie was a little girl who lovedto organise hertoys.Her favourite game was to line up her toys in alphabetical order by their namethen pair them up the first with the last, the second with the second to last etc.For example, one set of toys wasan ant, a bee, a yak and a zebra.She paired Ant and Zebra, Bee and Yak.Your problem is to assist Jane in ordering toys in the sameway when she goes to a friend’s house–she just loves order so much!Given  a  listof  toys,  order  them  so  that  the  one  with thename  which comes  firstalphabetically is put with the one which comes last alphabetically, the second with the second last and so on until all the toys have been paired.  If there is an odd number of toys, the one in the middle must be displayed on its own after all the pairs.

Input:
The first line of input will be a positive integer, T,which is not greater than 20.  This tells you how many toysthere are at this friend’s house.  Then there are Tlines eachlisting a toy. Toynameswill not be more than 12characters long, may contain spaces and will all begin with a capital letter. They will be not be listed in any particular order.

Output:
Output  should  consist of  the pairs  of toys,  each  pair  on  a  separate  line.  The first  in each pair should be the toywith the name which comes firstalphabetically. The pair should  be  separated  by  a  comma.  If  there  is  an  odd  number  of toys,  the  last  listed shouldnot have a comma following it.
The pairs must be listed in alphabetical order of the first toy of the pair
*/

import java.util.*;
public class problemB{
    public static void main(String[] args) {
        ArrayList<String> toyList = new ArrayList<String>();
        Scanner sc = new Scanner(System.in);
        try{
            int numToys = Integer.parseInt(sc.nextLine());
            if (numToys > 20) {
                System.out.println("The number of toys cannot be greater than 20.");
                System.exit(0);
            }
            for (int i = 1; i <= numToys; i++){
                String toyName = sc.nextLine();
                if (toyName.length() > 12 ){
                    System.out.println("Invalid Toy Name");
                    System.exit(0);
                }
                toyName = toyName.substring(0, 1).toUpperCase() + toyName.substring(1);
                toyList.add(toyName);
            }
            Collections.sort(toyList);
            for (int i = 0; i <= toyList.size()/2; i++){
                if (toyList.get(i) != toyList.get(toyList.size()-1-i)){
                    System.out.println(toyList.get(i) +", "+toyList.get(toyList.size()-1-i));
                }
                else{
                    System.out.println(toyList.get(i));
                }
            }
        }
        catch (Exception ex){
            ex.printStackTrace();
        }
    }
}