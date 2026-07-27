#!/usr/bin/env python3
"""Auto-generate README.md for the skills-backup repo by scanning all SKILL.md frontmatters."""
import re
import sys
from pathlib import Path

SKILLS_DIR = Path.home() / ".cc-switch" / "skills"

# Category definitions: (category_name, emoji_icon, skill_name_list)
CATEGORY_MAP = {
    "开发工作流": ["feature-dev"],
    "代码质量": [
        "verification-before-completion", "karpathy-guidelines", "code-simplifier",
    ],
    "调试与测试": ["systematic-debugging", "tdd", "webapp-testing"],
    "文档生成": [
        "skills/common/markitdown", "ppt-master", "doc", "pdf", "Visiomaster",
    ],
    "学术与论文": [
        "academic-paper-polisher", "nature-reader", "paper-review",
    ],
    "会议与沟通": [
        "codex-meeting-insights", "codex-meeting-notes",
    ],
    "知识管理": ["notion-research-documentation", "storage-analyzer"],
    "项目初始化": [
        "codex-project-onboarding",
    ],
    "辅助工具": ["caveman"],
}

# Manual notes for specific skills (skill_name -> note)
SKILL_NOTES: dict[str, str] = {
    "tdd": "保留版本；强调行为测试和垂直切片",
    "skills/common/markitdown": "通用转换工具",
    "codex-meeting-insights": "保留版本",
    "codex-meeting-notes": "保留版本",
    "codex-project-onboarding": "Codex 专用",
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
        "dir": skill_dir.relative_to(SKILLS_DIR).as_posix(),
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
    skill_dirs = [
        d for d in sorted(SKILLS_DIR.iterdir())
        if d.is_dir() and not d.name.startswith(".")
    ]
    common_dir = SKILLS_DIR / "skills" / "common"
    if common_dir.exists():
        skill_dirs.extend(
            d for d in sorted(common_dir.iterdir())
            if d.is_dir() and not d.name.startswith(".")
        )

    for d in skill_dirs:
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
        "`~/.cc-switch/skills/` 是唯一维护的 Git 仓库；`~/.claude/skills/` "
        "和 `~/.codex/skills/` 都是指向它的 Junction（同一份文件，非独立 clone）。"
        "自定义 Skill 修改后，在 CCS 目录 commit + push；Codex 系统层 `.system/` "
        "由官方维护，不纳入本仓库追踪。"
    )
    lines.append("")
    lines.append("**Remote:** `https://github.com/deprive-Wang/skills-backup.git`")
    lines.append("")
    lines.append("## 快速恢复")
    lines.append("")
    lines.append("```bash")
    lines.append("# CCS 统一目录")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.cc-switch/skills")
    lines.append("")
    lines.append("# 然后将 Claude / Codex skills 目录链接到 CCS 统一目录")
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

    # Compact set note
    lines.append("---")
    lines.append("")
    lines.append("## 精简说明")
    lines.append("")
    lines.append("同一类能力只保留一个主要入口，官方系统 skill 位于 `.system/`，不列入自定义索引：")
    lines.append("")
    lines.append("| 功能 | 可选 Skill | 说明 |")
    lines.append("|------|-----------|------|")
    lines.append("| 调试与 TDD | `systematic-debugging` / `tdd` | 分别负责根因调试与测试驱动开发 |")
    lines.append("| 科研展示 | `ppt-master` / `Visiomaster` | 分别负责 PPT 与可编辑 Visio 图 |")
    lines.append("| 文档处理 | `doc` / `pdf` | 分别负责 DOCX 与 PDF |")
    lines.append("")

    # Naming conventions
    lines.append("---")
    lines.append("")
    lines.append("## 命名约定")
    lines.append("")
    lines.append("- `codex-` 前缀: Codex 特定版本")
    lines.append("- `nature-` 前缀: Nature 学术写作系列")
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
    lines.append("cd ~/.cc-switch/skills")
    lines.append("git add <明确的 Skill 路径> README.md generate_readme.py")
    lines.append('git commit -m "更新: <skill名> -- <简述>"')
    lines.append("git push")
    lines.append("```")
    lines.append("")
    lines.append("### 新电脑恢复")
    lines.append("")
    lines.append("```bash")
    lines.append("git clone https://github.com/deprive-Wang/skills-backup.git ~/.cc-switch/skills")
    lines.append("# 再把 ~/.claude/skills 和 ~/.codex/skills 链接到 ~/.cc-switch/skills")
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
