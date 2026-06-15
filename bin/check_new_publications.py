#!/usr/bin/env python
"""Detect Google Scholar publications that are newly tracked since the last
run and don't yet have a matching entry in the curated bibliography.

Compares the `papers` map in an old and new snapshot of `_data/citations.yml`.
Any publication ID that is new (wasn't present in the old snapshot) and whose
title doesn't fuzzy-match a title already in `_bibliography/papers.bib` is
written to the output file for review.
"""

import argparse
import re
import sys
import yaml


def normalize_title(title: str) -> str:
    title = re.sub(r"[{}]", "", title)
    title = re.sub(r"\\[a-zA-Z]+", "", title)  # strip LaTeX escapes, e.g. {\alpha}
    title = re.sub(r"[^a-z0-9 ]", "", title.lower())
    return re.sub(r"\s+", " ", title).strip()


def load_bib_titles(path: str) -> set:
    with open(path) as f:
        text = f.read()
    titles = set()
    for m in re.finditer(r"^\s*title\s*=\s*\{(.+?)\}\s*,?\s*$", text, re.M | re.S):
        norm = normalize_title(m.group(1))
        if norm:
            titles.add(norm)
    return titles


def load_papers(path: str) -> dict:
    with open(path) as f:
        data = yaml.safe_load(f) or {}
    return data.get("papers", {}) or {}


def title_in_bib(title: str, bib_titles: set) -> bool:
    norm = normalize_title(title)
    if not norm:
        return False
    for bt in bib_titles:
        if norm[:40] == bt[:40] or norm in bt or bt in norm:
            return True
    return False


def write_issue_body(path: str, candidates: list, scholar_id: str) -> None:
    lines = []
    if scholar_id:
        scholar_url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
        lines.append(
            f"The following publications were newly detected on [Google Scholar]({scholar_url}) "
            "but don't appear to have a matching entry in `_bibliography/papers.bib` yet:"
        )
    else:
        lines.append(
            "The following publications were newly detected on Google Scholar "
            "but don't appear to have a matching entry in `_bibliography/papers.bib` yet:"
        )
    lines.append("")
    for c in candidates:
        lines.append(f"- **{c.get('title')}** ({c.get('year')}, {c.get('citations')} citations)")
    lines.append("")
    lines.append(
        "Add an entry to `_bibliography/papers.bib` if you'd like it to appear on the "
        "[publications page](https://shankara-a.github.io/publications/)."
    )
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--old", required=True, help="Previous _data/citations.yml snapshot")
    parser.add_argument("--new", required=True, help="Updated _data/citations.yml")
    parser.add_argument("--bib", required=True, help="_bibliography/papers.bib")
    parser.add_argument("--output", required=True, help="Where to write candidate publications (YAML)")
    parser.add_argument("--issue-body", help="Where to write a Markdown issue body, if any candidates are found")
    parser.add_argument("--scholar-id", default="", help="Google Scholar user ID, for linking in the issue body")
    args = parser.parse_args()

    old_papers = load_papers(args.old)
    new_papers = load_papers(args.new)
    bib_titles = load_bib_titles(args.bib)

    new_ids = sorted(set(new_papers) - set(old_papers))

    candidates = []
    for pub_id in new_ids:
        pub = new_papers[pub_id]
        if not title_in_bib(pub.get("title", ""), bib_titles):
            candidates.append({"pub_id": pub_id, **pub})

    with open(args.output, "w") as f:
        yaml.dump(candidates, f, sort_keys=False)

    if args.issue_body and candidates:
        write_issue_body(args.issue_body, candidates, args.scholar_id)

    print(f"Found {len(new_ids)} new Scholar publication(s); {len(candidates)} not yet in {args.bib}.")
    for c in candidates:
        print(f"  - [{c.get('year')}] {c.get('title')} ({c.get('citations')} citations)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
