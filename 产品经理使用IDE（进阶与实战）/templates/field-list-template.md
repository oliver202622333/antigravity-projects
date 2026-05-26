# 字段清单模板

> **文档类型**：字段清单  
> **实体名称**：[实体名称]  
> **创建日期**：YYYY-MM-DD  
> **最后更新**：YYYY-MM-DD  
> **作者**：[作者名称]

---

## 业务说明

[简要说明此实体的业务含义、用途和应用场景]

---

## 主表字段

| 字段名      | 类型     | 必填 | 说明                                       |
| ----------- | -------- | ---- | ------------------------------------------ |
| id          | String   | 是   | 唯一标识，系统自动生成                     |
| code        | String   | 是   | 编码，格式：XXX-YYYYMMDD-001，系统自动生成 |
| name        | String   | 是   | 名称，最大长度100字符                      |
| description | String   | 否   | 描述，最大长度500字符                      |
| status      | Enum     | 是   | 状态，默认值：Draft，见枚举值定义          |
| createdAt   | DateTime | 是   | 创建时间，系统自动生成                     |
| createdBy   | String   | 是   | 创建人，系统自动获取当前用户               |
| updatedAt   | DateTime | 是   | 更新时间，系统自动维护                     |
| updatedBy   | String   | 是   | 更新人，系统自动获取当前用户               |

---

## 明细字段（如适用）

| 字段名     | 类型   | 必填   | 说明                 |
| ---------- | ------ | ------ | -------------------- |
| itemId     | String | 是     | 明细ID，系统自动生成 |
| parentId   | String | 是     | 关联主表ID           |
| sequenceNo | Number | 是     | 行号，从1开始        |
| [业务字段] | [类型] | [必填] | [说明]               |

---

## 枚举值定义

### status（状态）

- **Draft**：草稿 - 初始状态，可编辑
- **Active**：生效 - 已生效，不可编辑
- **Closed**：关闭 - 已关闭，不可编辑

### [其他枚举字段]

- **值1**：说明1
- **值2**：说明2

---

## 字段类型说明

本文档使用以下字段类型：

| 类型        | 说明               | 示例                         |
| ----------- | ------------------ | ---------------------------- |
| String      | 字符串             | "张三"                       |
| Number      | 数值（整数或小数） | 100, 99.99                   |
| Boolean     | 布尔值             | true, false                  |
| Date        | 日期               | 2026-01-31                   |
| DateTime    | 日期时间           | 2026-01-31 10:00:00          |
| Enum        | 枚举（固定可选值） | Draft, Active, Closed        |
| Array<Type> | 数组               | [{...}, {...}]               |
| Object      | 对象（嵌套结构）   | {key1: value1, key2: value2} |
| Ref<Entity> | 引用其他实体       | 关联到User实体               |

---

## 嵌套结构说明（如适用）

如果字段包含复杂的嵌套结构，在此详细说明：

### items（明细列表）

类型：`Array<Item>`

**Item结构**：
| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| sku | String | 是 | SKU编码 |
| productName | String | 是 | 商品名称 |
| quantity | Number | 是 | 数量，必须>0 |
| unitPrice | Number | 是 | 单价，单位：元 |
| amount | Number | 是 | 金额，计算公式：quantity \* unitPrice |

---

## 字段约束与规则

### 数据验证规则

- **code**：必须唯一，系统自动生成，格式：[前缀]-YYYYMMDD-[序号]
- **name**：必填，长度1-100字符
- **quantity**：必须>0，最大999999
- **amount**：自动计算，不可手动修改

### 计算字段

- **amount**：计算公式 = quantity \* unitPrice，保留2位小数

### 关联约束

- **parentId**：必须关联到已存在的[父实体]
- **userId**：必须关联到已存在的用户

---

## TypeScript类型定义（供前端使用）

```typescript
// 主实体类型定义
interface [EntityName] {
  id: string;
  code: string;
  name: string;
  description?: string;
  status: EntityStatus;
  createdAt: string;
  createdBy: string;
  updatedAt: string;
  updatedBy: string;
}

// 枚举类型定义
enum EntityStatus {
  Draft = 'Draft',
  Active = 'Active',
  Closed = 'Closed'
}

// 明细类型定义（如适用）
interface [ItemName] {
  itemId: string;
  parentId: string;
  sequenceNo: number;
  // 其他业务字段
}
```

---

## Mock数据示例（供前端使用）

```typescript
const mockData: [EntityName][] = [
  {
    id: "001",
    code: "XXX-20260131-001",
    name: "示例数据1",
    description: "这是一条示例数据",
    status: EntityStatus.Active,
    createdAt: "2026-01-31 10:00:00",
    createdBy: "张三",
    updatedAt: "2026-01-31 10:00:00",
    updatedBy: "张三",
  },
  {
    id: "002",
    code: "XXX-20260131-002",
    name: "示例数据2",
    description: "这是另一条示例数据",
    status: EntityStatus.Draft,
    createdAt: "2026-01-31 11:00:00",
    createdBy: "李四",
    updatedAt: "2026-01-31 11:00:00",
    updatedBy: "李四",
  },
];
```

---

## 备注

[其他需要说明的内容]

---

## 修订记录

| 版本 | 日期       | 修订内容 | 修订人 |
| ---- | ---------- | -------- | ------ |
| V1.0 | YYYY-MM-DD | 初始版本 | [姓名] |
