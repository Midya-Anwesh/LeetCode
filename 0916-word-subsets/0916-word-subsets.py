class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:


        """
        
        In order to check if a word of words1 is a superset of all word present in words2 we need to do the following:
            1. All characters that occurs in string of words1 must have frequinceis that are >= max(frequency of that chatacter in all strings in words2)
        
        To track that we will use two dictionary,
            temp: To keep track of frequencies of characters in current string of words2
            target: To keep only the max frequencies of characters, by comparing frequinceis of characters present in temp and target

        And lastly, we will traverse through all words in words1, for every word we will do the following
            1. Store frequencies of all characters of current word in a temporary(temp) dictionary
            2. With the help of temp and target we will check if the cuurent word is a superset of all word present in words2
            3. If it satisfies then we will add it to the return vector
        
        """


        # Dict to store max frequencies of all characters in words2
        target = dict()

        # Traverse every word in words2
        for word in words2:

            # Store the frequency of all character in current word in temporary dict
            temp = dict()
            for char in word:
                temp[char] = temp.get(char, 0) + 1

            # Update the target to keep track of only max frequencies
            target = {char:max(target.get(char, 0), temp.get(char, 0)) for char in temp|target}
        
        # Return vector
        ret = []

        # Traverse all word of words1
        for word in words1:

            # Keep track of frequencies of characters in current word
            temp = dict()
            for char in word:
                temp[char] = temp.get(char, 0) + 1

            # Check the condition for a word of words1 to be a superset of all word present in words2
            # If yes, then add the current word to return vector
            if all(temp.get(char, 0) >= target[char] for char in target):
                ret.append(word)

        # Return all the words of words1 that are superset of all word present in words2
        return ret