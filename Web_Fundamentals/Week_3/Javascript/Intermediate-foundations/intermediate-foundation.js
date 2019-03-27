function sigma(x){
    var sum = 0;
    
    for(var i = 1; i <= x; i++){
        sum+=i;
    }
    return sum;
}

function factorial(x){
    var prod = 1;

    for(var i = 1; i <= x; i++){
        prod*=i;
    }
    return prod;
}

function fibonnaci(x){
    if(x==0){
        return 0;
    }
    else if(x==1){
        return 1;
    }
    else{
        var prev1 = 0;
        var prev2 = 1;
        for(var i = 2; i <=x; i++){
            var retVal = prev1 + prev2;
            prev1 = prev2;
            prev2 = retVal;
        }
        return retVal;
    }
}

function secLast(x){
    if(x.length <= 1){
        return null;
    }
    else{
        return x[x.length - 2];
    }
}

function nLast(x,n){
    if(x.length < n){
        return null;
    }
    else{
        return x[x.length - n];
    }
}

function secondLargest(x){
    var max = x[0];
    var secMax = x[0];
    for(var i = 0; i < x.length; i ++){
        if(x[i] > max){
            secMax = max;
            max = x[i];
        }

    }
    return secMax;
}

function doubleTrouble(x){
    var retArr = [];
    for(var i = 0; i < x.length; i++){
        retArr.push(x[i]);
        retArr.push(x[i]);
    }
    return retArr;
}

function recursiveFib(n){
    if(n == 0 || n == 1){
        return n;
    }
    else{
        return recursiveFib(n-2) + recursiveFib(n-1);
    }
}

console.log(recursiveFib(100));