class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []
        self.count = 0

    def greet(self, other_person):
        self.count += 1
        print 'Hello %s, I am %s' % (other_person.name, self.name)

    def add_friend(self, friend):
        self.friend.append(friend)

    def num_friends(self):
        return len(self.friend)

    def getGreetingCount(self):
        return self.count

sonny = Person("sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)

sonny.add_friend(jordan)
jordan.add_friend(sonny)

print "sonny has %d friends" % sonny.num_friends()
print "jordan has %d friends" % jordan.num_friends()

print "sonny has said hello %d times" % sonny.getGreetingCount()
print "jordan has said hello %d times" % jordan.getGreetingCount()
