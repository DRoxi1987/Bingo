from random import choice


class Pouch:
    def __init__(self):
        self.rand_list = []
        self.create_rand_list()

    def create_rand_list(self):
        for i in range(1, 90):
            self.rand_list.append(i)

    def iter(self):

        if self.rand_list:
            ran = choice(self.rand_list)
            if ran in self.rand_list:
                self.rand_list.remove(ran)
                return ran
        else:
            return False

