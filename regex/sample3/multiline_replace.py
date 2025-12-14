import re

# File path
file_path = 'test.txt'

# Read the entire file content
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# The regular expression to find a word, a newline, and then digits
# \s+ matches one or more whitespace characters (including newlines)
pattern = re.compile(r'([A-Z_]+)\s+(\d+)')

# The replacement string, using backreferences to the captured groups
# \1 refers to the first group ([A-Z_]+)
# \2 refers to the second group (\d+)
replacement = r'\1 \2'

# Perform the replacement
new_content = pattern.sub(replacement, content)

# Write the new content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print(f"Successfully replaced text in {file_path}")
