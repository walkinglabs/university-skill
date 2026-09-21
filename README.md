<div align="center">

# 大学.skill

<p align="center">
  <img src="assets/hero.gif" width="800" alt="把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课。" />
  <br />
  <sub>动画由 <a href="https://github.com/alchaincyf/huashu-design">huashu-design</a> skill 制作</sub>
</p>

> *「你想上的下一堂大学课，何必等开学。」*

[![Agent Skills](https://img.shields.io/badge/Agent_Skills-SKILL.md-55745c?style=flat-square)](SKILL.md)
[![Output](https://img.shields.io/badge/Output-Markdown_·_LaTeX_·_PDF-a74b38?style=flat-square)](#你会得到什么)
[![Language](https://img.shields.io/badge/中文-English-657580?style=flat-square)](README_EN.md)
[![Stars](https://img.shields.io/github/stars/walkinglabs/university-skill?style=flat-square&color=55745c)](https://github.com/walkinglabs/university-skill/stargazers)

<br />

**把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课。**

**Put a university professor in your AI. Turn any topic into a real university lecture.**

<sub>基于 SKILL.md 的教学技能，可安装到支持 Agent Skills 的 AI 助手中。</sub>

<br />

想学蛋白质设计、JEPA，或一个从没接触过的领域？<br />
告诉 AI 你想学什么，让它像一位好教授那样，从基础讲到原理，从例子讲到实践。<br />
需要带走慢慢读，也可以直接说：**帮我写一本 PDF 课本。**

[看效果](#效果示例) · [安装](#安装) · [它会怎么教](#它会怎么教) · [工作原理](#工作原理)

<br />

**其他语言 / Other Languages:**

[English](README_EN.md)

<br />

</div>

---

## 效果示例

只需说出你想学的主题，以及你希望怎样学。

```text
用户       ❯ 帮我写一本 PDF 课本：从零入门蛋白质结构设计 AI4S。
             假设我只有高中生物和数学基础。

大学.skill ❯ 从氨基酸如何组成蛋白质讲起，解释序列、结构与功能的关系，
             再区分结构预测和蛋白质设计各自在解决什么问题。
             随后进入 AI 方法，用示意图、具体案例和练习逐步展开。
             最后整理为 PDF 课本，附术语表、自测答案与文献导航。
```

```text
用户       ❯ 帮我写一本 PDF 课本：从零入门 JEPA 模型。
             要讲清原理，用小数字走一遍，再给最小代码示例。

大学.skill ❯ 先解释为什么要学习表示，以及预测表示和重建像素有何区别。
             再拆开上下文编码器、目标编码器和预测器，
             用低维例子说明信息如何流动、损失如何计算，
             然后讨论表示坍塌、训练机制与不同 JEPA 变体的边界。
```

```text
用户       ❯ 帮我写一本 PDF 课本：从零理解 RSI 的发展和原理。

大学.skill ❯ 这里的 RSI 是递归自我改进，还是金融中的相对强弱指标？
             确定含义后，从它要解决的问题出发，串起发展脉络、
             核心原理、具体例子和适用边界，关键事实逐项核实来源。
```

再看一个具体的手算片段：

```text
你       › 我只有高中数学基础，给我讲透梯度下降。

大学.skill › 先从一个只有一个参数的模型开始：预测值 = w × x。
             x = 2，目标值 = 6，初始 w = 1。

             预测：1 × 2 = 2
             误差：2 − 6 = −4
             损失：½ × (−4)² = 8
             梯度：(2 − 6) × 2 = −8
             更新：1 − 0.1 × (−8) = 1.8
             新损失：½ × (3.6 − 6)² = 2.88

             为什么是减去梯度？步长太大会怎样？
             从这一个数字例子，接着推到一般公式与代码。
```

[阅读全文与练习](examples/gradient-descent.md) · [运行数值核验](examples/gradient_descent.py)

<sub>以上对话为设计示例，展示预期教学方式；梯度下降数字由随附脚本核验，未将示例描述为已生成的完整课本。</sub>

---

## 安装

### 方式一：一句话安装

把下面这句话交给你正在使用的技能兼容助手：

```text
帮我安装这个 skill：https://github.com/walkinglabs/university-skill
```

### 方式二：手动安装

将完整仓库放入所用工具的技能目录，保留 `references/` 与 `assets/`。例如在 Codex 的用户技能目录中：

```bash
git clone https://github.com/walkinglabs/university-skill.git ~/.codex/skills/university-skill
```

入口为根目录的 [SKILL.md](SKILL.md)。纯讲义写作不需要额外 API Key；PDF 需要中文 LaTeX 环境，代码验证需要相应语言与依赖。模型、联网与文件操作由宿主助手提供，具体运行时兼容性仍需验证。

### 开始上课

```text
帮我写一本 PDF 课本：从零入门蛋白质结构预测与设计 AI4S。
帮我写一本 PDF 课本：从零入门 JEPA 模型，附手算和代码。
帮我写一本 PDF 课本：从零理解递归自我改进（RSI）的发展和原理。
给我上一堂关于注意力机制的大学课，所有矩阵计算都用小数字走一遍。
把这篇论文讲给我听，先补必要前置，再推导核心方法。
```

---

## 它会怎么教

<table>
<tr>
<td width="50%" valign="top">

### 01 · 教授的知识路径
每章承接上章的问题。先知道为什么需要这个方法，再理解它怎样工作。

</td>
<td width="50%" valign="top">

### 02 · 教科书的推导密度
直觉、具体数字、正式定义逐层展开。关键步骤不藏在“显然”里。

</td>
</tr>
<tr>
<td valign="top">

### 03 · 实验课的动手能力
手算给完整中间量，代码给输入与输出。运行过才写“已验证”。

</td>
<td valign="top">

### 04 · 大学讲义的完整结构
分卷正文、解释图、阶梯附录、名词表、自测答案和来源导航一起交付。

</td>
</tr>
</table>

教学内核由作者的两套 Masterclass 工作流整理而来：**masterclass-textbook-writer** 与 **40页讲义写作**。新版类比规范、分卷机制、伪代码、数值核验和排版约束均已整合。[查看来源与规则取舍](docs/provenance.md)。

---

## 你会得到什么

| | 一堂大学课 | 深度技术教材 | 40 页通识讲义 |
| --- | --- | --- | --- |
| 适用 | 讲透一个问题 | 从机制走到实现 | 从零建立领域地图 |
| 体量 | 按目标收敛 | 约 25–35 页 | 约 40 页 |
| 主线 | 直觉、例子、推导 | 方法、手算、实现、边界 | 六卷递进，附录四件套 |
| 产物 | Markdown，可选 PDF | 讲义、源码、示例 | 分卷源码、PDF、验证记录 |

<sub>页数为写作目标，以最终编译结果为准。非技术主题使用案例、史料与论证，不强行加入数学或代码。</sub>

---

## 工作原理

```text
一个主题
   │
   ├── 定起点      读者基础 / 学习目标 / 输出档位
   ├── 建地图      前置依赖 / 符号表 / 来源核实
   ├── 写深度      直觉 → 手算 → 正式定义 → 实现
   ├── 分卷装订    章节衔接 / 机制图 / 附录四件套
   └── 验证交付    数值 / 代码 / 引用 / PDF 排版
```

**讲得清楚，算得出来，查得到来源。**

类比只留给真正的难点，正文保持平静专业。新知识先铺路，严格形式放进可继续钻研的附录。学习成效根据真实作答判断，不能由助手自行宣布。

---

## 一起把课讲好

最有价值的反馈是一句：“我在这一步没跟上。”

带上主题、基础和那一段讲解，提交 [Issue](https://github.com/walkinglabs/university-skill/issues)。贡献新的手算示例、纠正推导、检验代码，或用一个新主题测试教学流程。

[贡献指南](CONTRIBUTING.md) · [行为评估](evals/README.md) · [动画源文件](assets/hero.html)

---

## 灵感与致谢

- [女娲.skill](https://github.com/alchaincyf/nuwa-skill)：README 的叙事编排与开场动效形式。
- [达尔文.skill](https://github.com/alchaincyf/darwin-skill)：用实际任务验证改进的思路。
- [huashu-design](https://github.com/alchaincyf/huashu-design)：开场动画的设计与导出工作流。
- **Masterclass 两套源技能**：这套教学引擎的实际起点，详见 [溯源记录](docs/provenance.md)。

当前为初始化版本，不代表大学认证或真实教授授课；教学效果仍需实际学习验证。

<div align="center">
<br />
<strong>把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课。</strong>
<br />
<sub>Put a university professor in your AI. Turn any topic into a real university lecture.</sub>
<br /><br />
<sub>University.skill · Built by walkinglabs</sub>
</div>
