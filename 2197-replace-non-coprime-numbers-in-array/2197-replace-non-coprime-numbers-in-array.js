/**
 * @param {number[]} nums
 * @return {number[]}
 */
var replaceNonCoprimes = function(nums) {
    function GCD(a, b) {
        while (b != 0) {
            [a, b] = [b, a%b];
        }
        return a;
    }

    let stack = [];

    for (num of nums){
        if (!stack.length) {
            stack.push(num);
            continue;
        }

        let gcd = GCD(num, stack.slice(-1)[0]);
        stack.push(num);
        while (gcd > 1) {
            let p1 = stack.pop();
            let p2 = stack.pop();
            stack.push((p1*p2) / gcd);
            if (stack.length == 1){
                break;
            }
            gcd = GCD(stack.slice(-1)[0], stack.slice(-2, -1)[0]);
        }
    }
    return stack;
};