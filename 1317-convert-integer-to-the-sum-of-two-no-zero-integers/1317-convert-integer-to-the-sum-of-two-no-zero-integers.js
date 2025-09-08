/**
 * @param {number} n
 * @return {number[]}
 */
var getNoZeroIntegers = function(n) {
    n = n.toString();
    function genNums(idx, n1, n2, carry){
        if (idx === 0){
            let neededSum = parseInt(n.charAt(idx)) - carry;
            let forN1 = Math.floor(neededSum/2);
            n1 = `${forN1}${n1}`;
            n2 = `${neededSum - forN1}${n2}`;
            return [parseInt(n1), parseInt(n2)];
        }
        for (let i = 1; i < 10; i++){
            for (let j = 1; j < 10; j++){
                let currSum = i+j+carry;
                if ((currSum % 10) === parseInt(n.charAt(idx))){
                    let ret =  genNums(idx-1, `${i}${n1}`, `${j}${n2}`, Math.floor(currSum / 10));
                    if ((ret.length === 2)){
                        return ret;
                    }
                }
            }
        }
        return [];
    }
    return genNums(n.length-1, "", "", 0);
};