# 产品经理使用AI IDE（进阶与实战）

> **项目版本**：V1.0  
> **创建日期**：2026-01-31  
> **维护者**：Vitamin

---

## 📖 项目简介

这是一个帮助产品经理使用AI IDE完成**日常工作全流程**的知识库和工作空间。提供标准化的模板、工作流、Skills技能包和最佳实践。

### 🎯 核心能力矩阵

| 工作阶段     | 支持能力                                 | 代表性输出                 |
| :----------- | :--------------------------------------- | :------------------------- |
| **需求管理** | 需求澄清、JTBD分析、RDD生成、优先级评估  | 需求定义卡片、影响范围分析 |
| **方案设计** | 数据建模、流程设计、状态机设计、风险探测 | ER图、字段清单、流程图     |
| **文档撰写** | PRD、API文档、用户手册、变更说明         | 完整PRD、接口文档          |
| **原型开发** | 前端Demo、UI效果图、交互流程             | React/Vue代码、Mermaid图   |
| **质量保障** | 自检清单、逻辑验证、边界探测、测试用例   | 验收标准、测试计划         |
| **沟通协作** | 评审PPT、汇报材料、交接文档              | 演示文稿、操作手册         |
| **知识沉淀** | 经验归档、术语表、最佳实践库             | 项目知识库、设计模式       |

### 🔄 工作流全覆盖

从一句话需求到最终交付的完整链路：

```
用户需求 → Phase 1（需求洞察） → Phase 2（方案架构） → Phase 3（规格生成） → Phase 4（验证迭代） → 正式交付
```

- **Phase 1 需求洞察**：拒绝伪需求，输出RDD需求定义卡片
- **Phase 2 方案架构**：数据模型+流程设计+风险探测
- **Phase 3 规格生成**：完整PRD+前端Demo
- **Phase 4 验证迭代**：自检优化，确保质量

---

## 🗂️ 项目结构

```
产品经理使用IDE（进阶与实战）/
├── .agent/                    # ⭐ AI配置中心（强制推荐）
│   ├── rules/                 # 项目规则（PRD规范、前端规范等）
│   ├── skills/                # AI技能包（可复用的专项能力）
│   └── workflows/             # 标准工作流（/create-prd等）
├── analysis/                  # 业务分析区（建议，可选）
│   ├── data-analysis/         # 数据分析（成品或原始材料）
│   ├── process-simulation/    # 流程推演（确认版或草稿）
│   └── scope-analysis/        # 影响范围分析
├── assets/                    # 资源文件库（建议，可选）
│   ├── images/                # 图片素材
│   ├── icons/                 # 图标
│   ├── mockups/               # 原型图、设计稿
│   └── diagrams/              # 流程图、架构图源文件
├── context/                   # 项目上下文（建议，可选）
│   ├── 01-project-background.md    # 项目背景
│   ├── 02-target-audience.md       # 目标用户
│   ├── 03-core-strategy.md         # 核心策略
│   ├── 04-business-logic.md        # 业务逻辑
│   └── 05-term-glossary.md         # 术语表
├── docs/                      # 参考文档库（建议，可选）
│   ├── 01-reference/          # 参考资料
│   └── 02-other-docs/         # 其他文档
├── drafts/                    # 草稿区（建议，可选）
├── outputs/                   # 最终交付物（建议，可选）
│   ├── client-prds/           # 对外交付的PRD
│   ├── presentations/         # 汇报演示材料
│   ├── handoff-docs/          # 交接文档
│   └── archive/               # 归档
├── prds/                      # 正式PRD输出区（建议，可选）
├── prompts/                   # 提示词库（建议，可选）
├── templates/                 # 模板库（建议，可选）
│   ├── prd-template.md              # PRD标准模板
│   ├── field-list-template.md       # 字段清单模板
│   ├── business-process-template.md # 业务流程推演模板
│   └── frontend-style-guide.md      # 前端样式规范
├── AGENT.md                   # ⭐ 全局知识库（强制推荐）
└── README.md                  # 本文件
```

