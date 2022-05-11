package riddle;

public class Riddle {
	
	private String question;
	
	private String answer;

	public Riddle(String q, String a) {
		this.question = q;
		this.answer = a;
	}
	
	public String getQuestion() {
		return this.question;
	}
	
	public String getAnswer() {
		return this.answer;
	}

}
