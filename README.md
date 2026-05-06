# Codex Skills Backup

这个仓库用于备份、恢复和同步你的 Codex 工作流资产。

## 目标

- 备份自定义 skill
- 备份高频使用的第三方 skill 副本
- 保存论文工作流、代码工作流、常用 skill 组合
- 在更换电脑或本地崩溃后快速恢复

## 目录结构

- `core-workflows/`
  保存你的工作流文档
- `skills/custom/`
  保存你自己创建或改写过的 skill
- `skills/core/`
  保存工作流直接依赖的高频 skill 副本
- `skills/common/`
  保存常用但不是核心依赖的 skill 副本
- `catalog/`
  保存清单、来源和恢复命令
- `scripts/`
  保存同步与恢复脚本

## 日常使用

### 1. 修改本地工作流或 skills 后同步

在 PowerShell 中进入仓库目录后运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-to-github.ps1
```

如果没有变化，脚本会输出 `nothing to sync`。

如果有变化，脚本会：

- 更新备份内容
- 自动执行 `git add`
- 自动提交
- 如果已经配置远端，则自动 `git push`

### 2. 在新电脑恢复

先把这个仓库 clone 到本地，然后运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\restore-from-backup.ps1
```

脚本会：

- 恢复 `skills/custom`
- 恢复 `skills/core`
- 恢复 `skills/common`
- 输出其他仍需单独安装的 skill 和命令

## 首次绑定 GitHub 私有仓库

当前机器没有安装 `gh` CLI，所以第一次创建远端仓库需要你手动完成。

### GitHub 上的操作

1. 在 GitHub 新建一个私有仓库，建议名为 `codex-skills-backup`
2. 不要初始化 `README`、`.gitignore` 或 License
3. 创建完成后复制仓库地址

### 本地操作

在本仓库目录运行：

```powershell
git remote add origin <你的仓库地址>
git branch -M main
git push -u origin main
```

HTTPS 示例：

```powershell
git remote add origin https://github.com/<your-name>/codex-skills-backup.git
git branch -M main
git push -u origin main
```

## 维护规则

- 工作流文档变更后及时同步
- 自定义 skill 变更后及时同步
- 新增高频 skill 时，按用途放入 `skills/core` 或 `skills/common`
- 非高频第三方 skill 仅登记在 `catalog/skills-manifest.md`
