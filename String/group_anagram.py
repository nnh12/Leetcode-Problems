class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_list = {}
        return_list = []

        for str in strs:
            sorted_str = ''.join(sorted(str)) # sort the string
            if sorted_str not in dict_list:
                dict_list[sorted_str] = []
                dict_list[sorted_str].append(str)
            else:
                dict_list[sorted_str].append(str)
        
        for key in dict_list:
            return_list.append(dict_list[key])
        
        return return_list    
