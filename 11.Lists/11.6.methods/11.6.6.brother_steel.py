import re

list(map(lambda x: print(re.sub(r'\s+#.*', '', x)), [input() for _ in range(int(input()[1:]))]))
