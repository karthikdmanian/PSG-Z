u=(4,5)
v=(6,7)
def cosine(u,v):
    dotp=u[0]*v[0]+u[1]*v[1]
    umag=(u[0]**2+u[1]**2)**0.5
    vmag=(v[0]**2+v[1]**2)**0.5
    return dotp/(umag*vmag)
print("The cosine of",u,"and",v,"is",cosine(u,v))

