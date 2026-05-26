# PRD正式输出区 (PRDs)

本文件夹用于存放**经过验证的正式需求文档**。这是给开发团队、测试团队使用的"标准交付物"。

---

## 📍 使用场景

### 什么时候用这个文件夹？

- ✅ drafts/中的PRD通过Phase 4验收后
- ✅ 需要给开发团队提供正式需求文档
- ✅ 需求进入开发排期前
- ✅ 需要版本化管理PRD文档

### prds/ vs outputs/ 的区别

| 维度         | prds/                 | outputs/                     |
| :----------- | :-------------------- | :--------------------------- |
| **受众**     | 内部团队（开发/测试） | 外部（客户/上级/跨团队）     |
| **内容**     | 需求文档为主          | 各类成品（PRD/PPT/汇报材料） |
| **格式**     | 详细技术规格          | 精美可演示                   |
| **更新频率** | 随开发迭代更新        | 里程碑交付                   |

---

## 📁 文件夹组织

按**模块**组织，每个模块包含完整的文档集：

### 标准结构

```
prds/
├── purchase-order/                # 采购订单模块
│   ├── PRD.md                    # 主PRD文档
│   ├── field-list.md             # 字段清单
│   ├── business-logic.md         # 业务逻辑说明（可选）
│   └── demo/                     # 前端Demo代码（可选）
│       ├── list.tsx
│       ├── detail.tsx
│       └── README.md
├── inventory-management/          # 库存管理模块
│   ├── PRD.md
│   └── field-list.md
└── archive/                       # 归档文件夹
    └── old-purchase-order-20260115/
```

---

## 📋 标准文件清单

### 必需文件

#### PRD.md

完整的产品需求文档

**必须包含章节**：

- 需求背景与目标
- 功能清单
- 字段说明
- 业务规则
- 状态与流转
- 页面与交互
- 异常处理
- 权限说明

**参考模板**：`templates/prd-template.md`

---

#### field-list.md

字段清单

**必须包含信息**：

- 字段名（中英文）
- 类型（精确到Decimal(18,2)）
- 必填/可选
- 枚举值（完整列出）
- 嵌套结构说明

**参考模板**：`templates/field-list-template.md`

---

### 可选文件

#### business-logic.md

**复杂业务逻辑说明**

适用场景：

- 业务规则特别复杂
- 涉及多系统交互
- 需要单独说明的流程

---

#### demo/

**前端Demo代码**

包含内容：

- TypeScript接口定义
- React组件（列表页、详情页）
- Mock数据
- README说明

**风格规范**：`templates/frontend-style-guide.md`

---

## ✅ 文档审核标准

### PRD文档

- [ ] 包含所有必需章节
- [ ] 业务规则已编号（R01, R02...）
- [ ] 状态流转已闭环（含正向/逆向/异常）
- [ ] 字段清单格式正确
- [ ] 异常处理、取消规则、权限说明完整
- [ ] 通过Phase 4自检清单

### 字段清单

- [ ] 表格格式规范
- [ ] 类型定义精确（非模糊类型）
- [ ] 枚举值列举完整
- [ ] 嵌套结构说明清楚
- [ ] 包含审计字段（created_by, updated_at等）

### 前端Demo

- [ ] TypeScript类型定义完整
- [ ] Mock数据真实合理
- [ ] 样式符合Design System
- [ ] 代码可运行（npm run dev通过）

---

## 📌 版本管理

### 版本号规则

PRD文档使用语义化版本号：

- **V1.0**：初始版本
- **V1.1**：小改动（字段调整、规则优化、bug修复）
- **V2.0**：大改动（流程变更、功能新增、架构调整）

### 修订记录

每次更新必须在PRD底部记录：

```markdown
## 修订记录

| 版本 | 日期       | 修订内容                   | 修订人  |
| ---- | ---------- | -------------------------- | ------- |
| V1.0 | 2026-01-31 | 初始版本                   | Vitamin |
| V1.1 | 2026-02-05 | 新增取消规则，优化字段说明 | Vitamin |
| V2.0 | 2026-02-15 | 重构状态机，新增审批流程   | Vitamin |
```

---

## 🔄 文档更新流程

### 更新步骤

1. 在`drafts/`中修改（不要直接改prds/）
2. 使用`/4-verify-iterate`验证
3. 更新版本号和修订记录
4. 覆盖`prds/`中的对应文件

### 重大变更

如果是V2.0级别的大改动：

1. 将旧版本移至`archive/`
2. 命名格式：`[module-name]-v1.0-20260131/`
3. 新版本放在`prds/[module-name]/`

---

## 📂 模块命名规范

模块文件夹使用**小写英文 + 连字符**：

✅ **正确**：

- `purchase-order`
- `inventory-management`
- `warehouse-receipt`

❌ **错误**：

- `PurchaseOrder`（驼峰）
- `inventory_management`（下划线）
- `采购订单`（中文）

---

## 🔄 文件流转

### drafts → prds

**条件**：

- 通过`/4-verify-iterate`自检
- 人工review确认

**操作**：

```bash
# 从drafts移动到prds，并重命名为模块名
mv drafts/2026-02-01-采购订单/ prds/purchase-order/
```

---

### prds → outputs

**条件**：

- 需要对外交付（客户/上级）
- 里程碑交付物

**操作**：

```bash
# 复制到outputs（不是移动，prds保留）
cp -r prds/purchase-order/PRD.md outputs/client-prds/采购订单PRD_v1.0_20260201.md
```

---

### prds → archive

**条件**：

- 需求废弃
- 大版本重构（V2.0替代V1.0）
- 系统下线

**操作**：

```bash
mv prds/purchase-order/ prds/archive/purchase-order-v1.0-20260131/
```

---

## 💡 最佳实践

### 1. 从drafts推进

不要手动创建prds/文件夹，应该从drafts/验收通过后移入。

### 2. 保持文档完整性

每个模块至少包含：`PRD.md` + `field-list.md`

### 3. 及时更新修订记录

每次修改PRD，必须在"修订记录"章节记录变更。

### 4. 版本化思维

重大变更时，旧版本归档，新版本独立维护。

---

## 🎯 质量检查清单

将文档移入prds/前，使用以下清单：

### 逻辑完整性

- [ ] 状态流转闭环（无死胡同）
- [ ] 异常处理覆盖（网络超时、并发冲突）
- [ ] 业务规则编号管理

### 数据规范性

- [ ] 字段类型精确（Decimal vs Double）
- [ ] 必填/可选明确
- [ ] 枚举值完整

### 权限与安全

- [ ] 包含"权限说明"章节
- [ ] 敏感数据脱敏
- [ ] 无越权风险

### 前端Demo（如有）

- [ ] TypeScript接口完整
- [ ] Mock数据合理
- [ ] 代码可运行

---

## ⚠️ 注意事项

- **正式文档**：prds/是正式版本，需谨慎修改
- **不要直接改**：应在drafts/修改后再覆盖prds/
- **版本管理**：使用版本号追踪变更
- **及时归档**：废弃版本移至archive/

---

## 🔗 参考资源

- **PRD模板**：`templates/prd-template.md`
- **字段清单模板**：`templates/field-list-template.md`
- **前端样式规范**：`templates/frontend-style-guide.md`
- **验证workflow**：`/4-verify-iterate`
- **项目规则**：`.agent/rules/project-rule.md`
