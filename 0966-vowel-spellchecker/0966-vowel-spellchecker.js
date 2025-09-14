/**
 * @param {string[]} wordlist
 * @param {string[]} queries
 * @return {string[]}
 */
let VOWELS = ['a', 'e', 'i', 'o', 'u'];
var spellchecker = function(wordlist, queries) {
    /* Function that replaces all vowels in a word with '_'
        Cause if we delete all vowels, then it can collide with another word
    */
    let replaceAllVowel = (word) => {
        let lowerCaseWord = word.toLowerCase();
        let withOutVowel = "";
        for (char of lowerCaseWord) {
            if (VOWELS.includes(char)){
                withOutVowel += '_';
            }
            else {
                withOutVowel += char;
            }
        }
        return withOutVowel;
    }

    /*As per given requirements,
        We will map lowercase word to original word (case insensitive)
        We will map lowercase vowel replaced word to original word (case insensitive - vowel eroor)
        We will Remeber only first occurence of such cases, as question requires us to return the first occurence
    */
    let wordDict = new Map();
    for (let i = 0; i < wordlist.length; i++){
        // Remember only first occurence of the word
        if (!wordDict.has(wordlist[i])){
            wordDict.set(wordlist[i], wordlist[i]);
        }
        // Remember only first occurence of case insensitive case
        let lowerCase = wordlist[i].toLowerCase();
        if (!wordDict.has(lowerCase)){
            wordDict.set(lowerCase, wordlist[i]);
        }
        // Remeber only first occurence of case insensitive - vowel error
        let withOutVowels = replaceAllVowel(wordlist[i]);
        if (!wordDict.has(withOutVowels)){
            wordDict.set(withOutVowels, wordlist[i]);
        }
    }

    /* There might be cases where lower case of a word(w1) is already in wordlist as w2
       In such cases when query includes w2, then it could be ambiguous about what to return
       So, we also convert the original list into an set
       Thus, if we get exact match then we know we have to return the original query
             otherwise, we have to map to most appropriate ans. by searching the hash map
    */ 
    wordlist = new Set(wordlist);
    let responses = [];
    for (query of queries) {
        // First check if exact match exists
        if (wordlist.has(query)){
            responses.push(query);
            continue;
        }

        // Check if case insensitive match exists
        query = query.toLowerCase();
        if (wordDict.has(query)) {
            responses.push(wordDict.get(query));
            continue;
        }

        // Check if case insensitive - vowel error match exists
        let withOutVowel = replaceAllVowel(query);
        if (wordDict.has(withOutVowel)) {
            responses.push(wordDict.get(withOutVowel));
        }
        // If no match exists
        else {
            responses.push("");
        }
        
    }

    return responses;
};