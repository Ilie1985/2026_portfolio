from pathlib import Path
import yaml

DATA = Path("docs/data/projects.yml")
PROJECTS_MD = Path("docs/projects.md")

def make_card(p: dict) -> str:
    title = p.get("title", "Untitled")
    desc = p.get("description", "")
    tags = p.get("tags", [])
    github = p.get("github")
    tableau = p.get("tableau")

    tag_line = " • ".join(tags) if tags else ""
    links = []
    if github:
        links.append(f"[GitHub]({github})")
    if tableau:
        links.append(f"[Tableau]({tableau})")
    link_line = " | ".join(links) if links else ""

    return f"""
<div class="project-card">

### {title}

{tag_line}

{desc}

{link_line}
</div>
""".strip()

def main():
    projects = yaml.safe_load(DATA.read_text(encoding="utf-8")) or []
    cards = "\n\n".join(make_card(p) for p in projects)
    grid = f'<div class="project-grid">\n\n{cards}\n\n</div>\n'

    md = PROJECTS_MD.read_text(encoding="utf-8")
    start = "<!-- PROJECTS_START -->"
    end = "<!-- PROJECTS_END -->"

    before = md.split(start)[0] + start + "\n"
    after = "\n" + end + md.split(end)[1]

    PROJECTS_MD.write_text(before + grid + after, encoding="utf-8")
    print("Updated docs/projects.md")

if __name__ == "__main__":
    main()