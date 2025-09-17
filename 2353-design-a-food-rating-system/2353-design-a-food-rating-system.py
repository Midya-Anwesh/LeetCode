
from collections import defaultdict
from heapq import heappush, heappop
from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.childs = [None for _ in range(26)]
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = None
        self.length = 0
    
    def addWord(self, word: str) -> None:
        if self.root is None:
            self.root = TrieNode()
        temp = self.root
        for i in range(len(word)):
            if temp.childs[ord(word[i])-97] is None:
                temp.childs[ord(word[i])-97] = TrieNode()
            temp = temp.childs[ord(word[i])-97]
        
        # Only increment length if this is a new word
        if not temp.wordEnd:
            temp.wordEnd = True
            self.length += 1
    
    def getMinWord(self, currNode: Optional['TrieNode']) -> str:
        if currNode is None:
            return ""
        for i in range(len(currNode.childs)):
            if currNode.childs[i] is None:
                continue
            if currNode.childs[i].wordEnd:
                return chr(i+97)
            ret = self.getMinWord(currNode.childs[i])
            if len(ret):
                return chr(i+97) + ret
        return ""
    
    def removeWord(self, word: str) -> None:
        temp = self.root
        if temp is None:
            return
        for i in range(len(word)):
            if temp.childs[ord(word[i])-97] is not None:
                temp = temp.childs[ord(word[i])-97]
            else:
                return  # Word not found
        
        # Only decrement if word actually exists
        if temp.wordEnd:
            temp.wordEnd = False
            self.length -= 1

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hashedCuisines = defaultdict(lambda: ([], defaultdict(lambda: Trie())))
        self.foodToCuisineRating = dict()
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            ratingHeap, ratingWiseFood = self.hashedCuisines[cuisine]
            ratingWiseFood[rating].addWord(food)
            if ratingWiseFood[rating].length == 1:
                heappush(ratingHeap, -rating)
            self.foodToCuisineRating[food] = [cuisine, rating]
    
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.foodToCuisineRating[food]
        ratingHeap, ratingWiseFood = self.hashedCuisines[cuisine]
        
        ratingWiseFood[rating].removeWord(food)
        ratingWiseFood[newRating].addWord(food)
        if ratingWiseFood[newRating].length == 1:
            heappush(ratingHeap, -newRating)
        
        self.foodToCuisineRating[food][1] = newRating
    
    def highestRated(self, cuisine: str) -> str:
        ratingHeap, ratingWiseFood = self.hashedCuisines[cuisine]
        while ratingHeap and ratingWiseFood[-ratingHeap[0]].length == 0:
            heappop(ratingHeap)
        
        if ratingHeap:
            maxRating = -ratingHeap[0]
            return ratingWiseFood[maxRating].getMinWord(ratingWiseFood[maxRating].root)
        return ""