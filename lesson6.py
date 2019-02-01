__author__ = "Гонцов Александр Евгеньевич"

import random

pupils = ('Аваньков','Ткачов','Ларионова','Совокурина','Пиров','Сергеев','Каталонина','Бийский','Прозорляев','Захарова','Лунев')
litera = ('А.','Б.','В.','Г.','Д.','Е.','Ж.','З.','И.','К.')
subjects = ('Алгебра', 'Русский язык', 'Обществознание', 'Физика', 'Английский язык', 'Литература', 'Биология', 'География')

class School():
    def __init__(self,name):
        self.name = name
        self.Classes = []
    def addClass(self, Litera):
        self.Classes.append(Litera)
    def showClasses(self):
        print('Школа {} содержит:'.format(self.name))
        for i in self.Classes:
            print('класс {}'.format(i.name))
    def showClass(self, name):
        for i in self.Classes:
            if i.name == name: i.showClass()
    def showPupilInfo(self, name):
        for classes in self.Classes:
            for Pupils in classes.Pupils:
                if Pupils.name == name:
                    for teacher in classes.Teachers:
                        print('Ученик {} класс {} преподаватель {} предмет {}'.format(Pupils.name, classes.name, teacher.name, teacher.subject))
    def showPupilParents(self, name):
        for cl in self.Classes:
            for pupils in cl.Pupils:
                if pupils.name == name: pupils.showParents()
    def genSchool(self, classes, pupils, subjects):
        for i in range(int(classes)):                 
            new_class = Class(str(random.randint(1,11))+random.choice(('A', 'Б', 'В', 'Г')))
            self.addClass(new_class)
            for i in range(int(pupils)):
                new_class.addPupil(Pupil(random.choice(pupils)+' '+random.choice(litera)+random.choice(litera),
                                      random.choice(pupils)+'a '+random.choice(litera)+random.choice(litera),
                                      random.choice(pupils)+' '+random.choice(litera)+random.choice(litera)))
            for i in range(int(subjects)):
                new_class.addTeacher(random.choice(pupils)+random.choice(litera)+random.choice(litera), random.choice(subjects))
            
class Class():
    def __init__(self, name):
        self.name = name
        self.Pupils = []
        self.Teachers = []
    def addPupil(self, pupil):
        self.Pupils.append(pupil)
    def addTeacher(self, name, subject):
        self.Teachers.append(Teacher(name, subject))
    def showClass(self):
        print('Класс {} содержит:'.format(self.name))
        for itm in self.Pupils:
            print('ученик {}'.format(itm.name))

class Pupil():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
    def showParents(self):
        print('Отец - {}, Мать - {}'.format(self.father, self.mother))

class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject