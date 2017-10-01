// CppFundamentals.cpp : Defines the entry point for the console application.
//

#include "stdafx.h" // ???  must be first...
#include <iostream> // necessary for cout, etc.
#include <iomanip>
#include <string>

using namespace std; // alternative to using std::cout, etc., for everytime you use something from the std library

// Functions // Must be declared before they are used in C++, like in JS, unlike in Java

// a fxn can be declared with a signature alone, and define at the end of the file.

int fxnHeader(int, string); // this must be define somewhere to be used, and this declaration is usually in a header file.

int addition(int a, int b) {
	return a + b;
}

void ptrDouble(int* a) {
	*a = *a * 2;
}

void refDouble(int& a) {
	a *= 2;
}

int divide(int a, int b = 2) {
	// fxn with a defalt parameter
	return 1;
}

int main()
{
	// Data types

	char letter;
	int x;

	letter = 'x';
	cout << "The size of the char is " << sizeof(char) << endl;
	// char, 1 byte on MS VC++, can be different on different architectures
	// bool, 1
	// int, 4
	// float, 4
	// short, 2
	// long, 4
	// double, 8

	string myString = "hello"; // must include <string>

	cout << myString << endl;

	// Loops

	// for loop
	for (x = 0; x < 5; x++)
	{
		cout << letter << "\t" // tab
			<< int(letter) << "\t" // converts char to ASCII representation 
			<< hex << int(letter) << endl; // converts int to hex representation
		cout << dec; // changes output back to decimal
		letter++;
	}

	// while loop
	while (true) {
		//do something here
		break;
	}

	// do while loop
	do {
		// do something here
		break;
	} while (true);

	// enhanched for loop (range-based for loop)
	int myArr[] = { 3,4,5 }; // brackets are not after type, like in Java
	for (int x : myArr) {
		cout << "x: " << x << endl;
	}


	// Conditionals

	// if else
	int number = 4;
	if (number < 5) {
		cout << number << " is less than 5" << endl;
	}
	else
	{
		// do something else
	}

	// switch case
	switch (number) {
	case 1:
		cout << "first" << endl;
		break;
	case 4:
		cout << "fourth" << endl;
		break;
	}

	// ternary operator

	bool myBool = false;

	int y = myBool ? 1 : 0;

	cout << y << endl;

	// Function calls
	int ans = addition(4, 6);
	cout << ans << endl;
	
	int testInt = 7;
	int* test = &testInt;

	cout << "test: " << *test << endl;
	ptrDouble(&testInt); // passing in address of testInt (fxn takes a ptr as argument); value is changed outside of fxn scope
	ptrDouble(test); // passing in ptr to testInt to same fxn, same result
	cout << "test after: " << *test << endl;

	int int1 = 8;
	int &int2 = int1; // binding int2 to int1, changing either will change the other

	int1 += 4;
	cout << int2 << endl; // 12

	refDouble(int1);
	cout << int2 << endl; // 24 

	// arguments may be passed by reference in order to use less space and time,
	// but the fxn can then change the value of the original variable.
	// if this is not desired, make the parameters const
	// e.g. string concatenate (const string& a, const string& b)
	//		{ return a+b;}


	system("pause");
    return 0; // returning 0 from main indicates a success
}



// Classes ///

class Rectangle {
	int width, height;
public:								// access specifier/modifier; all members can be grouped so that they dont all have to specify access
	Rectangle(int, int); // declaring a constructor, must be defined (can be defined here or elsewhere with Rectangl::Rectangle(int a, int b){}
	// Constructors can be overloaded as in Java

	// Possible constructor
	Rectangle(int x, double y) : width(x), height(y) { } //uses : and () for member initialization through the constructor

	void set_values(int, int);		// standard to only use method headers, and define the methods elsewhere
	int area() { return width*height; }
};

void Rectangle::set_values(int x, int y) {  // defining the method that was declared in the class
	width = x; // does not use the "this" keyword
	height = y;
}

/*
int main() {
	Rectangle rect; // New keyword is not used to instantiate an object, it would be used when declaring a pointer
	rect.set_values(3, 4);
	cout << "area: " << rect.area();
	return 0;

	// if creating an object with parameters for the constructor, use Rectangle rect(5,4), but if using the default constructor, do not use ()


	}
*/
