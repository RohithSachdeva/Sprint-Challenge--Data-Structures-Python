class RingBuffer:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        self.first_element = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item) #could have array be self.items to match the provided parameter item...
        else:
            self.data[self.first_element] = item
        self.first_element += 1

        if self.first_element == self.capacity:
            self.first_element = 0

    def get(self):
        return self.data

"""
Append adds the given element to the buffer... 

get method returns all the elements in order... should return none values as well 

Init should include an empty array 
    capacity = self.capacity
    data < capacity ... you can append the item into the array .. 
    some examples include a 0 index which is what gets overwritten... so need to make sure things are getting properly appended to the end 
    makes sense... have a reference point to the first element in the structure 


seem to have + 1   % modular  in the append methods in examples ... not sure I fully understand that.  

also seen a += 1 to move the index which makes sense 

def enqueue(self, item):
        Insert an item at the back of the CircularBuffer
        Runtime: O(1) Space: O(1)
        if self.is_full():
            raise OverflowError(
                "CircularBuffer is full, unable to enqueue item")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size


        github example... 
"""