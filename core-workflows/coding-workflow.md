# Coding Workflow

适用场景：毕业设计系统开发、网页应用、脚本、功能迭代、Bug 修复、重构、测试与验收。

## 核心目标

- 先把任务切小，再进入实现。
- 开发和验证尽量同步，减少“写完才发现不对”。
- 卡住时先诊断，不盲改。
- 每完成一个阶段就整理代码和文档。

## 推荐 Skills

- `create-plan`
- `planing-with-file`
- `grill-me`
- `grill-with-docs`
- `tdd`
- `diagnose`
- `webapp-testing`
- `zoom-out`
- `improve-codebase-architecture`
- `karpathy-guidelines`
- `to-prd`
- `to-issues`
- `file-organizer`
- `neat-freak`
- `setup-pre-commit`

## 标准流程

### 1. 先明确这次要做什么

开始前先说清任务，例如：

- “实现登录页和注册接口联调”
- “修复文件上传失败的问题”
- “重构实验数据展示模块”

优先调用：

- `create-plan`
- `planing-with-file`

产出目标：

- 一个可执行的开发计划
- 当前任务的 `plan.md`

### 2. 需求不清楚时先追问

如果你自己也没完全想清楚，先别急着写代码。

优先调用：

- `grill-me`
- `grill-with-docs`

使用建议：

- 没有现成文档，只是想把需求问清楚：`grill-me`
- 项目已经有上下文、术语、设计约束：`grill-with-docs`

产出目标：

- 边界清晰的需求
- 更少返工

### 3. 实现时尽量走小步开发

优先调用：

- `tdd`
- `karpathy-guidelines`

使用建议：

- 先写失败测试
- 再做最小实现
- 最后整理代码

产出目标：

- 更稳的功能实现
- 可验证的改动

### 4. 出现问题时切诊断模式

不要一上来就乱改。

优先调用：

- `diagnose`

适合场景：

- 页面报错但原因不清楚
- 接口返回异常
- 状态同步错乱
- 测试偶发失败
- 性能退化

产出目标：

- 更明确的问题定位
- 更低的误修概率

### 5. 如果是 Web 毕设，做页面和流程验证

优先调用：

- `webapp-testing`
- `playwright`

使用建议：

- `webapp-testing` 更偏“测试流程和总结结果”
- `playwright` 更偏“真实浏览器交互和页面自动化”

产出目标：

- 关键页面通过验证
- 用户流程能跑通

### 6. 写久了以后，主动抬头看结构

如果你感觉项目开始变乱，优先调用：

- `zoom-out`
- `improve-codebase-architecture`

使用建议：

- `zoom-out`：先解释系统整体和当前模块位置
- `improve-codebase-architecture`：再决定怎么拆模块、减耦合

产出目标：

- 更清楚的模块边界
- 更容易继续迭代的结构

### 7. 需要把任务正式化时

如果你想把口头需求变成更正式的工程材料，优先调用：

- `to-prd`
- `to-issues`

产出目标：

- PRD
- 可执行任务拆分

### 8. 阶段结束就收尾

优先调用：

- `file-organizer`
- `neat-freak`
- `setup-pre-commit`

产出目标：

- 目录更整洁
- 文档和代码同步
- 以后不容易把格式、lint、测试搞乱

## 常见任务怎么走

### 场景一：新增一个功能

1. `create-plan`
2. `planing-with-file`
3. `grill-me`
4. `tdd`
5. `webapp-testing`
6. `neat-freak`

### 场景二：修一个难定位的 Bug

1. `create-plan`
2. `diagnose`
3. `tdd`
4. `webapp-testing`
5. `zoom-out`

### 场景三：准备中后期重构

1. `zoom-out`
2. `improve-codebase-architecture`
3. `create-plan`
4. `planing-with-file`
5. `tdd`
6. `neat-freak`

## 你可以直接这样说

- “按代码工作流帮我推进这个功能”
- “先帮我拆开发计划，再开始写”
- “这个 bug 很怪，按诊断流程查”
- “帮我把这个页面功能写完并顺手测一下”
- “这部分代码越来越乱了，帮我从结构上看看”
