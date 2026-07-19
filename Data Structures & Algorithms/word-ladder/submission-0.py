class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        # 1 Build the hashmap/graph using wildcards

        graph = defaultdict(set)
        wordList.append(beginWord)

        def get_wildcards(word):
            res = set()
            for i in range(len(word)):
                wildcard = word[0:i]+"*"+word[i+1:]
                res.add(wildcard)
            return res

        for word in wordList:
            for wildcard in get_wildcards(word):
                graph[wildcard].add(word)

        # 2 BFS to traverse and find endword
        count = 0
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        while q:
            count += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return count
                for wildcard in get_wildcards(node):
                    for word in graph[wildcard]:
                        if word not in visited:
                            q.append(word)
                            visited.add(word)
                    
        return 0