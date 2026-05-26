---
description: 阶段3：规格生成 - 组装完整PRD和前端Demo
---

# Workflow: Phase 3 - 规格生成 (Make Specs)

此工作流是**最后一步**。前两步的思考和设计已经完成，现在是"组装"和"输出"。

## 步骤 1: 生成PRD (PRD Generation)

1. 读取 Phase 2 的《核心方案设计草稿》。
2. 填充到 `templates/prd-template.md` 中。
3. 确保所有业务规则都有编号 (R01, R02...)。
4. 确保包含"异常处理"和"权限说明"章节。

## 步骤 2: 生成前端Demo (Optional)

> **Goal**: 将PRD转化为可视化的代码。

如果需要前端Demo：

1. 调用 **Skill: `frontend-designer`** (如有) 或基于Design System规范。
2. 为PRD中的关键页面生成 React/Tailwind 代码。
3. 确保生成的代码包含 `interface` 定义和 `mock` 数据。

## 步骤 3: 交付与归档 (Delivery)

1. 将最终PRD保存到 `prds/[模块名]/PRD.md`。
2. 将Demo代码保存到 `prds/[模块名]/demo/`。
3. 输出一份《验收标准清单(AC List)》供测试使用。

**Done**: 任务完成！
