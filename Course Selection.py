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

def courses():
    fifteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15X_Medians.csv")
    fifteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15F_Medians.csv")

    sixteenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16W_Medians.csv")
    sixteenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16S_Medians.csv")
    sixteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16X_Medians.csv")
    sixteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16F_Medians.csv")

    seventeenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17W_Medians.csv")
    seventeenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17S_Medians.csv")
    seventeenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17X_Medians.csv")
    seventeenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17F_Medians.csv")

def courseMatrix(course):

    fifteenX = np.transpose(fifteenX)
    fifteenF = np.transpose(fifteenF)

    sixteenW = np.transpose(sixteenW)
    sixteenS = np.transpose(sixteenS)
    sixteenX = np.transpose(sixteenX)
    sixteenF = np.transpose(sixteenF)

    seventeenW = np.transpose(seventeenW)
    seventeenS = np.transpose(seventeenS)
    seventeenX = np.transpose(seventeenX)
    seventeenF = np.transpose(seventeenF)

    numCol = sixteenS.shape[1]
    length = fifteenX.shape[1]
    length1 = fifteenF.shape[1]

    length2 = sixteenW.shape[1]
    length3 = sixteenX.shape[1]
    length4 = sixteenF.shape[1]

    length5 = seventeenW.shape[1]
    length6 = seventeenS.shape[1]
    length7 = seventeenX.shape[1]
    length8 = seventeenF.shape[1]

    for col in range(0, numCol):
        if (col < length):
            fifteenX[1, col] = gpa(fifteenX[1, col])
        if (col < length1):
            fifteenF[1, col] = gpa(fifteenF[1, col])

        if (col < length2):
            sixteenW[1,col] = gpa(sixteenW[1,col])
        if (col < numCol):
            sixteenS[1,col] = gpa(sixteenS[1,col])
        if (col < length3):
            sixteenX[1,col] = gpa(sixteenX[1,col])
        if (col < length4):
            sixteenF[1,col] = gpa(sixteenF[1,col])

        if (col < length5):
            seventeenW[1,col] = gpa(seventeenW[1,col])
        if (col < length6):
            seventeenS[1,col] = gpa(seventeenS[1,col])
        if (col < length7):
            seventeenX[1,col] = gpa(seventeenX[1,col])
        if (col < length8):
            seventeenF[1,col] = gpa(seventeenF[1,col])

    courseMatrix = np.zeros([4, 5000])
    list = []
    for counter in range(0, 5000):
        list.append("NA")
    header = np.array([list])
    courseMatrix = np.vstack((header, courseMatrix))

    counter = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0
    counter6 = 0
    counter7 = 0
    counter8 = 0

    for col in range(0, length):
        courseMatrix[0, col] = fifteenX[0, col]
        courseMatrix[1, col] = fifteenX[1, col]
    for col in range(0, length1):
        if (isNotIn(fifteenF[0, col], courseMatrix) == True):
            courseMatrix[0, counter + length] = fifteenF[0, col]
            courseMatrix[2, counter + length] = fifteenF[1, col]
            counter += 1
        else:
            courseMatrix[2, isNotIn(fifteenF[0, col], courseMatrix)] = fifteenF[1, col]
    index = length + counter

    for col in range(0, length2):
        if (isNotIn(sixteenW[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter1] = sixteenW[0, col]
            courseMatrix[3, index + counter1] = sixteenW[1, col]
            counter1 += 1
        else:
            courseMatrix[3, isNotIn(sixteenW[0, col], courseMatrix)] = sixteenW[1, col]
    index += counter1
    for col in range(0, numCol):
        if (isNotIn(sixteenS[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter2] = sixteenS[0, col]
            courseMatrix[4, index + counter2] = sixteenS[1, col]
            counter2 += 1
        else:

            courseMatrix[4, isNotIn(sixteenS[0, col], courseMatrix)] = sixteenS[1, col]
    index += counter2
    for col in range(0, length3):
        if (isNotIn(sixteenX[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter3] = sixteenX[0, col]
            courseMatrix[1, index + counter3] = sixteenX[1, col]
            counter3 += 1
        else:
            temp = float(courseMatrix[1, isNotIn(sixteenX[0, col], courseMatrix)]) + sixteenX[1, col]
            courseMatrix[1, isNotIn(sixteenX[0, col], courseMatrix)] = temp
    index += counter3
    for col in range(0, length4):
        if (isNotIn(sixteenF[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter4] = sixteenF[0, col]
            courseMatrix[2, index + counter4] = sixteenF[1, col]
            counter4 += 1
        else:
            temp = float(courseMatrix[2, isNotIn(sixteenF[0, col], courseMatrix)]) + sixteenF[1, col]
            courseMatrix[2, isNotIn(sixteenF[0, col], courseMatrix)] = temp
    index += counter4

    for col in range(0, length5):
        if (isNotIn(seventeenW[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter5] = seventeenW[0, col]
            courseMatrix[3, index + counter5] = seventeenW[1, col]
            counter5 += 1
        else:
            temp = (float(courseMatrix[3, isNotIn(seventeenW[0, col], courseMatrix)]) + seventeenW[1, col]) / 2
            courseMatrix[3, isNotIn(seventeenW[0, col], courseMatrix)] = temp
    index += counter5
    for col in range(0, length6):
        if (isNotIn(seventeenS[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter6] = seventeenS[0, col]
            courseMatrix[4, index + counter6] = seventeenS[1, col]
            counter6 += 1
        else:
            temp = (float(courseMatrix[4, isNotIn(seventeenS[0, col], courseMatrix)]) + seventeenS[1, col]) / 2
            courseMatrix[4, isNotIn(seventeenS[0, col], courseMatrix)] = temp
    index += counter6
    for col in range(0, length7):
        if (isNotIn(seventeenX[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter7] = seventeenW[0, col]
            courseMatrix[1, index + counter7] = seventeenW[1, col]
            counter7 += 1
        else:
            courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)] = float(courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)]) + seventeenX[1, col]
            temp = float(courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)]) + seventeenX[1, col]
            if (float(courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)]) > 8.0):
                temp /= 3
                courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)] = temp
            else:
                temp /= 2
                courseMatrix[1, isNotIn(seventeenX[0, col], courseMatrix)] = temp
    index += counter7
    for col in range(0, length8):
        if (isNotIn(seventeenF[0, col], courseMatrix) == True):
            courseMatrix[0, index + counter8] = seventeenF[0, col]
            courseMatrix[2, index + counter8] = seventeenF[1, col]
            counter8 += 1
        else:
            courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)] = float(courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)]) + seventeenF[1, col]
            temp = float(courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)]) + seventeenF[1, col]
            if (float(courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)]) > 8.0):
                temp /= 3
                courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)] = temp
            else:
                temp /= 2
                courseMatrix[2, isNotIn(seventeenF[0, col], courseMatrix)] = temp
    index += counter8

    courseMatrix = np.transpose(courseMatrix)
    courseMatrix = pd.DataFrame(data = courseMatrix)
    print courseMatrix
    #courseMatrix.to_csv("/Users/HC/Desktop/Other/Layuplist_Project/CourseMatrix")

courses()