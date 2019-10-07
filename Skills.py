# This is a class for modelling learning and skills


class Skills:
    pass

    def __init__(self, new_hire, where_department):
        self.new_hire = new_hire
        self.where_department = where_department

    def development(self, learning, finish_learning, take_an_exam):
        print("method from class Skills")
        if learning:
            print("method from class Skills")
            print("learning in progress")
            if finish_learning:
                print("I have finished my studies and ready to take an exam.")
                if take_an_exam:
                    print("passed my exam")
                else:
                    print(False)
                    print("Exam failed, refresh your study")
                    self.development()
            else:
                print(False)
                print("I have not finish exam")
        else:
            return False
