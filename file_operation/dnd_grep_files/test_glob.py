from pathlib import Path

p = Path('.')

for path in p.glob('**/*.log'):
    print(path)

print()
for path in p.rglob('*.log'):
    print(path)

print()
files = [str(x) for x in p.rglob('*.log')]
for f in files:
    print(f)

print()
files = p.rglob('*.log')
for f in files:
    print(f)
