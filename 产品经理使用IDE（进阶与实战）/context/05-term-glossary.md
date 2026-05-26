# 术语表

> **最后更新**：2026-01-31  
> **维护者**：Vitamin

---

## 文档管理术语

| 术语     | 英文                          | 说明                            |
| -------- | ----------------------------- | ------------------------------- |
| PRD      | Product Requirements Document | 产品需求文档                    |
| 字段清单 | Field List                    | 数据实体的字段定义文档          |
| 工作流   | Workflow                      | 固化的工作流程，如create-prd    |
| 技能包   | Skill                         | 可复用的AI技能，如字段清单转PRD |
| 模板     | Template                      | 标准化的文档模板                |
| Demo     | Demo/Prototype                | 前端原型/演示代码               |

---

## 项目文件夹术语

| 术语         | 英文          | 路径              | 说明                                       |
| ------------ | ------------- | ----------------- | ------------------------------------------ |
| 配置中心     | Agent Config  | .agent/           | AI配置文件夹，包含rules、workflows、skills |
| 项目规则     | Project Rules | .agent/rules/     | 项目级规则，如PRD规范                      |
| 工作流文件夹 | Workflows     | .agent/workflows/ | 工作流定义文件                             |
| 技能文件夹   | Skills        | .agent/skills/    | 技能包定义文件                             |
| 上下文       | Context       | context/          | 项目背景和业务逻辑                         |
| 模板库       | Templates     | templates/        | 标准模板文件                               |
| 草稿区       | Drafts        | drafts/           | AI生成的初稿                               |
| 正式输出区   | PRDs          | prds/             | 经过审核的正式文档                         |
| 分析区       | Analysis      | analysis/         | 业务分析文档                               |
| 提示词库     | Prompts       | prompts/          | 常用提示词                                 |

---

## 单据管理术语

| 术语      | 英文            | 说明                              |
| --------- | --------------- | --------------------------------- |
| 单据      | Document        | 业务单据，如订单、入库单等        |
| 主单据    | Master Document | 被关联的单据                      |
| 从单据    | Sub Document    | 关联主单据的单据                  |
| 单头      | Header          | 单据的主表信息                    |
| 单行/明细 | Line/Detail     | 单据的明细信息                    |
| 单据编号  | Document Code   | 单据的唯一标识，如PO-20260131-001 |

---

## 状态管理术语

| 术语   | 英文      | 说明             |
| ------ | --------- | ---------------- |
| 草稿   | Draft     | 初始状态，可编辑 |
| 待审核 | Pending   | 已提交待审核状态 |
| 已审核 | Approved  | 审核通过状态     |
| 已驳回 | Rejected  | 审核驳回状态     |
| 生效   | Active    | 已生效状态       |
| 已完成 | Completed | 业务完成状态     |
| 已关闭 | Closed    | 关闭状态         |
| 已取消 | Cancelled | 取消状态         |

---

## 数据类型术语

| 术语     | 英文      | 说明         | 示例                  |
| -------- | --------- | ------------ | --------------------- |
| 字符串   | String    | 文本类型     | "张三"                |
| 数值     | Number    | 数字类型     | 100, 99.99            |
| 布尔值   | Boolean   | 真假值       | true, false           |
| 日期     | Date      | 日期类型     | 2026-01-31            |
| 日期时间 | DateTime  | 日期时间类型 | 2026-01-31 10:00:00   |
| 枚举     | Enum      | 固定可选值   | Draft, Active, Closed |
| 数组     | Array     | 数组类型     | [{...}, {...}]        |
| 对象     | Object    | 对象类型     | {key: value}          |
| 引用     | Reference | 引用其他实体 | Ref<User>             |

---

## 业务规则术语

| 术语     | 英文              | 说明                 |
| -------- | ----------------- | -------------------- |
| 业务规则 | Business Rule     | 业务处理的逻辑和约束 |
| 验证规则 | Validation Rule   | 数据验证的规则       |
| 计算规则 | Calculation Rule  | 数据计算的公式       |
| 流转规则 | Transition Rule   | 状态流转的条件       |
| 取消规则 | Cancellation Rule | 单据取消的规则       |
| 关闭规则 | Closing Rule      | 单据关闭的规则       |

---

## 前端开发术语

