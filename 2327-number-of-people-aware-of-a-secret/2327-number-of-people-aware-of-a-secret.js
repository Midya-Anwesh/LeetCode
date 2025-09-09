/** 
*  @param {number} n 
*  @param {number} delay 
*  @param {number} forget 
*  @return {number} 
*/ 
var peopleAwareOfSecret = function (n, delay, forget) {
    const MOD = 1000000007n;
    let newLeaker = new Map();
    let forgetOn = new Map();
    let currLeaker = 0n;
    let peopleWhoKnow = 1n;
    newLeaker.set(1 + delay, 1n);
    forgetOn.set(1 + forget, 1n); 
    for (let day = 1; day <= n; day++) {
        if (newLeaker.has(day)) {
            currLeaker += newLeaker.get(day); 
        } 
        if (forgetOn.has(day)) {
            currLeaker -= forgetOn.get(day);
            peopleWhoKnow -= forgetOn.get(day);
        }
        if (currLeaker > 0n) {
            peopleWhoKnow += currLeaker;
            newLeaker.set(day + delay, currLeaker);
            forgetOn.set(day + forget, currLeaker);
        }
    }
    return Number(((peopleWhoKnow % MOD) + MOD) % MOD);
}