> **📌 关于文件夹结构的灵活性**
>
> - **强制推荐**：`.agent/`和`AGENT.md`是核心配置，建议保留
> - **灵活可选**：其他文件夹可根据实际需求选择性创建
> - **命名自由**：除了`.agent/`和`AGENT.md`外，其他文件夹命名可以自由发挥，不必严格使用英文，可以使用中文或自定义名称

---

## 🚀 快速开始

### 1. 了解项目

首次使用请阅读以下文档：

1. **AGENT.md**：全局知识库，包含项目演进日志、最佳实践、FAQ
2. **context/01-project-background.md**：项目背景和目标
3. **.agent/rules/project.md**：项目规则和输出规范

### 2. 熟悉工作流

本项目提供4个标准工作流：

| 工作流       | 用途               | 命令                    |
| ------------ | ------------------ | ----------------------- |
| 创建PRD      | 从需求到完整PRD    | `/create-prd`           |
| 创建字段清单 | 快速整理字段定义   | `/create-field-list`    |
| 创建前端Demo | 生成前端原型代码   | `/create-frontend-demo` |
| 业务分析推演 | 分析业务流程和影响 | `/analyze-business`     |

### 3. 第一个PRD

**示例对话**：

```
@AGENT.md @context/01-project-background.md

我需要为"采购订单"模块创建PRD文档，业务需求如下：
- 采购部门向供应商采购商品
- 订单包含主表和明细表
- 支持草稿、已确认、已完成等状态

请使用/create-prd工作流帮我生成。
```

### 4. 生成前端Demo

**示例对话**：

```
@prds/purchase-order/PRD.md

请基于这个PRD生成前端Demo，包括列表页和详情页。
使用/create-frontend-demo工作流。
```

---

## 💡 核心功能

### 📝 PRD文档撰写

**特点**：

- 标准化模板，包含所有必需章节
- 业务规则编号管理（R01、R02...）
- 状态流转必须闭环
- 自动质量检查

**工作流**：`/create-prd`  
**模板**：`templates/prd-template.md`

---

### 📊 字段清单整理

**特点**：

- 标准表格格式
- 类型定义准确（String、Number、Enum等）
- 枚举值列举完整
- 支持嵌套结构

**工作流**：`/create-field-list`  
**模板**：`templates/field-list-template.md`

---

### 🎨 前端Demo生成

**特点**：

- TypeScript类型定义完整
- Mock数据真实合理
- 遵循统一的Design System
- 代码可直接运行

**工作流**：`/create-frontend-demo`  
**规范**：`templates/frontend-style-guide.md`

---

### 🔄 业务流程分析

**特点**：

- Mermaid流程图可视化
- 数据推演step by step
- 边界场景和异常处理完整
- 影响范围分析全面

**工作流**：`/analyze-business`  
**模板**：`templates/business-process-template.md`

---

## 📚 核心文档

### 必读文档

- **AGENT.md**：全局知识库，项目经验和最佳实践
- **context/01-project-background.md**：项目背景
- **.agent/rules/project.md**：项目规则

### 模板文档

- **templates/prd-template.md**：PRD标准模板
- **templates/field-list-template.md**：字段清单模板
- **templates/business-process-template.md**：业务流程推演模板
- **templates/frontend-style-guide.md**：前端样式规范

### 工作流文档

- **.agent/workflows/create-prd.md**：创建PRD工作流
- **.agent/workflows/create-field-list.md**：创建字段清单工作流
- **.agent/workflows/create-frontend-demo.md**：创建前端Demo工作流
- **.agent/workflows/analyze-business.md**：业务分析推演工作流

---

## 🎯 使用技巧

### 1. 充分利用上下文

使用`@`引用文档，帮助AI理解需求：

```
@AGENT.md @context/01-project-background.md @context/04-business-logic.md

[你的需求]
```

### 2. 使用工作流

通过工作流固化最佳实践：

```
请使用/create-prd工作流生成采购订单的PRD文档
```

### 3. 草稿与正式分离

- AI生成的初稿放在`drafts/`
- 审核通过后移至`prds/`
- 支持快速试错和迭代

### 4. 持续沉淀知识

在`AGENT.md`中记录：

- 项目重要决策
- 遇到的问题和解决方案
- 发现的最佳实践

