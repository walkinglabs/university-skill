---
name: university-textbook
description: 创建约 20 页的快速阅读技术课本，聚焦核心概念、关键推导、代表性手算与最小实现。适用于快速入门、预习或回顾深度学习、具身智能等技术主题，交付 LaTeX/PDF 与 Markdown；超过 40 页的系统学习需求使用 university-coursebook。
---

# University Textbook · 约 20 页快速阅读

默认交付约 20 页的精简课本：收敛主题范围，优先讲清关键原理和一个完整例子。保留理解所必需的推导，不靠缩小字号压缩页数。用户指定篇幅时以其要求为准。

本技能沉淀了世界顶级的深度学习与具身智能机器人教科书教程撰写全流程规范，旨在解决长篇学术讲义编写中的“篇幅被压缩、跳步推导、代码简略、排版溢出”等瓶颈，实现兼具费曼大白话启发力、高中数理认知脚手架、微观纯手工演算、可运行端到端代码和严格数学附录的高质量长篇教程输出。

---

## 核心四大支柱与标准规范

### 1. 章节因果链条严密咬合（The Narrative Thread）
- **第一节**：认知渊源、物理常识与底层矛盾（质点模型/像素熵陷阱/存储墙/莫拉维克悖论）；
- **第二节**：经典基准架构剖析与几何/动力学崩溃危机（Representation Collapse、自回归累积漂移）；
- **第三节**：新范式核心数学突破与动力学直觉（非对称动力学、Stop-Gradient、EMA 动量飞轮、连续流匹配）；
- **第四节**：**微观单步纯手工演算（极为关键）**：设定低维数值（如 $D=2$），一步不跳地计算前向预测、损失、反向传播次梯度、参数更新与 EMA 平滑的每一个真实数字；
- **第五节**：给出**学术级 LaTeX 伪代码（必须严格遵循 `algorithm + algorithmic` 规范）**，并编写**可直接跑通的端到端 PyTorch Demo 网络**，附带与官方工业实现的 `torch.allclose` 零误差校验；
- **第六节**：全景代际对比表格 + 工业级落地部署避坑指南 + 顶会论文研读导航图；
- **附录（阶梯 0 -> 1 -> 2）**：将最硬核的数学底座（李群流形、连续极限 ODE、李雅普诺夫稳定性、VICReg 协方差满秩定理）彻底剥离并循序渐进讲透。

### 2. 高中数理认知支架（Cognitive Scaffolding）
- **阶梯 0（生活/高中常识）**：用最朴素的生活现象建立物理直觉（如画家画马抓神态、打网球挥拍肌肉记忆、双人滑冰惯性牵引）；
- **阶梯 1（低维代数手算）**：用二维坐标 $[x, y]$、一元方程真实代入具体数值演算每一步；
- **阶梯 2（高维严格泛函与顶会原始定义）**：给出顶会论文的原版公式与严格证明。

### 3. TikZ 矢量配图防出界与精密排版铁律
- 全文至少包含 4 幅高精度 TikZ 图表；
- **单节点封装排版**：方框内部文字必须写在同一个 Node 的 `{}` 中，严禁使用游离文本导致文字冲出边框；
- **显式文本宽度约束**：凡设置 `minimum width=W` 的节点，必须显式声明 `text width=W-0.5cm, align=center`，并配置 `inner sep=4pt~6pt`；
- **连线文字防碰撞**：两模块间若有文字标注，水平净空必须预留 $\ge 2.0\text{cm}$，文字多行换行排版；
- 整体画布宽度控制在 `12cm` 以内（`scale=0.9` 左右），杜绝 `Overfull \hbox`。

### 4. 学术级 LaTeX 伪代码标准规范（严二姨/官方标准）

在 LaTeX 文档中，伪代码排版遵循以下标准规范：

```latex
\usepackage{algorithm}
\usepackage{algorithmic}

\begin{algorithm}[htbp]
\renewcommand{\algorithmicrequire}{\textbf{Input:}}
\renewcommand{\algorithmicensure}{\textbf{Output:}}
\caption{算法标题}
\label{alg:my_algorithm}
\begin{algorithmic}[1]
\STATE \textbf{Input:} 输入变量与超参数
\STATE \textbf{Output:} 输出结果
\STATE 初始化参数
\REPEAT
    \STATE 核心计算与前向传播
    \FOR{$i = 1$ \TO $M$}
        \STATE 单步更新与条件分支
    \ENDFOR
    \STATE 反向传播与梯度更新
    \STATE 动量平滑演化
\UNTIL 收敛
\STATE \textbf{Ensure:} 最终优化模型
\end{algorithmic}
\end{algorithm}
```

---

## 分卷流水线执行策略（Multi-Stage Chunked Pipeline）

在撰写约 20 页的快速阅读课本时，按内容分块并控制每部分篇幅，采用多阶段流水线调度：
1. **阶段 0：全局状态与符号注册表**（锁定全书统一符号与引用接口）；
2. **阶段 1：分块深度撰写**（Chunk A: 1-2 节 $\to$ Chunk B: 3-4 节 $\to$ Chunk C: 5 节代码 $\to$ Chunk D: 6 节对比 $\to$ Chunk E: 附录推导）；
3. **阶段 2：缝合与交叉引用链接修复**；
4. **阶段 3：自动化双次编译与 TikZ 排版自愈**。

## 配套资源

- 撰写主线正文前，读取 [写作指南](references/writing-guide.md)。
- 需要 TikZ 机制图时，读取 [图解指南](references/diagram-guide.md)。
- 需要严格数学附录时，读取 [数学附录指南](references/math-appendix-guide.md)。

这些文件与 `SKILL.md` 位于同一技能目录，安装时必须一起保留。
