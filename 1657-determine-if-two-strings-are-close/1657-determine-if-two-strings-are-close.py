class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count_word1 = Counter(word1)
        count_word2 = Counter(word2)
        
        count_count1 = Counter(count_word1.values())
        count_count2 = Counter(count_word2.values())
        
        return count_count1 == count_count2 and set(count_word1.keys()) == set(count_word2.keys())
        