---
name: git-auto
description: 自动提交当前 git 项目变更：检测变更 → 更新 README（如有生成器） → git add → commit → pull --rebase → push
---

# Git Auto Commit

手动调用，对当前 git 项目执行完整自动提交流程。

## 工作流程

1. 检测当前目录是否在 git 仓库内；若不是，提示跳过
2. 若项目根目录有 `generate_readme.py`，执行它刷新 README
3. `git add -A`
4. `git commit -m "auto: N changed file(s) [项目名]"`
5. 若有 remote：`git pull --rebase` + `git push`

## 使用方法

在任意项目目录下执行：

```bash
"D:\Git\bin\bash.exe" "C:\Users\14000\.cc-switch\auto-commit.sh"
```
