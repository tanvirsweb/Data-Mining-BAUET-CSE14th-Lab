import re
from IPython.display import Markdown, display
from pathlib import Path

def generate_toc():
    """
    Auto-generates a clickable Markdown Table of Contents
    based on the current notebook's markdown headings.
    Works inside VS Code Jupyter environment.
    """
    # Get current notebook path dynamically (works when saved)
    try:
        from IPython import get_ipython
        ipynb_name = get_ipython().getoutput("echo $PWD")[0]
        notebook_files = list(Path(ipynb_name).glob("*.ipynb"))
        if not notebook_files:
            raise FileNotFoundError("No .ipynb file found in directory.")
        nb_path = notebook_files[0]
    except Exception as e:
        display(Markdown(f"**Error locating notebook:** {e}"))
        return

    # Read notebook content
    text = nb_path.read_text(encoding="utf-8")

    # Find Markdown headings
    headers = re.findall(r'#+\s.*', text)

    # Generate clickable Markdown links
    toc_lines = []
    for h in headers:
        level = h.count('#')
        title = h.replace('#', '').strip()
        # Generate anchor links like GitHub-style markdown
        link = re.sub(r'[^a-z0-9\s-]', '', title.lower())
        link = link.replace(' ', '-')
        toc_lines.append(f"{'  '*(level-1)}- [{title}](#{link})")

    # Display the formatted Table of Contents
    display(Markdown("### 📖 Table of Contents\n" + "\n".join(toc_lines)))



generate_toc()