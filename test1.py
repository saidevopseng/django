# feature available since 3.8v as the part of PEP 570
def f1(a,b,/):
    print(a,b)
f1(10,20)
# f1(a=10,b=20)
