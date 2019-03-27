function resetNegatives(x){
    for(i=0; i < x.length; i++){
        if (x[i] < 0){
            x[i] = 0;
        }
    }
    return x;
}

console.log(resetNegatives([1,2,-3,-5]));

function moveForward(x){
    x.shift();
    x.push(0);
    return x;
}

console.log(moveForward([1,2,3,4,5,6]));


function returnReversed(x){
    var temp = 0;
    var len = x.length;
    for(i=0; i < len / 2; i++){
        temp = x[i];
        x[i] = x[len - i - 1];
        x[len - i - 1] = temp;
    }
    return x;
}

console.log(returnReversed([1,2,3,4,5,6]));

function repeatTwice(x){
    var retArr = [];
    for(var i = 0; i < x.length; i ++){
        retArr.push(x[i]);
        retArr.push(x[i]);
    }
    return retArr;
}

console.log(repeatTwice([1,2,3,4,5,6]));