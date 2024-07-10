class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}

        for str_ in strs:
            sorted_str = "".join(sorted(str_))
            if sorted_str not in map_:
                map_[sorted_str] = [str_]
            else:
                map_[sorted_str].append(str_)
            
        result = [map_[key] for key in map_.keys()]
        
        return result
            
