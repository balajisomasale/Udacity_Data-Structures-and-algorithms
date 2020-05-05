from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Intiallizing the variables of my class LRU_cache
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        # Retrieving the item from given key. If it doesnt present,return -1
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache
        if key in self.cache:
            self.cache.pop(key)
        
        self.cache[key] = value
        
        # If the cache is at capacity remove the oldest item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
        
cache = LRU_Cache(5)

cache.set(1, 1);
cache.set(2, 2);
cache.set(3, 3);
cache.set(4, 4);


print(cache.get(1))       # It returns 1
print(cache.get(2))       # It returns 2
print(cache.get(9))      # It returns -1 because 9 does not present in the CACHE

cache.set(5, 5) 
cache.set(6, 6)

print(cache.get(3))      # returns -1 because the cache reached it's capacity 
                         # and 3 was the least recently used entry


cache.set(4, 4)        # Setting the same number for the CHECK
print(cache.get(4))    # returns 4 as same number is still there



#Resubmitting the Work => Checking the Edge cases.
print(cache.get(0))     #This returns -1 as it is Empty cases
cache.set(0,0)        #Iam setting 0 also here just to check
print(cache.get(0))   #0 is returned which means It is satisfying our requirement

cache.set(-2,-2)
print(cache.get(-2))    #Here it is returning -2 as we set the value to -2 .. which is satisfied


