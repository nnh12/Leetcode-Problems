class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        list = [0]*n
        time_stamp = 0

        for i in range(len(logs)):
            log = logs[i].split(':')
            cur_id = int(log[0])
            cur_type = log[1]
            cur_time = int(log[2])

            if cur_type == "start":
                if stack:
                    prev_id, prev_type, prev_time = stack[-1]
                    list[prev_id] += cur_time - time_stamp

                stack.append( (cur_id, cur_type, cur_time) )
                time_stamp = cur_time
            else:
                prev_id, prev_type, prev_time = stack.pop()
                list[cur_id] += cur_time - time_stamp + 1
                time_stamp = cur_time + 1


        return list
