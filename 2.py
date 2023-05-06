def seqa(m):
    termos = []
    for n in range(1,m+1):
        In = 100*((1.0025**n-1)/0.0025-n)
        termos.append(In)
    return termos

def seqb(m):
    In = 0
    for n in range(1,m+1):
        In+=100*((1.0025**n-1)/0.0025-n)
    return In

print("a)", seqa(6))
print("b)", seqb(24))
