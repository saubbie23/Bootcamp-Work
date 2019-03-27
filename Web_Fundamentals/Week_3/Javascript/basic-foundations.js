function get255(){
    var retArr = [];
    for(i=1; i <=255; i++){
        retArr.push(i);
    }
    return retArr;
}

function evenSum(){
    var sum = 0;
    for(var i = 2; i <= 1000; i+=2){
        sum+=i;
    }
    return sum;
}

function oddSum(){
    var sum = 0;
    for(var i = 1; i < 5000; i+=2){
        sum+=i;
    }
    return sum;
}

function sumArray(x){
    var sum = 0;
    for(var i = 0; i < x.length; i++){
        sum+=x[i];
    }
    return sum;
}

function arrayMax(x){
    var max = x[0];
    for(var i = 0; i < x.length; i++){
        if(x[i] > max){
            max = x[i];
        }
    }
    return max;
}

function arrayAvg(x){
    var len = x.length;
    var sum = 0;

    for(var i=0; i < len; i++){
        sum+=x[i];
    }
    return sum / len;
}

function oddArr(){
    var retArr = []
    for(var i = 1; i < 50; i+=2){
        retArr.push(i);
    }
    return retArr;
}

function greaterThan(x,Y){
    var count = 0;
    for(var i = 0; i < x.length; i++){
        if(x[i] > Y){
            count++;
        }
    }
    return count;
}

function squareArr(x){
    for(var i = 0; i < x.length; i++){
        x[i] = x[i]**2;
    }
    return x;
}

function negatives(x){
    for(var i = 0; i < x.length; i++){
        if(x[i] < 0){
            x[i] = 0;
        }
    }
    return x;
}

function maxMinAvg(x){
    var max = x[0];
    var min = x[0];
    var len = x.length;
    var sum = 0;
    var retArr = [];
    
    for(var i = 0; i < len; i ++){
        sum+= x[i];
        if(x[i] > max){
            max = x[i];
        }
        else if(x[i] < min){
            min = x[i];
        }
    }
    retArr.push(min);
    retArr.push(max);
    retArr.push(sum/len);
    return retArr;
}

function swapVals(x){
    var temp = x[0];
    x[0] = x[x.length - 1];
    x[x.length - 1] = temp;

    return x;
}

function numString(x){
    for(var i = 0; i < x.length; i ++){
        if(x[i] < 0){
            x[i] = 'Dojo';
        }
    }
    return x;
}