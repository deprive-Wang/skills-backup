#!/usr/bin/env python3
"""Auto-generate README.md for the skills-backup repo by scanning all SKILL.md frontmatters."""
import re
import sys
from pathlib import Path

SKILLS_DIR = Path.home() / ".cc-switch" / "skills"

# Category definitions: (category_name, emoji_icon, skill_name_list)
CATEGORY_MAP = {
    "开发工作流": [
        "feature-dev", "subagent-driven-development", "executing-plans",
        "dispatching-parallel-agents", "writing-plans", "workflow-code",
    ],
    "代码质量": [
        "pr-review-toolkit", "requesting-code-review", "receiving-code-review",
        "verification-before-completion", "karpathy-guidelines",
        "improve-codebase-architecture", "code-simplifier",
    ],
    "调试与测试": [
        "systematic-debugging", "diagnose", "tdd", "tdd-mattpocock",
        "test-driven-development", "webapp-testing", "playwright",
    ],
    "Git 工具": [
        "git-guardrails", "finishing-a-development-branch", "using-git-worktrees",
        "setup-pre-commit",
    ],
    "文档生成": [
        "minimax-docx", "minimax-pdf", "minimax-xlsx", "markitdown",
        "ppt-master", "pptx-generator", "doc", "pdf", "paperjsx",
        "codex-paperjsx", "Visiomaster",
    ],
    "写作与内容": [
        "content-research-writer", "codex-content-research-writer",
        "edit-article", "codex-changelog", "codex-email-polish",
    ],
    "学术与论文": [
        "workflow-thesis", "hv-analysis", "academic-paper-polisher",
        "nature-paper2ppt", "nature-polishing", "nature-reader",
        "nature-response", "nature-writing", "brainstorming",
        "grill-me", "grill-with-docs",
    ],
    "PaperSpine 论文工作流": [
        "paper-spine", "paper-spine-intake", "paper-spine-ui",
        "paper-spine-research", "paper-spine-citation", "paper-spine-build",
        "paper-spine-rewrite", "paper-spine-latex", "paper-spine-translate",
        "paper-spine-humanize", "paper-spine-audit", "paper-spine-update",
    ],
    "会议与沟通": [
        "meeting-insights-analyzer", "codex-meeting-insights",
        "meeting-notes-and-actions", "codex-meeting-notes",
    ],
    "知识管理": [
        "neat-freak", "obsidian-vault", "notion-research-documentation",
        "notion-spec-to-implementation", "file-organizer", "codex-file-organizer",
    ],
    "项目管理": [
        "to-issues", "to-prd", "triage", "qa", "create-plan",
        "codex-create-plan", "planning-with-file",
    ],
    "技能系统": [
        "using-superpowers", "workflow-reference", "workflow-combos",
        "writing-skills", "write-a-skill", "write-a-skill-mattpocock",
        "codex-skill-creator", "codex-template-skill",
    ],
    "项目初始化": [
        "init", "codex-project-onboarding",
    ],
    "辅助工具": [
        "caveman", "spreadsheet-formula-helper",
    ],
}

# Manual notes for specific skills (skill_name -> note)
SKILL_NOTES: dict[str, str] = {
    "tdd": "与 `test-driven-development` 功能相同",
    "test-driven-development": "与 `tdd` 功能相同",
    "tdd-mattpocock": "含测试反模式指南",
    "content-research-writer": "与 `codex-content-research-writer` 功能相同",
    "codex-content-research-writer": "Codex 版本",
    "file-organizer": "与 `codex-file-organizer` 功能相同",
    "codex-file-organizer": "Codex 版本",
    "create-plan": "与 `codex-create-plan` 功能相同",
    "codex-create-plan": "Codex 版本",
    "meeting-insights-analyzer": "与 `codex-meeting-insights` 功能相同",
    "codex-meeting-insights": "Codex 版本",
    "meeting-notes-and-actions": "与 `codex-meeting-notes` 功能相同",
    "codex-meeting-notes": "Codex 版本",
    "paperjsx": "与 `codex-paperjsx` 功能相同",
    "codex-paperjsx": "Codex 版本",
    "write-a-skill": "与 `write-a-skill-mattpocock` 功能相似",
    "write-a-skill-mattpocock": "Matt Pocock 版",
    "codex-template-skill": "创建新 skill 的起始模板",
    "init": "Codex 专用",
    "codex-project-onboarding": "Codex 专用",
    "planning-with-file": "原名 `planing-with-file`，已修正拼写",
    "caveman": "超压缩通信模式 (省 75% Token)",
}

