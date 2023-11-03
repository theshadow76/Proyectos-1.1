class EcuationsGenerator:
    import random as r
    v1=r.randint(1,4)
    s1=r.randint(1,20)
    s2=r.randint(1,20)
    s3=r.randint(1,20)
    s4=r.randint(1,20)
    s5=r.randint(1,20)
    s1=str(s1)
    s2=str(s2)
    S3=str(s3)
    s4=str(s4)
    s5=str(s5)
    l1=[s1,s2,s3,s4,s5]
    if(v1==1):
        s6=r.choice(l1)
        s7=r.choice(l1)
        v2=s6+' + '+s7
        v3=int(s6)+int(s7) 
        