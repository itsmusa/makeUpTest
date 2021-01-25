import java.util.*;
import java.io.*;

public class SalesReport {

	// 
	public static void main(String[] args) {
		// Read in book information
		// 20 Marks
		// TO-DO
		
		// Read sales information and insert into book objects
		// 20 Marks
		// TO-DO
		
		// Full report
		// 5 Marks
		// TO-DO
	}

	/* Sort the books in increasing order according to yearly revenue they generated. */
	// 5 Marks
	private static void insertionSort(Book[] books) {
		// TO-DO
	}

	/* Display all books in books array. */
	private static void displayBooks(Book[] books) {
		for(Book book : books)
			System.out.println(book);
	}
	
	/* Get the accumulated year revenue for books within specified category. */
	// 10 Marks
	private static double getRevenueCategory(Book[] books, String category) {
		// TO-DO
	}

	/* Get book that generates the move revenue for the specified month. */
	// 15 Marks
	private static Book mostRevenue(Book[] books, int month) {
		// TO-DO
	}
}
