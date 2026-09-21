# LaTeX 与视觉验收

使用 [模板](../assets/lecture-template.tex)，正文逐卷放 parts/。检测 tectonic 或 XeLaTeX，不写死本机路径；选择当前环境可用的中文字体。

- 统一 algorithm + algpseudocode，使用 \Require、\Ensure、\State、\For、\EndFor。不得混入 algorithmic 的全大写命令。
- 算法浮动体不放教学盒。循环范围用数学或 \textbf{to}，不使用未定义的 \TO。
- 数学符号放数学环境；正文标识符用 \texttt 并转义下划线。多行公式用 align。
- DOI/URL 用 \url 或 \href{...}{\nolinkurl{...}}，避免长不可断行文本。
- 表宽含列间距不得超过版心。跨页表用 longtable 或拆分。附录使用 \appendix。
- TikZ 标题和内容在同一节点，显式 text width、align、inner sep；带字连线留净空。先算总宽，再排图，不能缩小到看不清。
- 教学盒仅用于解释、练习、小结和必要提示；小结不堆 DOI 和参数。

运行编译并保留日志；XeLaTeX 重跑到引用稳定，Tectonic 按自动轮次处理。清除致命错误、缺字、未定义引用和 ≥10pt Overfull，其余溢出也需目视判断。

用 pdfinfo 或 PDF 解析器统计页数，不能扫描压缩文件猜页数。渲染并检查封面、目录、密集公式、最长表格、代码、图和附录。记录检查页码；未渲染不能报告视觉验收通过。
