import Survey
def correct_myfile(old_survey_path):
    file = open(old_survey_path, 'r')
    dict = {}
    for line in file:
        sentence = line.split()
        id = sentence[0]
        age = (int)(sentence[2])
        scores = sentence[4:]
        id_size = 8
        min_age = 0
        max_age = 100

        if (len(id) != id_size) or (age < min_age) or (age > max_age):
            continue
        for x in scores:
            if x < '1' or x > '10':
                continue
        dict[id] = sentence[1:]
    keys = []
    new_dict = {}
    for key in dict:
        keys.append(key)
    keys.sort()

    for element in keys:
        val = dict[element]
        new_dict[element] = val

    for k, v in new_dict.items():
         print(k, end=" ")
         print(*v)

    file.close()

def scan_survey(survey_path):
    file = open(survey_path, 'r')
    survey = Survey.SurveyCreateSurvey()
    for line in file:
        sentence = line.split()
        id = sentence[0]
        eatingHabits = sentence[1]
        age = sentence[2]
        gender = sentence[3]
        scores = sentence[4:]
        Survey.SurveyAddPerson(Survey, id, age, gender, eatingHabits, Scores)
    file.close()
    return survey

def print_info(s , choc_type , gender , min_age , max_age, eating_habits):
    size = 10
    array = Survey.SurveyCreateIntAr(size)
    histogram = Survey.SurveyQuerySurvey(s, choc_type, gender, min_age, max_age, eating_habits)
    for index in range(size):
        val = histogram.count(index)
        Survey.SurveySetIntArIdxVal(array, index, val)
    for index in range(size):
        x = Survey.SurveyGetIntArIdxVal(arrray, index)
        print(x)
    Survey.SurveyQueryDestroy(histogram)
    Survey.SurveyDestoryIntAr(array)


def clear_survey(s):
    Survey.SurveyDestroySurvey(s)

