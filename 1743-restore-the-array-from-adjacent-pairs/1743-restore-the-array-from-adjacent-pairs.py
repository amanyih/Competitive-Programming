class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        result = []
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for left, right in adjacentPairs:
            graph[left].append(right)
            graph[right].append(left)
            indegree[left] += 1
            indegree[right] += 1
        
        ends = [element for element in indegree if indegree[element] == 1]
        
        for element in graph:
            if indegree[element] == 1:
                start = element
                break
        
        queue = collections.deque([start])
        result.append(start)
        
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)
                    result.append(neighbor)
        
        if ends[0] == start:
            result.append(ends[1])
        else:
            result.append(ends[0])
    
        return result

        