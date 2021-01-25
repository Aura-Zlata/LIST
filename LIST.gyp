
"""

with open ('dinlistainitiala.txt','r') as f:
    c=str(f.read())
    e=c.split()

with open ('dinlistainitiala.txt','w') as f:
    f.write(str(sorted(e)))

