class Solution:
    def maxOperations(self, s: str) -> int:
        moves = 0
        num_of_1 = 0
        curr_1s = 0

        for c in s:
            if c == '1':
                curr_1s += 1
            elif not curr_1s:
                continue
            # there was some one block
            else:
                moves += curr_1s + num_of_1
                num_of_1 += curr_1s
                curr_1s = 0
        
        return moves
