function bubbleSort(arr) {
    for(let i = 0; i < arr.length -1; i++){
        for(let j = 0; j < arr.length - i - 1; j++){
            if(arr[j] > arr[j + 1]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

function bubbleSortRecursive(arr,length) {
    if(length == 1)
        return;
    for(let j = 0; j < length -1; j++){
        
            if(arr[j] > arr[j + 1]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        
    }
    bubbleSortRecursive(arr, length - 1);
}

let myArray = [4,9,6,0,4,7,9,7,9,0,0,89,77,-2,-55,8];
let myArray2 = [4,9,6,0,4,7,9,7,9,0,0,89,77,-2,-55,8];

console.log(myArray);
bubbleSortRecursive(myArray,myArray.length);
console.log(myArray);

console.log(myArray2);
bubbleSort(myArray2);
console.log(myArray2);

// Time Complexity
// Theta(n)
// Omega(n^2)
// O(n^2)

// Space Complexity
// O(1)