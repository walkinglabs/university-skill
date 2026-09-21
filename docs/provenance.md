# 教学内核溯源

按维护者指定的 LifeGuide 内两份技能初始化：

| 源技能 | 继承 |
| --- | --- |
| D2L风格深度学习教材生成器 / masterclass-textbook-writer | 因果链、三阶认知、单步手算、实现验证、分卷写作 |
| D2L风格深度学习教材生成器 / 40页讲义写作 v2 | 高中起点、克制讲义语气、难点类比、附录四件套、引用与排版验收 |

已阅读两个 SKILL.md 和各自主内容模板；必要规范重新整理为本仓库相对引用，运行不依赖 LifeGuide 目录。

## 修订选择

- 旧模板要求逐概念大量类比；采用较新 v2 的难点类比与 15–25 盒指导。
- 两套伪代码包冲突，统一 algorithm + algpseudocode。
- allclose 改为容差一致性，不能称零误差。
- PDF 页数用解析器统计，不扫描压缩对象猜测。
- 无 DOI 与未核实分开，允许书籍、史料和官方文档。
- 原技能历史验证成绩不迁移成本项目实测成绩；字数和密度用于诊断。

README 编排参考 [nuwa-skill](https://github.com/alchaincyf/nuwa-skill)，评估思路参考 [darwin-skill](https://github.com/alchaincyf/darwin-skill)。动画依据 [huashu-design](https://github.com/alchaincyf/huashu-design) 分镜与确定性导出规范制作，内容为 University.skill 定制。
