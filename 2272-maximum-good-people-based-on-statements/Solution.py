# runtime = 373.0ms
# memory usage = 16.6MB

class Statement:
    def holds(self, statement: list[int], good_persons):
        for person, person_description in enumerate(statement):
            if (person_description == 1 and (not person in good_persons)) or \
            (person_description == 0 and person in good_persons):
                return False
        return True

class Solution:
    def good_person_subset(self, persons: int):
        for len in range(persons, 0, -1):
            yield from itertools.combinations(range(persons), len)

    def maximumGood(self, statements: list[list[int]]) -> int:
        for good_persons in self.good_person_subset(len(statements[0])):
            is_valid_distribution = True
            for person in good_persons:
                if not Statement().holds(statements[person], set(good_persons)):
                    is_valid_distribution = False
                    break
            if is_valid_distribution:
                return len(good_persons)
        return 0