from Applicant import Applicant


class ReadWriteFile:
    @staticmethod
    def read_input_file(file_name):
        with open(file_name, 'r') as input_file:
            lines = input_file.readlines()
            beds = int(lines[0].rstrip())  # number of beds
            parking_spots = int(lines[1].rstrip())  # number of parking spots
            chosen_by_LAHSA = int(lines[2].rstrip())  # number of applicants choosen by lahsa
            total_no_of_lines = chosen_by_LAHSA + 3
            lahsa_list = []
            for i in range(3, total_no_of_lines):
                lahsa_list.append((lines[i].rstrip()))
            choosen_by_SPLA = int(lines[total_no_of_lines].rstrip())  # number of applicants choosen by spla
            total_no_of_lines = total_no_of_lines + 1
            spla_list = []
            for i in range(total_no_of_lines, total_no_of_lines + choosen_by_SPLA):
                spla_list.append((lines[i].rstrip()))
            total_no_of_lines = total_no_of_lines + choosen_by_SPLA
            no_of_applicants = int(lines[total_no_of_lines].rstrip())  # number of applicants
            total_no_of_lines = total_no_of_lines + 1
            applicant = []
            for i in range(total_no_of_lines, total_no_of_lines + no_of_applicants):
                a = Applicant(lines[i].rstrip())
                if a.medical_condition == 'N' and a.car == 'Y' and a.license == 'Y':
                    a.valid_spla = True
                if a.pets == 'N' and a.gender == 'F' and a.age > 17:
                    a.valid_lahsa = True
                applicant.append(a)
            return beds, parking_spots, spla_list, lahsa_list, applicant

    @staticmethod
    def create_output_file(applicant_id):
        with open('output.txt', 'w') as output_file:
            output_file.write(applicant_id)