# Skill name overrides: directory name -> display name
DISPLAY_NAME_OVERRIDES: dict[str, str] = {}


def parse_skill(skill_dir: Path) -> dict | None:
    """Parse a SKILL.md file and return its metadata, or None if not parseable."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None

    content = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None

    frontmatter = m.group(1)
    name = None
    description = None
    in_block_scalar = False
    block_scalar_lines: list[str] = []
    block_indent: int = 0

    for line in frontmatter.split("\n"):
        if in_block_scalar:
            if line and (line.startswith(" " * (block_indent + 1)) or line.startswith("\t")):
                block_scalar_lines.append(line[block_indent:].lstrip())
                continue
            else:
                description = " ".join(block_scalar_lines).strip()
                in_block_scalar = False
                block_scalar_lines = []

        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        elif line.startswith("description:"):
            rest = line.split(":", 1)[1].strip()
            if rest in (">", "|", ">-", "|-", ">+", "|+"):
                in_block_scalar = True
                # Find indentation of the current value
                raw = line.split(":", 1)[1]
                block_indent = len(raw) - len(raw.lstrip())
                block_scalar_lines = []
            elif rest:
                description = rest

    # Handle block scalar that ends at EOF
    if in_block_scalar and block_scalar_lines:
        description = " ".join(block_scalar_lines).strip()

    if not name or not description:
        return None

    # Strip surrounding quotes from description
    description = description.strip()
    if len(description) >= 2 and description[0] == description[-1] and description[0] in ('"', "'"):
        description = description[1:-1]

    return {
        "dir": skill_dir.name,
        "name": name,
        "description": description,
    }


def get_category(skill_name: str) -> str | None:
    """Return the category for a skill, or None if not categorized."""
    for cat, names in CATEGORY_MAP.items():
        if skill_name in names:
            return cat
    return None


def build_readme() -> str:
    """Generate the complete README.md content."""
    skills = []
    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        parsed = parse_skill(d)
        if parsed:
            skills.append(parsed)

    # Index by directory name
    by_dir: dict[str, dict] = {s["dir"]: s for s in skills}

    # Group by category
    categorized: dict[str, list[dict]] = {cat: [] for cat in CATEGORY_MAP}
    uncategorized: list[dict] = []

    for s in skills:
        cat = get_category(s["dir"])
        if cat:
            categorized[cat].append(s)
        else:
            uncategorized.append(s)

    lines: list[str] = []

    # Header
    lines.append("# Skills Backup — Codex / Claude 双平台通用")
    lines.append("")
    lines.append(
        "本仓库备份全部自定义 Skill 资产，兼容 **OpenAI Codex** 与 "
        "**Anthropic Claude Code** 双平台。每个目录即一个独立 Skill，可在任一平台加载使用。"
    )
    lines.append("")
    lines.append(
        "> Claude Code 的内置命令（`update-config`、`keybindings-help`、"
        "`fewer-permission-prompts`、`loop`、`claude-api`、`run`、`verify`、"
        "`review`、`security-review`、`code-review` 等）以及 Anthropic 官方插件 "
        "skill（`anthropic-skills:*`）不在此仓库中，无需备份。"
    )
    lines.append("")
    lines.append("## 双目录同步")
    lines.append("")
    lines.append(
        "`~/.claude/skills/` 和 `~/.codex/skills/` 指向同一个 Git 仓库"
        "（同一份文件，非独立 clone）。任一处修改后 commit + push 即可。"
    )
    lines.append("")
    lines.append("**Remote:** `https://github.com/deprive-Wang/skills-backup.git`")
    lines.append("")
    lines.append("## 快速恢复")
    lines.append("")
    lines.append("```bash")
    lines.append("# Claude Code")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.claude/skills")
    lines.append("")
    lines.append("# OpenAI Codex (同一个仓库)")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.codex/skills")
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Skill 分类索引")
    lines.append("")

    # Emoji mapping for categories
    category_emojis: dict[str, str] = {
        "开发工作流": "",
        "代码质量": "",
        "调试与测试": "",
        "Git 工具": "",
        "文档生成": "",
        "写作与内容": "",
        "学术与论文": "",
        "PaperSpine 论文工作流": "",
        "会议与沟通": "",
        "知识管理": "",
        "项目管理": "",
        "技能系统": "",
        "项目初始化": "",
        "辅助工具": "",
    }

    for cat_name in CATEGORY_MAP:
        cat_skills = categorized.get(cat_name, [])
        if not cat_skills:
            continue
        emoji = category_emojis.get(cat_name, "")
        header = f"### {emoji} {cat_name}" if emoji else f"### {cat_name}"
        lines.append(header)
        lines.append("")

        # Determine if this category has notes
        has_notes = any(s["dir"] in SKILL_NOTES for s in cat_skills)
        if has_notes:
            lines.append("| Skill | 描述 | 备注 |")
            lines.append("|-------|------|------|")
            for s in cat_skills:
                note = SKILL_NOTES.get(s["dir"], "")
                desc = s["description"].replace("|", "\\|")
                lines.append(f"| `{s['dir']}` | {desc} | {note} |")
        else:
            lines.append("| Skill | 描述 |")
            lines.append("|-------|------|")
            for s in cat_skills:
                desc = s["description"].replace("|", "\\|")
                lines.append(f"| `{s['dir']}` | {desc} |")
        lines.append("")

    # Uncategorized skills
    if uncategorized:
        lines.append("### 未分类")
        lines.append("")
        lines.append("| Skill | 描述 |")
        lines.append("|-------|------|")
        for s in uncategorized:
            desc = s["description"].replace("|", "\\|")
            lines.append(f"| `{s['dir']}` | {desc} |")
        lines.append("")

    # Duplicate / variant note
    lines.append("---")
    lines.append("")
    lines.append("## 重复/变体 Skill 说明")
    lines.append("")
    lines.append("以下 skill 存在功能重复或变体关系，可根据偏好选择使用：")
    lines.append("")
    lines.append("| 功能 | 可选 Skill | 说明 |")
    lines.append("|------|-----------|------|")
    lines.append("| TDD | `tdd` / `test-driven-development` | 功能完全相同 |")
    lines.append("| TDD (进阶) | `tdd-mattpocock` | 含测试反模式指南 |")
    lines.append("| 内容写作 | `content-research-writer` / `codex-content-research-writer` | Codex 版本针对 Codex 环境适配 |")
    lines.append("| 文件整理 | `file-organizer` / `codex-file-organizer` | 同上 |")
    lines.append("| 创建计划 | `create-plan` / `codex-create-plan` | 同上 |")
    lines.append("| 会议洞察 | `meeting-insights-analyzer` / `codex-meeting-insights` | 同上 |")
    lines.append("| 会议纪要 | `meeting-notes-and-actions` / `codex-meeting-notes` | 同上 |")
    lines.append("| 文档生成 | `paperjsx` / `codex-paperjsx` | 同上 |")
    lines.append("| Skill 创建 | `write-a-skill` / `write-a-skill-mattpocock` / `codex-skill-creator` | 三个变体 |")
    lines.append("")

    # Naming conventions
    lines.append("---")
    lines.append("")
    lines.append("## 命名约定")
    lines.append("")
    lines.append("- `codex-` 前缀: Codex 特定版本")
    lines.append("- `nature-` 前缀: Nature 学术写作系列")
    lines.append("- `paper-spine-` 前缀: PaperSpine 论文工作流系列")
    lines.append("- 无前缀: 双平台通用或 Claude 原生")
    lines.append("- 大写开头 (`Visiomaster`): 特殊命名约定")
    lines.append("")

    # Sync guide
    lines.append("---")
    lines.append("")
    lines.append("## 日常同步")
    lines.append("")
    lines.append("### 修改 Skill 后推送")
    lines.append("")
    lines.append("```bash")
    lines.append("cd ~/.codex/skills   # 或 ~/.claude/skills")
    lines.append("git add -A")
    lines.append('git commit -m "更新: <skill名> -- <简述>"')
    lines.append("git push")
    lines.append("```")
    lines.append("")
    lines.append("### 新电脑恢复")
    lines.append("")
    lines.append("```bash")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.claude/skills")
    lines.append("# 或")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.codex/skills")
    lines.append("```")
    lines.append("")

    # Auto-gen footer
    lines.append("---")
    lines.append("")
    lines.append(f"> README.md 由 `generate_readme.py` 自动生成，共收录 {len(skills)} 个 Skill。")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    readme_path = SKILLS_DIR / "README.md"
    new_content = build_readme()

    old_content = ""
    if readme_path.exists():
        old_content = readme_path.read_text(encoding="utf-8")

    if old_content.strip() == new_content.strip():
        print("[generate_readme] README.md 无需更新")
        return 0

    readme_path.write_text(new_content, encoding="utf-8")
    print("[generate_readme] README.md 已更新")
    return 0


if __name__ == "__main__":
    sys.exit(main())
