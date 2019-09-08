import re
from collections import Counter

words = re.findall(r'\w+',open('dq.py').read().lower())
cnt = Counter()

#to check count of all the words in a text
for word in words:
	cnt[word] += 1

#check count of one given string
print(cnt.items())
