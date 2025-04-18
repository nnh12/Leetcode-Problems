class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        color_dict = defaultdict(set)
        ball_dict = {}
        list = []
        query_len = 0

        for query in queries:
            ball, color = query

            if ball in ball_dict and color != ball_dict[ball]:
                color_dict[ball_dict[ball]].remove(ball)
                if len(color_dict[ball_dict[ball]]) == 0:
                    del color_dict[ball_dict[ball]]
                ball_dict[ball] = color
                color_dict[color].add(ball)
            else:
                ball_dict[ball] = color
                color_dict[color].add(ball)
            
            list.append(len(color_dict))
        
        return list
