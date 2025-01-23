"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    round_list = []
    while student_scores:
        round_list.append(round(student_scores.pop(0)))
    return round_list


def count_failed_students(student_scores):
    count = 0
    while student_scores:
        i = student_scores.pop(0)
        if i <= 40:
            count += 1
    return count

    


def above_threshold(student_scores, threshold):
    threshold_list = []
    while student_scores:
        i = student_scores.pop(0)
        if i >= threshold:
            threshold_list.append(i)
    return threshold_list


def letter_grades(highest):
    """Where the highest score is 88, and failing is <= 40.
       "F" <= 40
 41 <= "D" <= 52
 53 <= "C" <= 64
 65 <= "B" <= 76
 77 <= "A" <= 88
 """

    grade_list = []
    threshold = 41
    calc = round((highest - 40 ) / 4)

    for _ in range (4):
        grade_list.append(threshold)
        threshold = (threshold) + calc

    return grade_list



def student_ranking(student_scores, student_names):
    ranking_list = []
    for i in range(len(student_scores)):
        ranking_list.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return ranking_list

def perfect_score(student_info):
    perfect_list = []
    for i in range(len(student_info)):
        if 100 in student_info[i]:
            perfect_list.extend(student_info[i])
            break
    return perfect_list




# to print out the return value.
round_score = round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3])
failed = count_failed_students([90,40,55,70,30,25,80,95,38,40])
the_best = above_threshold([90,40,55,70,30,68,70,75,83,96], 75)
calc_grade = letter_grades(88)
match_names = student_ranking([100, 99, 90, 84, 66, 53, 47], ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred'])
perfect = perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]])

print( 'Round The scores:', round_score, 'Non-passing Students:', failed, 'The best scores:', the_best, 'Calculating Letter Grades:', calc_grade, 'Matching Names to the scores:', match_names, 'A perfect score:', perfect)