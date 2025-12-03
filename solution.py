# solution.py
import numpy as np

class Solution:
    def __init__(self):
        # 设置模式：0=不提交到排行榜，1=提交到排行榜,默认为1
        self.mode = 1  
        
    def policy(self, state, trajectory):
        """
        实现你的策略函数
        """
        # 示例：随机移动
        
        return np.random.randint(-99, 99)
