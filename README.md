<div align="center">

# Assignment 4: 强化学习

[![Python](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/)
[![Deadline](https://img.shields.io/badge/Deadline-Dec%2015-red.svg)](http://101.132.193.95:3000)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

**📅 截止日期：12月15日0:00** | **🏆 [查看排行榜](http://101.132.193.95:3000)** | **📋 Assignment ID: 04**

### 📤 提交要求:通过水杉平台提交

---

</div>

## 📋 任务概述

> 本次任务要求通过强化学习算法解决一个动态位置优化问题。在一个磁性球环境中，智能体（P）需要学习调整其位置，以最大化与动态变化的目标球（q）相关的奖励信号。目标球会根据智能体的移动而响应性地移动，形成一个复杂的动态系统。

## 🎯 环境描述

### 环境参数
- **轨道范围**: 0-99
- **动作范围**: -99到99
- **每轮步数**: 200步

### 状态和动作
- **状态**: 当前智能体位置 P
- **动作**: 移动距离（整数，范围-99到99）
- **轨迹**: 包含历史状态、动作和奖励的序列

### 📊 离线数据集说明

项目提供了`offline_data.csv`离线数据集，包含1000个trial的完整轨迹数据，可用于策略分析和算法调试。

#### 数据集字段说明
| 字段名 | 说明 | 
|--------|------|
| **trial_id** | 试验编号 |
| **step_id** | 当前试验中的步数 | 
| **P** | 智能体当前位置 | 
| **action** | 执行的动作 |
| **reward** | 获得的奖励 |

#### 数据集统计信息
- **总trial数**: 1000个
- **每个trial步数**: 200步
- **总数据量**: 200,000条记录

> 💡 **提示**: 离线数据可以帮助你理解环境动态，但最终评测使用的是实时环境，策略需要能够适应环境的随机性。

## 💻 代码要求

### 需要实现的函数
在 `solution.py` 中实现 `Solution` 类的 `policy` 方法：

```python
def policy(self, state, trajectory):
    """
    实现你的策略函数
    
    参数:
        state: 当前状态（智能体位置P）
        trajectory: 历史轨迹列表，每个元素为(P, action, reward)
    
    返回:
        action: 要执行的动作（整数，范围-99到99）
    """
    # 你的策略实现
    return action
```

### 模式设置
```python
def __init__(self):
    # 设置模式：0=不提交到排行榜，1=提交到排行榜
    self.mode = 1
```

## 📈 评分标准 (总分 20分)

本次作业总分为 20 分。

### 评分规则（基于TotalReward）
根据TotalReward得分进行线性插值计算基础分数：

#### 评分基准点
- **基准线1**: TotalReward = 20 → **6分**
- **基准线2**: TotalReward = 94.61 → **10分**
- **排行榜前10%线**: TotalReward = FullScoreReward（排行榜前10%的最低分） → **20分**

#### 详细得分规则

| 场景 | 条件说明 | 基础得分 |
| :--- | :--- | :--- |
| **1** | TotalReward ≤ 20 | **6 分** |
| **2** | 20 < TotalReward < 94.61 | **6 ~ 10 分** (线性插值) |
| **3** | 94.61 ≤ TotalReward < FullScoreReward | **10 ~ 20 分** (线性插值) |
| **4** | TotalReward ≥ FullScoreReward | **20 分** |

---


## 🚀 运行评测

### 📦 1. 依赖安装:

推荐使用conda环境：

```bash
conda create -n ML python=3.8
conda activate ML
```

### ⚙️ 2. 设置环境变量

**🐧 Linux/macOS:**

```bash
export STUDENT_ID='你的学号'
export STUDENT_NAME='你的姓名'
export STUDENT_NICKNAME='你的昵称'
export MAIN_CONTRIBUTOR='AI' 
```

**🪟 Windows PowerShell:**

```powershell
$env:STUDENT_ID="你的学号"
$env:STUDENT_NAME="你的姓名"
$env:STUDENT_NICKNAME="你的昵称"
$env:MAIN_CONTRIBUTOR="human"
```

### ▶️ 3. 运行评测

**本次作业仅在水杉平台提交**：

```bash
chmod +x evaluate-linux
./evaluate-linux
```

**评测配置**：
- **时间限制**: 60秒
- **步数**: 200步
- **评估指标**: 200步总奖励值
- **提交平台**: 仅限水杉平台

**输出示例**：
```
Starting reinforcement learning assignment evaluation
============================================================
Evaluation configuration:
  Total steps: 200
  Time limit: 60 seconds
  Reward metric: 200-step total reward
============================================================
Found solution.py file
Running mode: 1

Starting reinforcement learning policy evaluation...
--------------------------------------------------
Evaluation completed:
  Steps completed: 200/200
  Total reward: 15.234567
  Evaluation time: 2.34 seconds
  Status: Completed normally

Submitting to leaderboard...
Submission successful!

Evaluation completed!
Final reward: 15.234567
```

### ⏱️ 超时处理说明

**重要**：评测系统有**60秒时间限制**。如果评估超时：

- **自动截断**：系统会立即停止后续步骤的执行
- **评估机制**：使用**当前已获得的总奖励**作为最终得分
- **正常计分**：超时不会影响得分计算，直接使用已完成的奖励值

---

## 🏆 Leaderboard

<div align="center">

### 🌐 访问地址

**🔗 [http://101.132.193.95:3000](http://101.132.193.95:3000)**

---

</div>

### 📋 提交说明

1. **提交频率**: 支持多次提交，系统记录最佳成绩
2. **提交时间**: 截止日期前的所有提交均有效
3. **成绩计算**: 以截止日期前获得的最高TotalReward为准

---

### 🎉 祝你取得好成绩！

**📅 记得在12月15日0:00前提交你的最佳成绩！**

---

Made with ❤️ for Machine Learning Education

</div>
