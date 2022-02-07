class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self, course_name):
        print('%s study %s new.'% (self.name, course_name))

    def watch_movie(self):
        if self.age >18:
            print("watch anything")
        else:
            print("watch TV")
def main():
    stu1 = Student('zs', 22)
    print('%s is %s.'% (stu1.name, stu1.age))
    stu1.study('math')
    stu1.watch_movie()

if __name__ == '__main__':
    main()

