import pandas as pd
import numpy as np

def gpa(str):
    if (str == "B-"):
        return (2 + 2.0/3)
    elif (str == "B/B-"):
        return (2 + 5.0/6)
    elif (str == "B"):
        return 3.0
    elif (str == "B+/B"):
        return (3 + 1.0/6)
    elif (str == "B+"):
        return (3 + 1.0/3)
    elif (str == "A-/B+"):
        return 3.5
    elif (str == "A-"):
        return (3 + 2.0/3)
    elif (str == "A/A-"):
        return (3 + 5.0/6)
    else:
        return 4.0

def isNotIn(course, termMatrix):
    numCol = termMatrix.shape[1]
    for col in range(0, numCol):
        if (course == termMatrix[0, col]):
            return col
    return True

def readCSV(filename):
    table = pd.read_csv(filename)
    table = table.as_matrix()
    return table

def courseEdit(term):
    #return term -> [subject + number, WC, Dist]


def courses():
    courseMatrix = np.zeros([8, 5000])
    fall = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Fall.csv")
    courseEdit(fall)

    winter = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Winter.csv")
    courseEdit(winter)

    spring = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Spring.csv")
    courseEdit(spring)

    summer = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Summer.csv")
    courseEdit(summer)

    courseMatrix = pd.DataFrame(data = courseMatrix)
    courseMatrix.to_csv("/Users/HC/Desktop/Other/Layuplist_Project/Course_Matrix.csv")