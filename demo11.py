# re库的贪婪匹配和最小匹配

import re

match = re.search(r'PY.*N', 'PYANBNCNDN')
# 实际上我们可以匹配到四个字符串 ：PYAN PYANBN PYANBNCN PYANBNCNDN

# 但是re库默认贪婪匹配，也就是匹配最长的
print(match.group(0))

# 如果我们想要最小的，也就是最小匹配,可以这样做
match2 = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match2.group())