| 术语          | 英文          | 说明                               |
| ------------- | ------------- | ---------------------------------- |
| 列表页        | List Page     | 数据列表页面                       |
| 详情页        | Detail Page   | 数据详情页面                       |
| 表单页        | Form Page     | 数据编辑表单页面                   |
| 筛选区        | Filter Bar    | 列表页的筛选条件区域               |
| 操作按钮      | Action Button | 页面操作按钮                       |
| 表格          | Table         | 数据表格组件                       |
| 分页          | Pagination    | 分页组件                           |
| Modal         | Modal/Dialog  | 弹窗组件                           |
| Toast         | Toast/Message | 提示信息组件                       |
| Badge         | Badge         | 状态标签组件                       |
| Design System | Design System | 设计系统，包含颜色、字体、组件规范 |
| Mock数据      | Mock Data     | 模拟数据                           |
| TypeScript    | TypeScript    | 带类型的JavaScript                 |

---

## 权限管理术语

| 术语     | 英文              | 说明                         |
| -------- | ----------------- | ---------------------------- |
| 角色     | Role              | 用户角色，如管理员、操作员   |
| 权限     | Permission        | 操作权限，如新增、编辑、删除 |
| 权限矩阵 | Permission Matrix | 角色与权限的对应表           |
| 管理员   | Administrator     | 系统管理员                   |
| 操作员   | Operator          | 业务操作人员                 |
| 审核员   | Approver          | 业务审核人员                 |

---

## 流程分析术语

| 术语     | 英文             | 说明             |
| -------- | ---------------- | ---------------- |
| 流程图   | Flowchart        | 业务流程图       |
| 序列图   | Sequence Diagram | 系统交互序列图   |
| 状态图   | State Diagram    | 状态流转图       |
| 关键节点 | Key Node         | 流程中的关键步骤 |
| 边界场景 | Edge Case        | 边界值场景       |
| 异常场景 | Exception Case   | 异常情况场景     |
| 影响范围 | Impact Scope     | 变更的影响范围   |

---

## AI协作术语

| 术语   | 英文      | 说明                 |
| ------ | --------- | -------------------- |
| AI IDE | AI IDE    | AI辅助的集成开发环境 |
| 提示词 | Prompt    | 给AI的指令或问题     |
| 上下文 | Context   | AI理解问题的背景信息 |
| 工作流 | Workflow  | 固化的AI协作流程     |
| 技能包 | Skill     | 可复用的AI能力       |
| 引用   | Reference | 使用@引用文档或代码  |
| 草稿   | Draft     | AI生成的初稿         |
| 迭代   | Iteration | 多次调整优化         |

---

## 质量管理术语

| 术语     | 英文            | 说明                     |
| -------- | --------------- | ------------------------ |
| 检查清单 | Checklist       | 质量检查的清单           |
| 必填项   | Required Field  | 必须填写的字段           |
| 可选项   | Optional Field  | 可选填写的字段           |
| 数据验证 | Data Validation | 数据有效性检查           |
| 格式化   | Formatting      | 数据格式化，如日期、金额 |
| 边界值   | Boundary Value  | 数据的边界值             |
| 空值     | Null/Empty      | 空值或未填写             |

---

## 数据计算术语

| 术语       | 英文                     | 说明                    |
| ---------- | ------------------------ | ----------------------- |
| 汇总       | Sum                      | 求和                    |
| 平均值     | Average                  | 平均数                  |
| 最大值     | Maximum                  | 最大值                  |
| 最小值     | Minimum                  | 最小值                  |
| 四舍五入   | Rounding                 | 数值四舍五入            |
| 千分位     | Thousand Separator       | 数字千分位格式，如1,234 |
| 小数位     | Decimal Places           | 小数保留位数            |
| 最大余额法 | Maximum Remainder Method | 数量分配算法            |

---

## 系统术语

| 术语 | 英文                              | 说明                 |
| ---- | --------------------------------- | -------------------- |
| ERP  | Enterprise Resource Planning      | 企业资源计划系统     |
| WMS  | Warehouse Management System       | 仓储管理系统         |
| OMS  | Order Management System           | 订单管理系统         |
| POS  | Point of Sale                     | 销售终端系统         |
| SKU  | Stock Keeping Unit                | 库存量单位，商品编码 |
| API  | Application Programming Interface | 应用程序接口         |

---

## 使用建议

### 术语使用原则

1. **专业术语保持英文**：如PRD、SKU、API等
2. **中英文对照**：首次出现时中英文对照，后续使用中文
3. **团队统一**：团队内部使用统一的术语
4. **避免歧义**：同一概念使用同一术语

### 术语更新

- 发现新术语时及时补充到本文档
- 定期回顾和更新术语表
- 团队共识后再使用新术语

---

**说明**：本文档定义了项目中使用的所有专业术语，帮助AI和团队成员准确理解业务概念。
