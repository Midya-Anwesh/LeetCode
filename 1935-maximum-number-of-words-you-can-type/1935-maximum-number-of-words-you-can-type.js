/**
 * @param {string} text
 * @param {string} brokenLetters
 * @return {number}
 */
var canBeTypedWords = function(text, brokenLetters) {
    brokenLetters = new Set(brokenLetters);
    text = text.split(" ");
    let ans = text.length;
    for (word of text){
        for (char of word){
            if (brokenLetters.has(char)){
                ans -= 1;
                break;
            }
        }
    }
    return ans;
};