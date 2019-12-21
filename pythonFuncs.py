import Survey
def correct_myfile(old_survey_path):
    file = open(old_survey_path, 'r')
    dict = {}
    for line in file:
        tmp = line
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
        dict[id] = tmp
    keys = []
    new_dict = {}
    for key in dict:
        keys.append(key)
    keys.sort()

    for element in keys:
        val = dict[element]
        new_dict[element] = val

    for k, v in new_dict.items():
         print(v,end="")

    file.close()


def scan_survey(survey_path):
    file = open(survey_path, 'r')
    a = 0
    survey = Survey.SurveyCreateSurvey()
    scores = [0,0,0,0,0]
    for line in file:
        sentence = line.split()
        id = sentence[0]
        eatingHabits = sentence[1]
        if eatingHabits == "Vegan":
            num = 0
        if eatingHabits == "Omnivore":
            num = 1	
        if eatingHabits == "Vegetarian":
            num = 2			
        age = sentence[2]
        gender = sentence[3]
        scores = Survey.SurveyCreateIntAr(5)
        for i in range(5):
            a = int(sentence[i+4])
            Survey.SurveySetIntArIdxVal(scores,i,a)
        Survey.SurveyAddPerson(survey, int(id), int(age), gender, num, scores)
    file.close()
    return survey

def print_info(s , choc_type , gender , min_age , max_age, eating_habits):
    if eating_habits == "Vegan":
        num = 0
    if eating_habits == "Omnivore":
        num = 1
    if eating_habits == "Vegetarian":
        num = 2
    histogram = Survey.SurveyQuerySurvey(s, choc_type, gender, min_age, max_age, num)
    print("[",end="")
    for index in range(10):
        x = Survey.SurveyGetIntArIdxVal(histogram, index)
        if(index == 9):
            print(x,end="")
            break;
        print(x,end="")
        print(', ',end="")
    print(']')
    Survey.SurveyQueryDestroy(histogram)


def clear_survey(s):
    Survey.SurveyDestroySurvey(s)

