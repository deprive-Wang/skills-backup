---
name: codex-template-skill
description: Skill 模板骨架。复制此目录并替换 frontmatter 和正文来创建新 skill。不要直接使用。
---

# Skill 模板

此文件是创建新 skill 的起始模板。使用步骤：

1. 复制 `codex-template-skill/` 目录，重命名为你的 skill 名（kebab-case）
2. 替换 frontmatter 中的 `name` 和 `description`
3. 用实际指令替换下方正文

## Frontmatter 规范

```yaml
---
name: your-skill-name          # kebab-case，与目录名一致
description: 一句话说明用途和触发条件。Claude 根据此字段决定是否调用此 skill。
---
```

`description` 是最关键的字段 -- 写清「什么时候该用这个 skill」，不要只写「做什么」。
