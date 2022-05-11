import java.util.Scanner;

public class InteractiveRiddleUser {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Riddle r = new Riddle("Question", "Answer");
		System.out.println("The Riddle question is: "+r.getQuestion());
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Your Answer is: ");
		String answer = sc.nextLine();
		
		boolean check = answer.equals(r.getAnswer());
		System.out.println("This is "+check);
		
		System.out.println("Correct Answer is: "+r.getAnswer());
		
		sc.close();
	}

}
