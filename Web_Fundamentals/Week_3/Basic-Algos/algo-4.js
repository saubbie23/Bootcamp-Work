function printVals(x,Y){
    var count = 0;
    for(var i=0; i < x.length; i++){
        if(x[i] > Y){
            count++;
        }
    }
    console.log(count);
}

printVals([1,2,3,4,5], 3);


function maxMinAvg(x){
    var min = 0;
    var max = 0;
    var sum = 0;
    for(var i = 0; i <x.length; i++){
        if(i==0){
            min = x[i];
            max = x[i];
            sum = x[i];
        }
        else{
            if(x[i] < min){
                min = x[i];
            }
            else if(x[i] > max){
                max = x[i];
            }
            sum+=x[i];
        }
    }

    console.log('Minimum: ' + min);
    console.log('Maximum: ' + max);
    console.log('Sum: ' + sum/x.length);
}

maxMinAvg([1,2,3,4,5,6,7]);


function replaceNegs(x){
    for(var i = 0; i < x.length; i++){
        if(x[i] < 0){
            x[i] = 'Dojo';
        }
    }
    console.log(x);
    return x;
}

replaceNegs([1,2,3,-4,-7]);

function removeVals(x, pos1, pos2){
    x.splice(pos1,1);
    x.splice(pos2 -1, 1);
    console.log(x);
    return x;
}

removeVals([1,2,3,4,5,6,7,8],2,5);