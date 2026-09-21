# TikZ 作图 Subagent 提示词模板

> **何时使用**：在 40 页长文中**画任何一幅 TikZ 配图之前**，把本文件的规则交给（或自己套用给）作图的 Subagent / 生成步骤。
> **为什么需要单独一份**：配图是最容易崩溃、最容易出界、也最容易拖慢进度的环节。把规则固化下来，可以避免每次都重新 debug。

---

## 一、调用接口（直接复制给 Subagent）

```text
请为《<文章标题>》绘制一幅 TikZ 配图，主题：<一句话说明这幅图要表达什么>。

硬性要求：
1. 只输出 \begin{figure}[htbp] ... \end{figure} 之间的完整代码，不要输出多余说明。
2. 必须在主文件已加载的 tikzlibrary 范围内作图（见下方「可用库清单」），
   禁止使用任何未加载的库（尤其是 decorations.pathmorphing / snaked 装饰）。
3. 所有坐标控制在 x ∈ [-8, 8]、y ∈ [-4, 4]；用 scale=0.85~0.95 缩放。
4. 每个方框的标题与正文写在同一个 node 的 {} 内部，并显式给出 text width。
5. 配色遵循下方「配色规范」，不要自创颜色。
```

---

## 二、可用库清单（务必核对，超范围必崩）

主文件 preamble 中实际加载的是：
```latex
\usetikzlibrary{arrows.meta,positioning,calc,shapes.geometric,patterns,
                decorations.pathreplacing,fit}
```

**可用**：`-{Stealth[...]}` 箭头、`positioning`、`calc`、`shapes.geometric`（circle/ellipse/diamond）、`patterns`、`decorations.pathreplacing`（花括号标注）、`fit`。

**不可用（会直接崩溃）**：
- `decorations.pathmorphing`（`snake`、`zigzag` 等装饰）——**坑王，已踩过一次**；
  需要波浪线时改用 **虚线 `dashed`** 或 `to[out=.., in=..]` 曲线代替。
- `shadows`、`fadings`、`mindmap`、`trees`、`automata`、`plotmarks`、`pgfplots`。

---

## 三、防崩溃铁律（按踩坑频率排序）

| # | 铁律 | 说明 |
|---|---|---|
| 1 | **不用未加载的库** | 见上表。最常犯的是 `snake` 装饰（需 `decorations.pathmorphing`，未加载→崩溃） |
| 2 | **数学符号必须包 `$...$`** | 节点文字里写 `\approx`、`\alpha`、`\neq` 而不包 `$` → `Missing $`（**高频坑**） |
| 3 | **节点名称必须纯字母数字** | 只能 `(nodeA)`、`(box1)`；**禁止** `(node_1)`、`(box-2)` |
| 4 | **特殊字符必须转义** | 下划线 `\_`、百分号 `\%`、与号 `\&`；如 `d\_model`、`100\%` |
| 5 | **有换行 `\\` 就必须声明 `align=` 或 `text width=`** | 否则 XeLaTeX 报 `Paragraph ended before \tikz@...`（**致命**） |
| 6 | **不用 `\foreach` 配复杂样式** | `\foreach` 与 `gray!55!white`、`above left=4pt` 组合曾触发解析失败；改用显式多条 `\draw` |
| 7 | **颜色只用规范表内的** | `blue!70!black` 等；不要自创自定义色 |
| 8 | **不用外部图片** | 全部 TikZ 原生绘制 |
| 9 | **节点内不用 `\texttt{中文}`** | 中文正常写即可（ctexart 已处理） |

---

## 四、防出界规则

1. **坐标预算（关键修正）**：**整图水平跨度应控制在 12 cm 以内**（A4 版心宽 16 cm，两侧留白）。
   实践上：x 方向可用约 **±6**，y 方向约 **±4**，配 `scale=0.9`。
   （早期版本写 ±8 偏宽，容易触发 `Overfull \hbox`。）
2. **方框必须给 `text width`，且 = `minimum width` − 0.5 cm**：
   ```latex
   \node[draw=blue!70!black, fill=blue!8, rectangle, rounded corners=3pt,
         minimum width=3.0cm, text width=2.5cm, inner sep=5pt, align=center] (a) at (-4,0)
       {{\small\bfseries 标题}\\{\tiny 说明文字}};
   ```
   内边距统一 `inner sep=5pt` 或 `6pt`。
3. **方框之间水平间距 ≥ 2.0 cm**：连线上的说明文字（如"启动子"、"Attention"）需要净空，
   否则文字会压在方框上。
4. **标题与正文写在同一 node 内**：严禁「先画空盒子、再在外面用 `\node at (box.north)` 放标题」——那种写法坐标一算错就出界（**坑王**）。
5. **标注文字单独放**：需要解释箭头的文字，用 `\node[font=\tiny] at (x,y) {...};`，位置放在**图形下方空白区**，不要压在线上。
6. **箭头统一**：`-{Stealth[length=5pt,width=4pt]}`；反馈/回流用 `dashed`。

---

## 五、配色规范

