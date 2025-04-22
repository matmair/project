from __future__ import annotations

from pathlib import Path

import frontmatter
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

KEYS = ["ADR", "author", "status", "created", "decided", "date", "type"]


def get_meta_table(path: str | Path) -> nodes.table:
    raw_metadata = frontmatter.load(path).metadata
    metadata = {k: v for k, v in raw_metadata.items() if k in KEYS}

    # Form table from front matter metadata
    table = nodes.table(cols=2)
    group = nodes.tgroup()
    head = nodes.thead()
    body = nodes.tbody()

    table += group
    group += nodes.colspec(colwidth=6)
    group += nodes.colspec(colwidth=6)
    group += head
    group += body

    for k, v in metadata.items():
        row = nodes.row()
        row += nodes.entry("", nodes.paragraph("", nodes.Text(k)))
        row += nodes.entry("", nodes.paragraph("", nodes.Text(v)))
        body += row
    return table


class AdrBlockRole(SphinxRole):
    """A role to render the ADR block."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        return [get_meta_table(self.env.doc2path(self.env.docname))], []


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("adr", AdrBlockRole())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
