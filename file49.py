class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        return (f"Name: {self.name}\nLocation: {self.location}")

    def publish(self, message):
        return (message)

class BookPublisher(Publisher):
    super().__init__(name, location)
    def __init__(num_authors):
        self.num_authors = num_authors
    
    def __str__(self):
        print(self.num_authors)

class NewspaperPublisher(Publisher):
    super().__init__(name, location)
    def __init__(num_pages):
        self.num_pages = num_pages

