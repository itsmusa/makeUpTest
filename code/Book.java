import java.util.Arrays;

// Total for Class: 25 Marks
public class Book {
	private String title;
	private String author;
	private String category;
	private String isbn;
	private double price;
	private int[] sales = new int[12];
	
	// 5 Marks
	public Book2(String title, String author, String category, String isbn, double price) {
		// TO-DO
	}
	
	public String getCategory() {
		return category;
	}
	
	public String getISBN() {
		return isbn;
	}
	
	// 3 Marks
	public void setSales(int month, int count) {
		// TO-DO
	}
	
	// 3 Marks
	public double getRevenue(int month) {
		// TO-DO
	}
	
	// 7 Marks
	public double getYearRevenue() {
		// TO-DO
	}
	
	// 7 Marks
	public String toString() {
		// TO-DO
	}
}
