function printAverage(x){
    sum = 0;
    // your code here
    for(var i=0;i<x.length;i++){
        sum+=x[i];
    }
    return sum / x.length
 }
 y = printAverage([1,2,3]);
 console.log(y); // should log 2
   
 y = printAverage([5,2,8]);
 console.log(y); // should log 5



 function returnOddArray(){
    // your code here
    retArr = []
    for(var i=1;i<=255; i+=2){
        retArr.push(i);
    }
    return retArr;
 }
 y = returnOddArray();
 console.log(y); // should log [1,3,5,...,253,255]


 function squareValue(x){
    // your code here
    for(var i = 0; i<x.length; i++){
        var tempVal = x[i] * x[i];
        x[i] = tempVal;
    }
    return x;
 }
 y = squareValue([1,2,3]);
 console.log(y); // should log [1,4,9]
   
 y = squareValue([2,5,8]);
 console.log(y); // should log [4,25,64]
