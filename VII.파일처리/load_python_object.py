#p247
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'

with open('person_data.bin', 'rb') as file:
    person = pickle.load(file)

print(person)
    # f=open("person_data.bin", "rb")
    # person = pickle.load(f)
    # print(person)
    #
    # f.close()
    #
    # f = open("persons_data.bin", "rb")
    # persons = pickle.load(f)
    #
    # for p in persons:
    #     print(p)
    #
    # f.close()