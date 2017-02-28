class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []

    def greet(self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)


    def add_friend(self, friend):
        self.friend.append(friend)

sonny = Person("sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("jordan", "jordan@aol.com", "495-586-3456")

sonny.add_friend(jordan)
jordan.add_friend(sonny)

print len(jordan.friend)
print len(sonny.friend)
