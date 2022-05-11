public class RiddleUser {

	public static void main(String[] args) {
		
		Riddle riddle1 = new Riddle("What is black and white and red all over?", "An embarrassed Zebra.");
		
		System.out.println("Here are 2 Riddles:");
		System.out.println(riddle1.getQuestion());
		
		System.out.println("The Answer to the first riddle is:");
		System.out.println(riddle1.getAnswer());
		
	}
	

}
