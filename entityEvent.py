from pygame import time
class EntityEvent:
    def __init__(self,name,function,args,interval,uses=-1):
        self.name = name
        self.function = function
        self.args = args
        self.interval = interval
        self.uses = uses
        current_time = time.get_ticks()
        self.next_use = current_time + interval
    
    def check(self):
        '''Checks if it is time to act, if it is, calls the function. Returns false if out of uses, otherwise returns True'''
        if self.uses != 0:
            current_time = time.get_ticks()
            if current_time > self.next_use:
                self.function(*self.args)
                self.next_use = current_time + self.interval
                self.uses -= 1
            return True
        else:
            return False