| 语义 | 代码 | 用途 |
|---|---|---|
| 输入 / 准备阶段 | `blue!70!black` 边 + `blue!8` 底 | 前置步骤 |
| 核心 / 关键步骤 | `purple!70!black` + `purple!8` | 主角、关键转折 |
| 输出 / 结果 | `green!70!black` + `green!8` | 产物、结论 |
| 警示 / 淘汰 / 反馈 | `red!70!black` + `red!8` | 失败项、反向箭头 |
| 中性 / 辅助 | `gray!70!black` + `gray!8` | 环境、基线 |
| 强调 | `orange!80!black` + `orange!8` | 最终交付、湿实验 |

箭头统一用 `-{Stealth[length=4pt]}`（细）或 `-{Stealth[length=6pt]}`（粗）。
虚线反馈加 `dashed`。

---

## 六、常用图表模板（直接改文字复用）

### 模板 A：横向流程（最多 5 个节点）
```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[scale=0.9]
  \node[draw=blue!70!black, fill=blue!8, rectangle, rounded corners=3pt,
        minimum width=2.7cm, text width=2.4cm, inner sep=4pt, align=center] (a) at (-5.6, 0.8)
      {{\tiny\bfseries ① 步骤一}\\{\scriptsize 说明}};
  \node[draw=purple!70!black, fill=purple!8, rectangle, rounded corners=3pt,
        minimum width=2.7cm, text width=2.4cm, inner sep=4pt, align=center] (b) at (-2.0, 0.8)
      {{\tiny\bfseries ② 步骤二}\\{\scriptsize 说明}};
  \node[draw=green!70!black, fill=green!8, rectangle, rounded corners=3pt,
        minimum width=2.7cm, text width=2.4cm, inner sep=4pt, align=center] (c) at (1.6, 0.8)
      {{\tiny\bfseries ③ 步骤三}\\{\scriptsize 说明}};
  \node[draw=orange!80!black, fill=orange!8, rectangle, rounded corners=3pt,
        minimum width=2.7cm, text width=2.4cm, inner sep=4pt, align=center] (d) at (5.2, 0.8)
      {{\tiny\bfseries ④ 步骤四}\\{\scriptsize 说明}};
  \draw[-{Stealth[length=4pt]}, thick] (a) -- (b);
  \draw[-{Stealth[length=4pt]}, thick] (b) -- (c);
  \draw[-{Stealth[length=4pt]}, thick] (c) -- (d);
\end{tikzpicture}
\caption{<图注：一句话讲清这幅图的因果链>}
\label{fig:<label>}
\end{figure}
```

### 模板 B：对比图（左右并置，**不要**用 `xshift` + `scale` 组合）
> **坑**：并排子图用 `xshift` 会与外层 `scale` 复合导致坐标算错、图形重叠。
> **正确做法**：全部节点写在**同一个坐标系**里，用不同的 x 坐标区分左右。

```latex
\begin{tikzpicture}[scale=0.9]
  % 左侧
  \node[draw=blue!70!black, fill=blue!8, circle, minimum size=0.85cm] (A) at (-5.4, 1.4) {\small A};
  \node[draw=blue!70!black, fill=blue!8, circle, minimum size=0.85cm] (B) at (-5.4, -0.6) {\small B};
  \draw[-{Stealth[length=5pt]}, thick, blue!80!black] (A) -- (B);
  \node[font=\tiny] at (-5.4, -1.6) {(a) 情形一};

  % 右侧（同一坐标系，只是 x 不同）
  \node[draw=red!70!black, fill=red!8, circle, minimum size=0.85cm] (C) at (0, 1.4) {\small C};
  \node[draw=red!70!black, fill=red!8, circle, minimum size=0.85cm] (D) at (2, 0) {\small D};
  \draw[-{Stealth[length=5pt]}, thick, red!80!black] (C) -- (D);
  \node[font=\tiny] at (1, -1.6) {(b) 情形二};
\end{tikzpicture}
```

### 模板 C：坐标图 / 曲线（用于能垒、复杂度、函数形状）
```latex
\begin{tikzpicture}[scale=0.95]
  \draw[-{Stealth[length=5pt]}, thin] (-4.5,0) -- (4.5,0) node[right] {\tiny $x$};
  \draw[-{Stealth[length=5pt]}, thin] (0,-2) -- (0,3) node[above] {\tiny $y$};
  \draw[thick, blue!70!black] (-4, 0) to[out=10, in=170] (0, 2.2) to[out=-10, in=185] (4, -1.2);
  \filldraw[red!80!black] (0, 2.2) circle (2.5pt);
  \node[font=\tiny, text=red!80!black, align=center] at (0, 2.8) {峰值 / 过渡态};
\end{tikzpicture}
```

### 模板 D：漏斗 / 层级（用于设计流水线、筛选流程）
用上下堆叠的**梯形**（左右两条斜边 + 上下两条横线），配合逐步变窄的宽度表达"层层收缩"。

---

## 七、自检清单（画完立刻过一遍）

- [ ] 用到所有 tikzlibrary 都在「可用库清单」内？
- [ ] 所有坐标在 x ∈ [-8, 8]、y ∈ [-4, 4]？
- [ ] 每个 node 都给了 `text width`？
- [ ] 标题与正文在**同一个** node 内？
- [ ] 节点文字里的数学符号都包了 `$...$`？
- [ ] 没用 `\foreach` + 复杂样式的组合？
- [ ] 颜色都在「配色规范」表内？
- [ ] 图注（caption）一句话讲清了因果链？
- [ ] `\label` 已给且正文有对应的 `\ref`？
