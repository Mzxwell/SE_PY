a=['a','s','w','f','yn','u','k','yh']
b=[12,56,2,6,56,12,3,5,]
print(sorted(a,key=lambda x:(b[a.index(x)],x),reverse=True))
print(sorted(a,key=lambda x:(b[a.index(x)]),reverse=True))
c =lambda x:(x+1,x+2)
print(c(1))