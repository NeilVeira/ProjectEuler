f = open("22.txt").read()
names = []
for line in f.split(","):
    names.append(line.strip('"'))
names.sort() 
#print names[:1000]

ans = 0
for i in xrange(len(names)):
    val = 0
    for c in names[i]:
        val += ord(c)-ord('A')+1
    #print names[i],val
    ans += val*(i+1)
    
print ans