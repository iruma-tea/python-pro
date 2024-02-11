# 段落を文とトークンに分割。単純なコードの列
import re  # https://docs.python.org/ja/3/howto/regex.html 参照

product_review = '''This is a fine milk, but the product line appears
 to be limited in available colors. I could only find white.'''

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
matches = sentence_pattern.findall(product_review)
sentences = [match[0] for match in matches]

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]
    print(words)
