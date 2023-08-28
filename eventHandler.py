import pygame
class EventHandler:
    def __init__(self,screen,tilemap,entities):
        self.screen = screen
        self.tilemap = tilemap
        self.entities = entities
        self.keydown_events = {}
        self.mouse_events = {}
        self.keyup_events = {}
        self.mouse_scroll_events = {}
        self.misc = {}
    
    def add_event(self,type,catalyst,function,parameters = []):
        '''Add a new event for the system to watch for.
        Paramters:
        type: either 'mouse' or 'keydown' or 'keyup'.
        catalyst: the button or key to respond to. If given 0, the function will happen on any occurence of that type. Only one misc. function can be added per type.
        function: the function to be performed.
        parameters: the parameters to be passed to the function
        '''
        if catalyst == 0:
            self.misc[type] = [function,parameters]
        else:
            if type == 'keydown':
                self.keydown_events[catalyst] = [function, parameters]
            elif type == 'keyup':
                self.keyup_events[catalyst] = [function, parameters]
            elif type == 'mouse':
                self.mouse_events[catalyst] = [function, parameters]
            elif type == 'mouse_scroll':
                self.mouse_scroll_events[catalyst] = [function,parameters]
            else:
                print("Error")
        
    
    def handle_events(self):
        '''Checks for any events that are being watched for.'''
        # Structure for events in keybaord or mouse_event dictionaries:
        # key: the event.key or event.button which causes the event
        # value: an array with two parts: the function to occur at that event, and the arguments for that function (empty array if no arguments)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key in self.keydown_events:
                    self.keydown_events[event.key][0](*self.keydown_events[event.key][1])
                elif 'keydown' in self.misc:
                    self.misc['keydown'][0](*self.misc['keydown'][1])
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in self.mouse_events:
                    self.mouse_events[event.button][0](*self.mouse_events[event.button][1])
                elif 'mouse' in self.misc:
                    self.misc['mouse'][0](*self.misc['mouse'][1])
            elif event.type == pygame.MOUSEWHEEL:
                if event.y in self.mouse_scroll_events:
                    self.mouse_scroll_events[event.y][0](*self.mouse_scroll_events[event.y][1])
            elif event.type == pygame.KEYUP:
                if event.key in self.keyup_events:
                    self.keyup_events[event.key][0](*self.keydown_events[event.key][1])
                elif 'keyup' in self.misc:
                    self.misc['keyup'][0](*self.misc['keyup'][1])
            

            