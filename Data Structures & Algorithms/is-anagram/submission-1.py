class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dico_s = {}
        dico_t = {}

        if len(s) != len(t): return False
        for i in range(len(s)):
            if s[i] in dico_s:
                dico_s[s[i]]+=1
            if s[i] not in dico_s:
                dico_s[s[i]]=1
            if t[i] in dico_t:
                dico_t[t[i]]+= 1
            else:
                dico_t[t[i]] = 1
        return dico_t == dico_s