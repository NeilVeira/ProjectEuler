from math import factorial as f
import Queue

facts = []
for i in range(10):
    facts.append(f(i))

def get_next(n):
    ret = 0
    while n > 0:
        ret += facts[n%10]
        n /= 10
    return ret 

chain = [0]*2200000
rev_chain = [[] for _ in range(2200000)]
chain_len = [-1]*2200000
chain_len[169] = chain_len[363601] = chain_len[1454] = 3
chain_len[871] = chain_len[45361] = 2
chain_len[872] = chain_len[45362] = 2

m = 0
for i in range(1,1000000):
    x = i
    while chain[x] == 0:
        xx = get_next(x)
        chain[x] = xx 
        rev_chain[xx].append(x)
        m = max(m,x)
        x = xx     

queue = Queue.Queue()
for x in [169,363601,1451,871,872,45361,45362]:
    queue.put(x)
    
ans = 0
while not queue.empty():
    top = queue.get()
    if chain_len[top] == 60:
        ans += 1
    for x in rev_chain[top]:
        if chain_len[x] == -1:
            chain_len[x] = chain_len[top]+1
            queue.put(x)
            
print ans 
