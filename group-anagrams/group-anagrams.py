class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = dict()

        for word in strs:
            sorted_word = sorted(word)
            result[tuple(sorted_word)] = []

        for elem in strs:
            result[tuple(sorted(elem))].append(elem)


        return result.values()
        