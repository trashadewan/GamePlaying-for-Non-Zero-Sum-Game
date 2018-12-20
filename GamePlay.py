import time
from Utility import Utility
from ReadWriteFile import ReadWriteFile


def best_pick_among_leftover(leftover_applicant, utility, type):
    s = type
    for i in leftover_applicant:
        s += i
    s += utility.to_string()
    if s in cache:
        return cache[s][0], cache[s][1]
    max_s, id = game_play_inner(leftover_applicant, utility, type)
    cache[s] = (max_s, id)
    return max_s, id


def game_play_inner(leftover_applicant, utility, type):
    length = len(leftover_applicant)
    if length == 0 or utility.utility_value == 0:
        return utility.value, ''
    no_space_in_utility = True
    max_s = -1
    app = ''
    for x in range(length):
        i = leftover_applicant[x]
        if utility.is_allowed_to_add(applicants[int(i) - 1]):
            no_space_in_utility = False
            leftover_applicant.remove(i)
            utility.modify(applicants[int(i) - 1])
            s, value = best_pick_among_leftover(leftover_applicant, utility, type)
            utility.modify_back(applicants[int(i) - 1])
            leftover_applicant.insert(x, i)
            if s > max_s:
                max_s = s
                app = i
    if no_space_in_utility:
        max_s = utility.value
    return max_s, app


def game_play_spla(co, sp, la, spla, lahsa):
    no_space_in_utility = True
    max_s, max_l = -1, -1
    app = ''
    for i in co:
        if spla.is_allowed_to_add(applicants[int(i) - 1]):
            no_space_in_utility = False
            new_list = co * 1
            new_list.remove(i)
            spla.modify(applicants[int(i) - 1])
            s, l, value = game_play_lahsa(new_list, sp, la, spla, lahsa)
            spla.modify_back(applicants[int(i) - 1])
            if s == max_s and app != '' and int(i) < int(app):
                max_l = l
                app = i
            if s > max_s:
                max_s = s
                max_l = l
                app = i
    total_requested_spla, a = best_pick_among_leftover(sp, spla, 's')
    if not (total_requested_spla == spla.value and no_space_in_utility):
        if total_requested_spla < max_s:
            return max_s, max_l, app
        elif total_requested_spla == max_s and int(app) < int(a):
            return max_s, max_l, app
        else:
            merged_list = (co + la)
            total_requested_merged, b = best_pick_among_leftover(merged_list, lahsa, 'l')
            return total_requested_spla, total_requested_merged, a
    else:
        merged_list = (co + la)
        total_requested_merged, b = best_pick_among_leftover(merged_list, lahsa, 'l')
        return spla.value, total_requested_merged, ''


def game_play_lahsa(co, sp, la, spla, lahsa):
    app = ''
    no_space_in_utility = True
    max_s, max_l = -1, -1
    for i in co:
        if (int(time.time() * 1000) - t) >= 179500:
            return spla.value, lahsa.value, ''
        if lahsa.is_allowed_to_add(applicants[int(i) - 1]):
            no_space_in_utility = False
            new_list = co * 1
            new_list.remove(i)
            lahsa.modify(applicants[int(i) - 1])
            s, l, value = game_play_spla(new_list, sp, la, spla, lahsa)
            lahsa.modify_back(applicants[int(i) - 1])
            if l == max_l and app != '' and int(i) < int(app):
                max_s = s
                app = i
            if l > max_l:
                max_l = l
                max_s = s
                app = i
    total_requested_lahsa, a = best_pick_among_leftover(la, lahsa, 'l')
    if not (total_requested_lahsa == lahsa.value and no_space_in_utility):
        if total_requested_lahsa < max_l:
            return max_s, max_l, app
        elif total_requested_lahsa == max_s and int(app) < int(a):
            return max_s, max_l, app
        else:
            merged_list = (co + sp)
            total_requested_merged, b = best_pick_among_leftover(merged_list, spla, 's')
            return total_requested_merged, total_requested_lahsa, a
    else:
        merged_list = (co + sp)
        total_requested_merged, b = best_pick_among_leftover(merged_list, spla, 's')
        return total_requested_merged, lahsa.value, ''


def main():
    global applicants, cache
    bed, parking_spot, spla_list, lahsa_list, applicants = ReadWriteFile.read_input_file("../grading_case/input22.txt")
    SPLA = Utility(bed)
    # Modify SPLA utility for already selected applicants by SPLA
    for i in spla_list:
        applicants[int(i) - 1].selected_by_spla = True
        SPLA.modify(applicants[int(i) - 1])
    LAHSA = Utility(parking_spot)
    # Modify LAHSA utility for already selected applicants by LAHSA
    for i in lahsa_list:
        applicants[int(i) - 1].selected_by_lahsa = True
        LAHSA.modify(applicants[int(i) - 1])
    cache = {}
    leftover_applicant = []
    # creating separate lists depending on
    LAHSA_applicant_list = []
    SPLA_applicant_list = []
    common_applicant_list = []
    for a in applicants:
        if a.selected_by_lahsa or a.selected_by_spla:
            continue
        if a.valid_lahsa and a.valid_spla:
            common_applicant_list.append(a.id)
        else:
            if a.valid_spla:
                SPLA_applicant_list.append(a.id)
            elif a.valid_lahsa:
                LAHSA_applicant_list.append(a.id)
    SPLA_best_score, LAHSA_best_score, best_applicant = game_play_spla(common_applicant_list, SPLA_applicant_list,
                                                                       LAHSA_applicant_list, SPLA, LAHSA)
    ReadWriteFile.create_output_file(best_applicant)
    print best_applicant
    print "Final Value %s %s" % (SPLA_best_score, LAHSA_best_score)


if __name__ == "__main__":
    t = time.time()*1000
    main()
    print (time.time()*1000-t)