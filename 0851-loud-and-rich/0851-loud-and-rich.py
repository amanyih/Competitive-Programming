class Solution:
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N

        def dfs(node):
            if answer[node] is not None:
                return answer[node]

            answer[node] = node
            for child in graph[node]:
                cand = dfs(child)
                if quiet[cand] < quiet[answer[node]]:
                    answer[node] = cand

            return answer[node]

        return [dfs(node) for node in range(N)]

        