---

## ⚙️ 文件夹说明

### `.agent/` - AI配置中心（⭐强制推荐）

告诉AI如何理解项目、如何工作

- **rules/**：项目规则和输出规范
- **workflows/**：标准化工作流程
- **skills/**：AI技能包，可复用的专项能力（如字段清单生成、前端Demo生成等）

### `AGENT.md` - 全局知识库（⭐强制推荐）

项目演进日志、最佳实践、经验教训的集中记录

### `context/` - 项目上下文（建议）

AI理解业务的基础知识库

### `templates/` - 模板库（建议）

标准化输出格式，确保文档质量

### `drafts/` - 草稿区（建议）

AI生成的初稿，支持快速试错

### `prds/` - 正式输出区（建议）

经过审核的正式文档

### `outputs/` - 最终交付物（建议）

对外交付或正式归档的最终文档，包括：

- **client-prds/**：交付给客户或上级的正式PRD
- **presentations/**：汇报演示材料
- **handoff-docs/**：开发交接、测试说明等文档

### `assets/` - 资源文件库（建议）

统一管理项目中的静态资源，包括：

- **images/**：截图、UI效果图、图表
- **icons/**：图标资源
- **mockups/**：原型图、设计稿
- **diagrams/**：流程图、架构图源文件

### `analysis/` - 业务分析区（建议）

存放业务分析、需求分析相关内容，包括：

- **成品文件**：已完成的分析报告、确认的需求文档
- **原始资料**：待整理的需求素材、初步的业务调研记录
- **工作底稿**：分析过程中的推演草稿

> **💡 提示**：除了`.agent/`和`AGENT.md`，其他文件夹都是建议性的，可以根据你的工作习惯自由调整或删减。文件夹命名也可以自定义，不必拘泥于英文。

---

## 📋 输出规范

### PRD文档规范

- ✅ 包含所有必需章节（异常处理、取消规则、权限说明等）
- ✅ 业务规则编号管理（R01、R02...）
- ✅ 状态流转必须闭环（含正向和逆向）
- ✅ 复杂逻辑使用Mermaid流程图

详见：`.agent/rules/project.md`

### 字段清单规范

- ✅ 使用标准表格格式
- ✅ 类型定义准确
- ✅ 枚举值列举完整
- ✅ 嵌套结构说明清楚

详见：`templates/field-list-template.md`

### 前端Demo规范

- ✅ TypeScript类型定义完整
- ✅ Mock数据真实合理
- ✅ 遵循Design System
- ✅ 代码可运行

详见：`templates/frontend-style-guide.md`

---

## 🔄 工作流程

### 标准流程

```
需求分析 → 字段清单 → 业务规则 → PRD撰写 → 前端Demo → 需求评审
```

### 详细步骤

1. **需求分析**：使用`/analyze-business`分析业务流程
2. **字段清单**：使用`/create-field-list`整理字段
3. **PRD撰写**：使用`/create-prd`生成PRD
4. **前端Demo**：使用`/create-frontend-demo`生成Demo
5. **需求评审**：使用PRD和Demo进行评审

---

## ❓ 常见问题

### Q: 如何开始第一个任务？

**A**:

1. 阅读`AGENT.md`和项目背景
2. 使用`/create-field-list`生成字段清单
3. 使用`/create-prd`生成PRD文档

### Q: 如何让AI更好地理解需求？

**A**:

1. 使用`@AGENT.md`引用全局知识库
2. 使用`@context/`引用项目背景
3. 提供充足的业务上下文

### Q: 如何确保文档质量？

**A**:

1. 使用标准模板
2. 遵循项目规则
3. 使用质量检查清单

更多问题见：`AGENT.md` → 常见问题FAQ

---

## 🚧 下一步计划

- [ ] 创建第一个PRD文档
- [ ] 生成第一个前端Demo
- [ ] 根据项目完善`context/04-business-logic.md`
- [ ] 在`AGENT.md`中沉淀项目经验

---

## 📞 联系方式

**维护者**：Vitamin  
**更新日期**：2026-01-31

---

## 📄 许可证

本项目为个人知识库项目，仅供参考学习。
