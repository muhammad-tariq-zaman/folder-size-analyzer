# folder-size-analyzer

Recursive folder size report with the top-N largest files. Standard library only.

## How to run

```bash
python3 main.py --path ./some-folder --top 10
```

## Example output (sample from test fixture data)

```text
Folder: ./some-folder
Total: 110 B (110 bytes)
Files: 2
Largest files:
     100 B  ./some-folder/sub/big.txt
```

No network access.
