/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function(n, languages, friendships) {
    let [mostFavLangCount, favLangs, countedPeople] = [0, new Map(), new Set()];
    function func(idx){
        for (lang of languages[idx]){
            if (favLangs.has(lang)){
                favLangs.set(lang, favLangs.get(lang)+1);
            }
            else{
                favLangs.set(lang, 1);
            }
            mostFavLangCount = Math.max(mostFavLangCount, favLangs.get(lang));
        }
    }
    for (friends of friendships){
        let [u, v] = friends;
        let comLangs = new Set(languages[u-1]).intersection(new Set(languages[v-1])).size;
        if (comLangs === 0){
            if (!countedPeople.has(u)){
                func(u-1);
                countedPeople.add(u);
            }
            if (!countedPeople.has(v)){
                func(v-1);
                countedPeople.add(v);
            }
        }
    }
    if (countedPeople.size > 0){
        return countedPeople.size - mostFavLangCount;
    }
    return 0;
};