import pandas as pd
import numpy as np

def readCSV(filename):
    table = pd.read_csv(filename)
    table = table.as_matrix()
    return table

def timeTable():
    timeTableFall = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Fall.csv")
    matrix(timeTableFall, "Fall.csv")

    timeTableWinter = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Winter.csv")
    matrix(timeTableWinter, "Winter.csv")

    timeTableSpring = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Spring.csv")
    matrix(timeTableSpring, "Spring.csv")

    timeTableSummer = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/Summer.csv")
    matrix(timeTableSummer, "Summer.csv")

def matrix(timeTable, str):
    numRow, numCol = timeTable.shape
    necessaryTable = np.empty([numRow, 3])

    for row in range(0, numRow):
        if (timeTable[row, 3] - int(timeTable[row, 3] == 0)):
            if (timeTable[row, 3] >= 10):
                string = "0" + str(timeTable[row, 3])
                timeTable[row, 3] = string
            else:
                string = "00" + str(timeTable[row, 3])
                timeTable[row, 3] = string
        else:
            if (timeTable[row, 3] * 10 - int(timeTable[row, 3] * 10) == 0):
                string = str(timeTable[row, 3]) + "0"
                timeTable[row, 3] = string
            else:
                timeTable[row, 3] = str(timeTable[row, 3])
        necessaryTable[row, 0] = timeTable[row, 2] + "-" + timeTable[row, 3]
        necessaryTable[row, 1] =  timeTable[row, 13]
        necessaryTable[row, 2] = timeTable[row, 14]

    necessaryTable = pd.DataFrame(data = necessaryTable)
    necessaryTable.to_csv("/Users/HC/Desktop/Other/Layuplist_Project/" + str)

def courses():
    fifteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15X_Medians.csv")
    courseEdit(fifteenX, "15X_Medians")
    fifteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/15F_Medians.csv")
    courseEdit(fifteenF, "15F_Medians")

    sixteenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16W_Medians.csv")
    courseEdit(sixteenW, "16W_Medians")
    sixteenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16S_Medians.csv")
    courseEdit(sixteenS, "16S_Medians")
    sixteenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16X_Medians.csv")
    courseEdit(sixteenX, "16X_Medians")
    sixteenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/16F_Medians.csv")
    courseEdit(sixteenF, "16F_Medians")

    seventeenW = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17W_Medians.csv")
    courseEdit(seventeenW, "17W_Medians")
    seventeenS = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17S_Medians.csv")
    courseEdit(seventeenS, "17S_Medians")
    seventeenX = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17X_Medians.csv")
    courseEdit(seventeenX, "17X_Medians")
    seventeenF = readCSV("/Users/HC/Desktop/Other/Layuplist_Project/17F_Medians.csv")
    courseEdit(seventeenF, "17F_Medians")

def courseEdit(medians, str):
    numRow, numCol =  medians.shape
    for row in range(0, numRow):
          index = medians[row, 0].rfind('-')
          courseName = medians[row, 0]
          medians[row, 0] = courseName[0: index]
    medians = pd.DataFrame(data = medians)
    medians.to_csv("/Users/HC/Desktop/Other/Layuplist_Project/" + str)

courses()