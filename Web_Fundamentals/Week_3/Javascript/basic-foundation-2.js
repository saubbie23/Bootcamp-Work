function makeitBig(x){
    for(var i = 0; i < x.length; i++){
        if(x[i] > 0){
            x[i] = "Big";
        }
    }
    return x;
}

function printLow(x){
    var min = x[0];
    var max = x[0];

    for(var i = 0; i < x.length; i++){
        if(x[i] < min){
            min = x[i];
        }
        else if(x[i] > max){
            max = x[i];
        } 
    }
    console.log(min);
    return max;
}

function retOdd(x){
    console.log(x[x.length - 2]);

    for(var i = 0; i < x.length; i++){
        if(x[i] % 2 != 0){
            return x[i];
        }
    }
}

function doubleVision(x){
    var retArr = []

    for(var i = 0; i < x.length; i++){
        retArr[i] = x[i]**2;
    }
    return retArr;
}

function countPos(x){
    var count = 0;

    for(var i = 0; i < x.length; i ++){
        if(x[i] > 0){
            count++;
        }
    }
    x[x.length - 1] = count;
    return x;
}

function evensOdds(x){
    var countOdd = 0;
    var countEven = 0;

    for(var i = 0; i < x.length; i++){
        if(x[i] % 2 == 0){
            countOdd = 0;
            countEven++;
        }
        else{
            countEven = 0;
            countOdd++
        }

        if(countEven >= 3){
            console.log('Even more so!');
        }
        if(countOdd >= 3){
            console.log('Thats odd!');
        }
    }
}

function incOdds(x){
    for(var i = 1; i < x.length; i+=2){
        x[i] = x[i] + 1;
    }
    console.log(x);
    return x;
}

function prevLen(x){
    for(var i = x.length - 1; i>=1; i--){
        x[i] = x[i-1].length;
    }

    return x;
}

function addSeven(x){
    var retArr = [];

    for(var i = 0; i < x.length; i++){
        retArr[i] = x[i] + 7;
    }
    return retArr;
}

function negative(x){
    for(var i = 0; i < x.length; i ++){
        if(x[i] > 0){
            x[i] = x[i] * -1;
        }
    }

    return x;
}

function alwaysHungry(x){
    var count = 0;

    for(var i = 0; i < x.length; i++){
        if(x[i] == "food"){
            console.log("yummy");
            count++;
        }
    }

    if(count == 0){
        console.log("I'm always hungry!");
    }
}

function swapCenter(x){
    var temp = 0;
    var len = x.length;

    for(var i = 0; i < len / 2; i ++){
        temp = x[i];
        x[i] = x[x.length - i - 1];
        x[x.length - i - 1] = temp; 
    }

    return x;
}

console.log(swapCenter([1,2,4,true,'aaa',6]));

function scaleArr(x, Y){
    for(var i = 0; i < x.length; i ++){
        x[i] = x[i] * Y;
    }

    return x;
}