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

def courseEdit(season, counter, course, courseMatrix):
    course = np.transpose(course)
    numRow, numCol = course.shape

    for col in range(0, numCol):
        if (isNotIn(course[0, col], courseMatrix[0, :])):
            courseMatrix[0, counter + col] = course[0, col]
            courseMatrix[season, counter + col] = gpa(course[1, col])
            counter += 1
        else:
            if (courseMatrix[season, isNotIn(course[0, col], courseMatrix)] == 0):
                courseMatrix[season, isNotIn(course[0, col], courseMatrix)] = gpa(course[1, col])
            else:
                temp = float(courseMatrix[season, isNotIn(course[0, col], courseMatrix)]) + gpa(course[1, col])
                courseMatrix[season, isNotIn(course[0, col], courseMatrix)] = temp
    return counter, courseMatrix

def courseMatrix():
    courseMatrix = np.zeros([4, 5000])
    list = []
    for counter in range(0, 5000):
        list.append("NA")
    header = np.array([list])
    WC = header
    distrib = header
    courseMatrix = np.vstack((header, courseMatrix))
    courseMatrix = np.vstack((courseMatrix,WC))
    courseMatrix = np.vstack((courseMatrix, distrib))

    fifteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15X_Medians.csv")
    numRow, numCol = fifteenX.shape
    counter = 0
    for col in range(0, numCol):
        courseMatrix[0, col] = fifteenX[0, col]
        courseMatrix[1, col] = fifteenX[1, col]
    fifteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15F_Medians.csv")
    counter, courseMatrix = courseEdit(1, counter, fifteenF, courseMatrix)

    sixteenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16W_Medians.csv")
    counter, courseMatrix = courseEdit(2, counter, sixteenW, courseMatrix)
    sixteenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16S_Medians.csv")
    counter, courseMatrix = courseEdit(3, counter, sixteenS, courseMatrix)
    sixteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16X_Medians.csv")
    counter, courseMatrix = courseEdit(0, counter, sixteenX, courseMatrix)
    sixteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16F_Medians.csv")
    counter, courseMatrix = courseEdit(1, counter, sixteenF, courseMatrix)

    seventeenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17W_Medians.csv")
    counter, courseMatrix = courseEdit(2, counter, seventeenW, courseMatrix)
    seventeenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17S_Medians.csv")
    counter, courseMatrix = courseEdit(3, counter, seventeenS, courseMatrix)
    seventeenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17X_Medians.csv")
    counter, courseMatrix = courseEdit(0, counter, seventeenX, courseMatrix)
    seventeenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17F_Medians.csv")
    counter, courseMatrix = courseEdit(1, counter, seventeenF, courseMatrix)

    numRow, numCol = courseMatrix.shape
    for row in range(1, 5):
        for col in range(0, numCol):
            if float(courseMatrix[row, col]) > 8.0:
                courseMatrix[row, col] = float(courseMatrix[row, col]) / 3
            elif float(courseMatrix[row, col]) > 4.0:
                courseMatrix[row, col] = float(courseMatrix[row, col]) / 2
    return courseMatrix()

def addDistribs(courses, season):
    numRow, numCol = season.shape
    for row in range(0, numRow):
        if (isNotIn(season[row, 0], courses[0, :]) != True):
            courses[5, isNotIn(season[row, 0], courses[0, :])] = season[row, 1]
            courses[6, isNotIn(season[row, 0], courses[0, :])] = season[row, 2]
    return courses

def matrix():
    courses = courseMatrix()
    fall = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Fall.csv")
    courses = addDistribs(courses, fall)

    winter = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Winter.csv")
    courses = addDistribs(courses, winter)
    spring = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Spring.csv")
    courses = addDistribs(courses, spring)
    summer = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Summer.csv")
    courses = addDistribs(courses, summer)

    courses.to_csv("/Users/HC/Desktop/Other/Layuplist_Project/" + "Courses.csv")

matrix()