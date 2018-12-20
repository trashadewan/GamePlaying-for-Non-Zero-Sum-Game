# class for applicants
class Applicant:
    def __init__(self, info):
        self.id = info[0:5]
        self.gender = info[5:6]
        self.age = int(info[6:9])
        self.pets = info[9:10]
        self.medical_condition = info[10:11]
        self.car = info[11:12]
        self.license = info[12:13]
        self.monday = int(info[13:14])
        self.tuesday = int(info[14:15])
        self.wednesday = int(info[15:16])
        self.thursday = int(info[16:17])
        self.friday = int(info[17:18])
        self.saturday = int(info[18:19])
        self.sunday = int(info[19:20])
        self.value = 0
        self.no_of_days_requested = 0
        for i in range(13,20):
            if info[i:i+1] == "1":
                self.value = self.value + (1 << (19-i))
                self.no_of_days_requested = self.no_of_days_requested + 1
        self.valid_spla = False
        self.valid_lahsa = False
        self.selected_by_spla = False
        self.selected_by_lahsa = False