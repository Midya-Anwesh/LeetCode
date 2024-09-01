# runtime = 31.0ms
# memory usage = 17.4MB

class Bucket:
    def __init__(self, capacity: int) -> None:
        self.max_cap = capacity
        self.curr = 0

    def __add__(self, filling_amount: int):
        new_bucket = Bucket(self.max_cap)
        new_bucket.curr = self.curr + filling_amount
        return new_bucket
    
    def __sub__(self, draining_amount: int):
        new_bucket = Bucket(self.max_cap)
        new_bucket.curr = self.curr - draining_amount
        return new_bucket
    
class Jug(Bucket):
    def __init__(self, capacity: int) -> None:
        super().__init__(capacity)
    
    def __add__(self, filling_amount: int):
        new_jug = Jug(self.max_cap)
        new_jug.curr = self.curr + filling_amount
        return new_jug
    
    def __sub__(self, draining_amount: int):
        new_jug = Jug(self.max_cap)
        new_jug.curr = self.curr - draining_amount
        return new_jug

class Sol:
    def __init__(self, x:int, y:int, target:int) -> None:
        cap_arr = [x, y, float('inf')]
        self.jug1 = Jug(cap_arr[0])
        self.jug2 = Jug(cap_arr[1])
        self.bucket = Bucket(cap_arr[2])
        self.bucket.curr = cap_arr[-1]
        self.req = target

        self.start_state = (self.jug1, self.jug2, self.bucket)

        self.visited_states = set()
        self.filling_path = [(self.jug1.curr, self.jug2.curr, self.bucket.curr)]
        self.filled = False

    def is_final_state(self, curr_state: tuple) -> bool:
        # Check if any one of the jugs contains reqired amount of water
        return (curr_state[0].curr == self.req) or (curr_state[1].curr == self.req) or\
         (curr_state[0].curr+ curr_state[1].curr == self.req)


    def fill_jugs(self, curr_state: tuple[Jug, Jug, Bucket]) -> None:
        if self.is_final_state(curr_state):
            self.filled = True
            return
        
        j1, j2, b = curr_state

        state = (j1.curr, j2.curr, b.curr)
        if state in self.visited_states:
            return

        self.visited_states.add((j1.curr, j2.curr, b.curr))
        next_states = []

        # Drain j1 to bucket
        if j1:
            next_states.append((j1-j1.curr, j2, b+j1.curr))

        # Drain j2 to bucket
        if j2:
            next_states.append((j1, j2-j2.curr, b+j2.curr))

        if j1.curr < j1.max_cap:

            #fill j1 from bucket
            next_states.append((j1+(j1.max_cap-j1.curr), j2, b-(j1.max_cap-j1.curr)))

            # fill j1 from j2
            if j2:
                j1_deficit = j1.max_cap-j1.curr
                if j2.curr <= j1_deficit:
                    next_states.append((j1+j2.curr, j2-j2.curr, b))
                else:
                    next_states.append((j1+j1_deficit, j2-j1_deficit, b))

        if j2.curr < j2.max_cap:

            # fill j2 from bucket
            next_states.append((j1, j2+(j2.max_cap-j2.curr), b-(j2.max_cap-j2.curr)))

            #fill j2 from j1
            if j1:
                j2_deficit = j2.max_cap-j2.curr
                if j1.curr <= j2_deficit:
                    next_states.append((j1-j1.curr, j2+j1.curr, b))
                else:
                    next_states.append((j1-j2_deficit, j2+j2_deficit, b))

        for states in next_states:
            self.filling_path.append((states[0].curr, states[1].curr, states[2].curr))
            self.fill_jugs(states)
            if self.filled:
                return
            self.filling_path.pop(-1)

    def ans(self):
        ret = []
        for state in self.filling_path:
            state = ", ".join(str(ele) for ele in state)
            ret.append("("+state+")")
        return "\n" + "  -->  ".join(ret) + "\n"
    
    def solve(self):
        self.fill_jugs(self.start_state)
        return self.filled

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        return Sol(x, y, target).solve()