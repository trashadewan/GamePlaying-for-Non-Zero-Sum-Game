# class for available utility
class Utility:
    def __init__(self, utility):
        self.utility = utility
        self.utility_value = 127
        self.value = 0
        self.monday = utility
        self.tuesday = utility
        self.wednesday = utility
        self.thursday = utility
        self.friday = utility
        self.saturday = utility
        self.sunday = utility

    def min(self):
        return min(self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday)

    def to_string(self):
        return str(self.monday) + str(self.tuesday) + str(self.wednesday) + str(self.thursday) + str(self.friday) + str(self.saturday) + str(self.sunday)

    def modify(self, a):
        if a.monday == 1:
            self.monday = self.monday - 1
            self.value = self.value + 1
            if self.monday == 0:
                self.utility_value = self.utility_value - (1 << 6)

        if a.tuesday == 1:
            self.tuesday = self.tuesday - 1
            self.value = self.value + 1
            if self.tuesday == 0:
                self.utility_value = self.utility_value - (1 << 5)

        if a.wednesday == 1:
            self.wednesday = self.wednesday - 1
            self.value = self.value + 1
            if self.wednesday == 0:
                self.utility_value = self.utility_value - (1 << 4)

        if a.thursday == 1:
            self.thursday = self.thursday - 1
            self.value = self.value + 1
            if self.thursday == 0:
                self.utility_value = self.utility_value - (1 << 3)

        if a.friday == 1:
            self.friday = self.friday - 1
            self.value = self.value + 1
            if self.friday == 0:
                self.utility_value = self.utility_value - (1 << 2)

        if a.saturday == 1:
            self.saturday = self.saturday - 1
            self.value = self.value + 1
            if self.saturday == 0:
                self.utility_value = self.utility_value - (1 << 1)

        if a.sunday == 1:
            self.sunday = self.sunday - 1
            self.value = self.value + 1
            if self.sunday == 0:
                self.utility_value = self.utility_value - (1 << 0)

    def modify_back(self, a):
        if a.monday == 1:
            self.monday = self.monday + 1
            self.value = self.value - 1
            if self.monday == 1:
                self.utility_value = self.utility_value + (1 << 6)

        if a.tuesday == 1:
            self.tuesday = self.tuesday + 1
            self.value = self.value - 1
            if self.tuesday == 1:
                self.utility_value = self.utility_value + (1 << 5)

        if a.wednesday == 1:
            self.wednesday = self.wednesday + 1
            self.value = self.value - 1
            if self.wednesday == 1:
                self.utility_value = self.utility_value + (1 << 4)

        if a.thursday == 1:
            self.thursday = self.thursday + 1
            self.value = self.value - 1
            if self.thursday == 1:
                self.utility_value = self.utility_value + (1 << 3)

        if a.friday == 1:
            self.friday = self.friday + 1
            self.value = self.value - 1
            if self.friday == 1:
                self.utility_value = self.utility_value + (1 << 2)

        if a.saturday == 1:
            self.saturday = self.saturday + 1
            self.value = self.value - 1
            if self.saturday == 1:
                self.utility_value = self.utility_value + (1 << 1)

        if a.sunday == 1:
            self.sunday = self.sunday + 1
            self.value = self.value - 1
            if self.sunday == 1:
                self.utility_value = self.utility_value + (1 << 0)

    def is_allowed_to_add(self,applicant):
        return (self.utility_value & applicant.value) == applicant.value