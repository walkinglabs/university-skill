# 初始化验证记录

验证日期：2026-09-21。

| 项目 | 实际结果 |
| --- | --- |
| 技能结构 | skill-creator 的 quick_validate.py 返回 Skill is valid |
| 手算示例 | 标准库脚本实跑；三个步长的参数与损失断言通过，有限差分梯度与解析梯度一致 |
| LaTeX 模板 | Tectonic 成功生成 PDF；这是空讲义骨架的编译检查，不是完整教材验收 |
| 模板警告 | macOS 系统字体路径可移植性、系统字体 ToUnicode 映射、algorithm.sty 注释编码警告；未宣称零警告 |
| 动画 | huashu-design seek 渲染脚本导出 216 帧，18 秒，960×540，12fps；FFmpeg 调色板优化 GIF 约 1.6 MB |
| 视觉 | 检查 GIF 六个时间点与浏览器预览；书籍、文字、场景均有内容，无空白镜头 |
| README | 本地 Markdown 渲染预览，桌面及 390px 手机检查；GIF 和徽章加载成功，手机 scrollWidth = innerWidth = 390 |
| Git | diff --check 通过；按维护者要求提交并推送至 origin/main |

仓库现收录两份既有完整成品作为输出参考：47 页蛋白质结构设计 AI4S 课本，以及 13 页 Muon 优化器课本。已核对 PDF 格式、A4 页面、页数、全页缩略图及代表页截图。蛋白质课本原文件第 23、38–41 页使用了未嵌入的 STFangsong 字体；公开副本已修复多版本对照示例，将代码块换成清晰的英文注释，并以高分辨率重新封装这五页。正文内容、公式和页数保持不变，最终 PDF 不再引用缺失字体。两份课本不是本次初始化过程中重新生成的作品。尚未进行学习者效果实验、独立模型行为回归或跨运行时兼容测试。evals 中的场景是后续执行的测试方案，不是通过报告。

## 动画复现

保留 assets/hero.html 作为可编辑源，assets/hero.mp4 为中间视频，assets/hero.gif 为 README 成品。安装 Playwright 和 FFmpeg 后，使用 huashu-design 的 scripts/render-video-seek.js，参数为 --duration=18 --fps=12 --width=960 --height=540，再通过 FFmpeg palettegen/paletteuse 转换 GIF。无须远程字体或图片。

本地 README 预览在 docs/readme-preview.html，接近 GitHub 排版，实际 GitHub 渲染仍以推送后页面为准。

## 定位修订

README 中英文首屏、图片替代文本与动画收尾统一为维护者指定的“把一位大学教授装进你的 AI，把任何主题变成一堂真正的大学课”。示例加入蛋白质结构设计 AI4S、JEPA、RSI 的 PDF 课本请求，RSI 歧义在示例中先澄清。更新动画后重新导出，检查结尾文字布局。
