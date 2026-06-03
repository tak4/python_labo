#!/usr/bin/env python3
import argparse
import os
import re
from typing import List

def collect_files(paths: List[str], recursive: bool) -> List[str]:
    files = []
    for p in paths:
        if os.path.isfile(p):
            files.append(p)
        elif os.path.isdir(p):
            if recursive:
                for root, _, filenames in os.walk(p):
                    for fn in filenames:
                        files.append(os.path.join(root, fn))
            else:
                for fn in os.listdir(p):
                    fp = os.path.join(p, fn)
                    if os.path.isfile(fp):
                        files.append(fp)
    return files

def load_keywords(args) -> List[str]:
    kws = []
    if args.keywords:
        for k in args.keywords:
            kws.extend(x for x in (item.strip() for item in k.split(",")) if x)
    if args.keyword_file:
        with open(args.keyword_file, encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s:
                    kws.append(s)
    return list(dict.fromkeys(kws))  # dedupe, preserve order

def make_regex(keywords: List[str], whole: bool, ignore_case: bool):
    if not keywords:
        return None
    parts = [re.escape(k) for k in keywords]
    pattern = "|".join(parts)
    if whole:
        pattern = r"\b(?:" + pattern + r")\b"
    flags = re.MULTILINE
    if ignore_case:
        flags |= re.IGNORECASE
    return re.compile(pattern, flags)

def search_files(files: List[str], regex, show_lineno=True):
    for fp in files:
        try:
            with open(fp, encoding="utf-8", errors="replace") as f:
                for i, line in enumerate(f, start=1):
                    if regex.search(line):
                        if show_lineno:
                            print(f"{fp}:{i}:{line.rstrip()}")
                        else:
                            print(f"{fp}:{line.rstrip()}")
        except (OSError,) as e:
            print(f"# error opening {fp}: {e}")

def main():
    p = argparse.ArgumentParser(description="Simple grep-like search for multiple keywords.")
    p.add_argument("paths", nargs="+", help="Files or directories to search")
    p.add_argument("-k", "--keywords", action="append", help="Comma-separated keywords (can repeat)")
    p.add_argument("-K", "--keyword-file", help="File with one keyword per line")
    p.add_argument("-r", "--recursive", action="store_true", help="Recurse into directories")
    p.add_argument("-i", "--ignore-case", action="store_true", help="Case-insensitive search")
    p.add_argument("-w", "--whole-word", action="store_true", help="Match whole words only")
    p.add_argument("--no-lineno", dest="lineno", action="store_false", help="Do not show line numbers")
    args = p.parse_args()

    keywords = load_keywords(args)
    if not keywords:
        p.error("No keywords provided (use -k or -K).")

    files = collect_files(args.paths, args.recursive)
    if not files:
        p.error("No files found to search.")

    regex = make_regex(keywords, args.whole_word, args.ignore_case)
    search_files(files, regex, show_lineno=args.lineno)

if __name__ == "__main__":
    main()