# runtime = 695.0ms
# memory usage = 16.6MB

class Solution:
    def __init__(self):
        self.operetors = ["*","/","+","-"]
        self.solved = False
        self.curr_arr = []


    def check_all_possibility(self, cards, cards_length = 0):
        if cards_length == 4:
            for value in self.evaluate(self.curr_arr, 0, 4):
                if round(value,1) == 24.0:
                    #print(self.curr_arr)
                    self.solved = True
            return

        for card in cards:
            if cards[card]:
                cards[card] -= 1
                self.curr_arr.append(card)
                self.check_all_possibility(cards, cards_length+1)
                if self.solved:
                    self.curr_arr = []
                    return
                self.curr_arr.pop(-1)
                cards[card] += 1


    def evaluate(self, cards, lb, ub):
        if ub-lb <= 1:
            yield cards[lb]

        elif ub-lb == 2:
            for op in self.operetors:

                yield eval(f"{cards[lb]}{op}{cards[ub-1]}")

        else:
            for k in range(lb+1, ub):
                for v1 in self.evaluate(cards, lb, k):
                    for op in self.operetors:
                        for v2 in self.evaluate(cards, k, ub):
                            if (op != "/" or (op == "/" and v2 != 0)):
                                yield eval(f"{v1}{op}{v2}")




    def judgePoint24(self, cards: List[int]) -> bool:
        card_map = dict()
        for card in cards:
            card_map[card] = card_map.get(card, 0)+1
        self.check_all_possibility(card_map)
        return self.solved
        
        