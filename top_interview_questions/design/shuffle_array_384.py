from typing import List
import random

# can also use random.sample and then copy over from the idxs - hope I will get random docs
class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums

    def reset(self) -> List[int]:
        return self.org
        

    def shuffle(self) -> List[int]:
        og = [x for x in self.org]
        random.shuffle(self.org)
        shuf = [x for x in self.org]
        self.org = og
        return shuf
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
