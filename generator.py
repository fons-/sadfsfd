from functools import reduce
import random

namen = [l.replace('\n','').replace('\r','') for l in open("namen.txt").readlines() if len(l)>2]
random.shuffle(namen)

aanvallers = [namen[i-1] for i in range(len(namen))]

lines = ["\t"+a+" & \\ding{254} & "+n+" \\\\\\\\ \r\n" for a,n in zip(aanvallers,namen)]

mid = reduce(lambda a,b:a+b,lines)
pre = open("pre.tex").read()
post = open("post.tex").read()

open("lijst.tex",'w').write(pre + mid + post)
