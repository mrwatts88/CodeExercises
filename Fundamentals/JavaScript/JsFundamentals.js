//// JavaScript declarations ///////

let foo = 1; // block level scope
var bar = 2; // function level scope
const foobar = 3 // constant, block level scope

/////////////////////////////////////////////////////

///// JavaScript data types and data structures //////

let num = 42; // Number (double precision 64-bit; includes +/- Infinity and NaN)
let str = 'foo'; // String (immutable)
let bool = true; // Boolean
let sym = Symbol(); // Symbol ???
let obj = {     // Functions are objects with the additional capability of being callable
    'key1': num,
    'key2': str,
    'key3': bool,
    'key4': sym,
    sym: 'symbols can be used as keys',
    'keyWithFxnValue': ()=>{
        console.log("I'm a function in the value of an object literal")
    }
}

Object.defineProperty(obj, 'key1', { // objects are not enumerable, not configurable, not writable as defaults
    enumerable: false,          // Can also define custom properties, eg. using setters and getters ???
    configurable: false,
    writable: false,
    value: 'static'
  });

Object.keys(obj); // returns the keys of obj in an array.

let arr = [1,3,4]; // Array
let int8arr = new Int8Array(); // Typed arrays
let int16arr = Int16Array.from(arr);

let mySet = new Set(arr); // Set (pass in an iterable; Sets are iterable in insertion order; values may only occur once; Methods: add, clear, delete, entries, forEach, has, keys,values)
// WeakSet (Same as Set, but cannot be enumerated over, so it is  better for garbage collection efficiency)
let myMap = new Map(int16arr); // Map (Maps can have any type for its keys, unlike an object, maps have a size property, Methods: clear, delete, entries, forEach, get, has, keys, set, values)
// WeakMap (Same as Map, but cannot be enumerated over, so it is  better for garbage collection efficiency)

//////////////////////////////////////////////////////////////

/////////////Loops////////////////////
let arry = [1,2,4];
for (let index = 0; index < array.length; index++) { // for loop
    console.log(array[index]);    
}

do { // do while loop
    
} while (condition);

looplabel:          // this is an optional label; if break is used within a loop it will terminate the loop it is currently in,
                    // if you are in nested loops and use break looplabel, it will exit all loops within and including the one that was labeled
while (condition) { // while loop
    
}

for (var key in object) {  // for in loop, used to iterate over the keys in an object
    if (object.hasOwnProperty(key)) {
        var element = object[key];
        
    }
}

for(let x of arr){ // for of loop, used to iterate over an array

}

////////////////////////////////////////////////////////

/////////////Conditionals//////////////////////////////

if (condition) { // if/else
    
} else {
    
}

switch (key) {  // switch case
    case value:
        
        break;

    default:
        break;
}

let x = (myVar == 4) ? 'okay' : 'not okay'; // ternary operator

//////////////////////////////////////////////

/////////////////Functions/////////////////////////

function name(param1, param2 = 4) { // standard function, showing a default argument (default arguments must be after all non-default arguments)
    console.log(arguments); // arguments contains all arguments passed in when the fxn was called
}

function myFxn(param1, ...restOfParams){
    // this function uses rest parameter syntax to capture an arbitrary number of arguments in an array
}

let name = ()=>{ // anonymous function with variable name

}

//////////////////////////////////////////////

////////////////Classes////////////////////////

class MyClass {
    constructor(grade) {
        console.log('object created');
        this.x = grade;
    }

    method1() {
        console.log(`my x value is: ${this.x}`);
    }
}


class MyScienceClass extends MyClass { // inheritance
    constructor(grade) {
        super(grade);       // calls the parent classes constructor
    }
}

let myInstance = new MyScienceClass('A'); // instantiate
myInstance.method1();   // call instance method (this is a method of the parent class, and can be accessed by the child class)

//////////////////////////////////////