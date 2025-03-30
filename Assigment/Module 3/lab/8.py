class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5))        
print(m.add(5, 10))    
print(m.add(5, 10, 15)) 
