class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.score = []
        self.times = times
        count = defaultdict(int)
        leader = persons[0]
        
        for person in persons:
            count[person] += 1
            if count[person] >= count[leader]:
                leader = person
            self.score.append(leader)
        

    def q(self, t: int) -> int:
        left = 0
        right = len(self.score) - 1
        ans = 0

        while left <= right:

            mid = (left + right) // 2

            if self.times[mid] <= t:
                left = mid + 1
                ans = mid
            else:
                right = mid-1
        return self.score[ans]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)