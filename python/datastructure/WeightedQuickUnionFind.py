import sys


class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n + 1)]
        self.sz = [1]*(n+1)
        self.arr[0] = -1
        self.sz[0] = -1
        self.components = n

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if (self.sz[i] < self.sz[j]):
            i,j = j,i # swapping to avoid two branches/ repetitions.
        self.arr[j] = i
        self.sz[i] += self.sz[j]

    def find(self, p):
        while self.arr[p] != p:
            p = self.arr[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def dump(self):
        print ('Union Find\n----------------')
        print ('Mapping Array :')
        print ([i for i in range(len(self.sz))])
        print (self.arr)
        print ('Sizing Array :')
        print (self.sz)



def main():
    n = int(input("No of vertices --> "))
    print(n)
    uf = UnionFind(n)
    while True:
        s = input().split()
        s = [int(x) for x in s]
        if len(s) > 0:
            if s[0] == 0:
                break # if control is 0 stop execution
            if s[0] == 1:#execute union operation
                uf.union(s[1],s[2])
                continue
            if s[0]==2:#execute connected operation
                print("Connected." if uf.connected(s[1],s[2]) else "Not connected.")
        else:
            break
    uf.dump()
    pass


main()
