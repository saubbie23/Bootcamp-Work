function fizzBuzz(num){

        for(var i = 1; i <=num; i++){
            if(i % 3 == 0){
                if(i % 5 == 0){
                    console.log("FizzBuzz");
                }
                else{
                    console.log('Fizz');    
                }
            }
            else if(i % 5 ==0){
                console.log('Buzz');
            }
            else{
                console.log(i);
            }
        }
}

// fizzBuzz(15);

function rotateArray(arr,shiftBy){
    for(var i = arr.length - 1; i > 0; i--){

        if(i + shiftBy > arr.length - 1){
            // var leftOver = arr.length - shiftBy - i;
            var leftOver = (shiftBy + i) - arr.length;
            // console.log(leftOver);
            temp = arr[leftOver];
            arr[leftOver] = arr[i];
            arr[i] = temp;  
            // console.log(i,arr); 
            // console.log('temp val',i, temp); 
        }
        else{
            temp = arr[i + shiftBy];
            arr[i + shiftBy] = arr[i];
            arr[i] = temp;
            // console.log(i,arr);
            // console.log('temp val', i, temp); 
        };
    }
    return arr;
}

// console.log(rotateArray([1,2,3,4,5,6],2));

function rotateArr(arr, shiftBy) {

    for (var j = 0; j < shiftBy; j++) {
        var temp = arr[arr.length - 1];
        for (var i = arr.length - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        arr[0] = temp;
    }
    return arr;
}
console.log(rotateArr([1, 2, 3, 4, 5], -1));