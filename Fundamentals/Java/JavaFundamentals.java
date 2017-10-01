
public class Fundamentals {

	public static void main(String[] args) {

		///////////// Loops /////////////////

		for (int i = 0; i < 10; i++) { // for loop
			int k = 4; // local variable
		}

		do {
			// do while loop
		} while (true);

		while (true) {
			// while loop
		}

		int[] myArr = { 1, 4, 8, 9 }; // array declaration and assignment
		int[] myArr2 = new int[4]; // alternate way to initialize an array
		myArr2[0] = 1;

		for (int element : myArr) {
			// loop through each element of an array (enhanced for loop)
		}
		//////////////////////////////////////////
		///////// Conditionals ///////////////////
		if (true) { // if/else

		} else {

		}

		switch (key) { // switch case
		case value:

			break;

		default:
			break;
		}

		int y = 5;
		String x = y == 4 ? "okay" : "not okay"; // ternary operator

		//////////////////////////////////////
		////////////// Instantiate an object /////////////////////
		myClass myInstance = new myClass("Andrew"); // Instantiating a class
													// using the specifying
													// constructor.
	}

	////////// Functions ///////////////
	public static void printMsg(String msg) { // <access modifier> <static?>
												// <return type>
												// <name>(<parameter
												// type><parameter name>)
		System.out.println(msg);
	}
}

///////////// Classes ///////////////////
class myClass {

	private static int myInt = 4; // data members should typically be private
	public final char myChar = '5'; // constants can be public without harm.
	private String name;

	// access modifiers: public, private, protected, package protected
	// static vs non-static: static will only be created in memory once, and can
	// be
	// accessed without creating an instance of the class in which it is
	// declared
	// final vs not final: final is a constant and cannot be changed once it is
	// assigned a value
	// final must be assigned a value when it is declared unless it is an
	// instance member of a class,
	// in which case it can, and usually should, be assigned in the constructor.
	// primitive data types: int, boolean, byte, char, short, long, float,
	// double

	myClass() {
		// constructor; called when an object is instantiated, can be
		// overloaded, unlike in JavaScript
		this("Matt"); // calling an overloaded constructor. This is good
						// practice for setting default values
	}

	myClass(String name) {
		this.name = name;
	};
}