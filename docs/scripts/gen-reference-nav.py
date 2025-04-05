"""
A mkdocs-gen-files[1] script to generate summary documents of the full Python API suitable for use
with mkdocs-literate-nav[2].

Any ".gitignore" files are respected along with a special-purpose ".docsignore" file which can be
used to additionally mark files as ones which shouldn't be included in the automatically generated
documentation index.

[1] https://oprypin.github.io/mkdocs-gen-files/
[2] https://oprypin.github.io/mkdocs-literate-nav/
"""

from pathlib import Path

import gitignorefile
import mkdocs_gen_files

nav = mkdocs_gen_files.Nav()
mod_symbol = '<code class="doc-symbol doc-symbol-nav doc-symbol-module"></code>'

repo_root = Path(__file__).parent.parent.parent
should_ignore = gitignorefile.Cache(
    ignore_names=[".docsignore", ".gitignore", ".git/info/exclude"]
)

for path in sorted(repo_root.rglob("*.py")):
    if should_ignore(str(path)):
        continue
    module_path = path.relative_to(repo_root).with_suffix("")
    doc_path = path.relative_to(repo_root).with_suffix(".md")
    full_doc_path = Path("reference", doc_path)

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = full_doc_path.with_name("index.md")
    elif parts[-1].startswith("_"):
        continue

    nav[tuple(parts)] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"---\ntitle: {ident}\n---\n\n::: {ident}")

    mkdocs_gen_files.set_edit_path(full_doc_path, ".." / path.relative_to(repo_root))

with mkdocs_gen_files.open("reference/SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
