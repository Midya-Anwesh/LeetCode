/**
 * @param {number[][]} queries
 * @return {number}
 */
var minOperations = function(queries) {
    let logBase = (num, base) => (Math.log(num+1) / Math.log(base));
    let ret = 0;
    for (query of queries){
        let [start, end] = query;
        let [dMax, s] = [0, 0];
        while (start <= end){
            let exp = Math.ceil(logBase(start, 4));
            dMax = Math.max(dMax, exp);
            let num = Math.pow(4, exp) - 1;
            if (num >= end){
                num = end;
            }
            let noOfElements = num-start+1;
            s += noOfElements * exp;
            start = num+1;
        }
        ret += Math.max(dMax, Math.ceil(s/2));
    }
    return ret;
};