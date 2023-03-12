class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = []
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.q) == self.k:
            if self.q[0] == self.value:
                self.count -= 1
            self.q.pop(0)
        if num == self.value:
            self.count += 1
        self.q.append(num)
        return self.count == self.k
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/description/
