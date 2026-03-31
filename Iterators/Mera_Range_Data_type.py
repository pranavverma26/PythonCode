class mera_Range:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return mera_range_iterator(self)
    
class mera_range_iterator:

    def __init__(self,itearble_obj):
        self.iterable=itearble_obj

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterable.start>=self.iterable.end:
            raise StopIteration
        
        current=self.iterable.start
        self.iterable.start+=1
        return current
    

for i in mera_Range(1,12):
        print(i)

