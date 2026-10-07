class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for s in strs:
            # say delimiter is `
            # so a string "vortex" = "6`vortex"
            curr = [str(len(s)), '`', s]
            ret.append(str(len(s)))
            ret.append('`')
            ret.append(s)
        return ''.join(ret)
    def decode(self, s: str) -> List[str]:
        ret = [] 
        curr_strlen = 0
        curr_delim = s.find('`')   
        while curr_delim != -1:
            strlen = int(s[curr_strlen:curr_delim]) 
            word = s[curr_delim+1:curr_delim+1 + strlen] 
            ret.append(word)
            curr_strlen=curr_delim+1+strlen 
            curr_delim=s.find('`',curr_strlen)
        return ret
        