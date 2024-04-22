class Event:
    events = {}

    def __init__(self, arr):
        self.events = {key: lambda: None for key in arr}

    def __setitem__(self, EVENT, value):
        if EVENT not in list(self.events.keys()):
            raise ValueError(f"Invalid Event Key: {EVENT} not found")
        self.events[EVENT] = value 

    def __getitem__(self, EVENT):
        if EVENT not in list(self.events.keys()):
            raise ValueError(f"Invalid Event Key: {EVENT} not found")
        return self.events[EVENT]