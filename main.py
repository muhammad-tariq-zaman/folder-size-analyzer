"""Folder size analyzer: recursive size report and top-N largest files."""
import argparse
import os
import sys


def human(n):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024
    return f"{n:.1f} PB"


def analyze(root, top_n=10):
    files = []
    total = 0
    for dirpath, _dirs, names in os.walk(root):
        for name in names:
            path = os.path.join(dirpath, name)
            try:
                size = os.path.getsize(path)
            except OSError:
                continue
            files.append((size, path))
            total += size
    files.sort(reverse=True)
    return {"root": root, "total_bytes": total, "file_count": len(files),
            "largest": files[:top_n]}


def report(result):
    lines = [f"Folder: {result['root']}",
             f"Total: {human(result['total_bytes'])} ({result['total_bytes']} bytes)",
             f"Files: {result['file_count']}", "Largest files:"]
    for size, path in result["largest"]:
        lines.append(f"  {human(size):>10}  {path}")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description="Report folder size and largest files.")
    p.add_argument("--path", required=True)
    p.add_argument("--top", type=int, default=10)
    args = p.parse_args(argv)
    print(report(analyze(args.path, args.top)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
