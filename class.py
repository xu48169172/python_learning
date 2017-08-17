class Person:

    def setname(self,name):
        self.name = name

    def getname(self):
        print self.name

    def greet(self):
        print "Hello I'm %s" % self.name


person=Person()
person.setname("Jack")
person.getname()
person.greet()
