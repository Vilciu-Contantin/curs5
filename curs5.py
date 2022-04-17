""""
Inscrierea studentilor la un curs si urmarirea progresului
"""


class Student:  # Firma de instalatii
    """
    Creeaza obiecte de tip Student:
        name
        age
        lesson
    """

    def __init__(self, name, age, lesson=1):
        """Inscrierea la curs"""
        self.name = name
        self.age = age
        self.lesson = lesson

    def get_lesson(self):
        """Returneaza lectia la care a ajuns studentul"""
        return self.lesson

    def finish_lesson(self, no_lessons=1):
        """
        Inregistreaza progresul la curs, in raport cu ultima inregistrare
        Parameters :
        no_lessons - nr de lectii parcurse de la ultima inregistrare
        """
        self.lesson += no_lessons

    def info(self):
        print(
            f'Studentul {self.name}, age: {self.age}, lectia : {self.lesson}')


class Course:  # Lucrari
    """
    Creeaza obiecte de tip curs
    Atribure 
        name -numele cursului
        max_studenti - capacitatea maxima a stidentilor
        total_lectii - nr de lectii din curs (static)
    """
    total_lectii = 15
    description = 'Cursul programare in Python'

    def __init__(self, name, max_studenti):
        self.name = name
        self.max_studenti = max_studenti
        self.studenti = []

    def enrol_studenti(self, student):
        """
        Adauga / inscrie un student la curs 
        Parametri:
         student - tip Student , cu datele cursantului
     """  # firme inscrise pentru lucrari in desfasurare
        if len(self.studenti) < self.max_studenti:
            self.studenti.append(student)
            print(f"Inscriere {student.name} realizate cu succes")
        else:
            print("Capacitatea maxima a cursului a fost atinsa")

    def get_max_capacity(self):
        """
        Returneaza numarul maxim de stidenti inscrisi
        """  # firma maxime pentru instalat fotovoltaice
        return self.max_studenti

    def get_filled_capacity(self):
        """Returneaza numarul de studenti inscrisi la curs
        """  # firme  de instalatii fotovoltaicie disponibile
        return len(self.studenti)

    @staticmethod
    def averange(args):
        """Calculeaza media valorilor din lista transmisa ca parametru"""
        total = 0
        for value in args:
            total += value
        return total/len(args)

    def get_avarange_lesson(self):
        """
        Returneaza media lectiilor parcurse de studenti
        """   # returmeaza lucrarile in desfasurare a firmelor
        # total = 0
        # for student in self.studenti:
        #     total += student.lesson
        # return total / len(self.studenti)
        return Course.averange([student.lesson for student in self.studenti])


def main():
    student1 = Student('Jhon Doe', 20,  1)
    student2 = Student('Alex Sima', 30, 2)
    student1.info()
    student1.finish_lesson()
    student1.info()
    student2.info()
    student2.finish_lesson()
    student2.info()
    curs = Course("Python developer", 3)
    curs .enrol_studenti(student1)
    curs .enrol_studenti(student2)
    curs.enrol_studenti(Student('Another Student', 29))
    print(f'Lectia medie este: {curs.get_avarange_lesson()}')
    print(f'Capacitatea maxima: {curs.get_max_capacity()}')
    student2.finish_lesson(4)
    print(f'Lectia medie este: {curs.get_avarange_lesson()}')
    student1.info()
    student2.info()
    student3 = Student('Max Max', 20)
    curs.enrol_studenti(student3)


if __name__ == "__main__":
    main()
