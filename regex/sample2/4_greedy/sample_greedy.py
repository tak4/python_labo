import re

# Greedy 欲深い：可能な限り長い文字列に一致させようとする動作
s = '<html><head><title>Title</title></head></html>'

print(re.match('<.*>', s))  # Greedy
print(re.match('<.*?>', s)) # Non-Greedy
