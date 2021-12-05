import numpy as np

def convert_marital_status(data):
    data = data[data["Marital_Status"] != "YOLO"]
    data = data[data["Marital_Status"] != "Absurd"]
    marital_status = data.copy(deep=True)["Marital_Status"]
    marital_status[marital_status == 'Alone'] = 'Single'
    data[data["Marital_Status"] == 'Alone']
    data["Marital_Status"] = marital_status

    married = marital_status
    married[married == "Married"] = 1
    married[married != 1] = 0
    data["Married"] = married

    single = marital_status
    single[single == "Single"] = 1
    single[single != 1] = 0
    data["Single"] = single

    together = marital_status
    together[together == "Together"] = 1
    together[together != 1] = 0
    data["Together"] = together

    divorced = marital_status
    divorced[divorced == "Divorced"] = 1
    divorced[divorced != 1] = 0
    data["Divorced"] = divorced

    widow = marital_status
    widow[widow == "Widow"] = 1
    widow[widow != 1] = 0
    data["Widow"] = widow

    return data.drop(columns=['Marital_Status'], inplace=False)

def convert_education(data):
    education = data.copy(deep=True)["Education"]
    education[education == '2n Cycle'] = 'Master'
    
    levels = ['Basic', 'Graduation', 'Master', 'PhD']

    for i in range(len(levels)):
        education[education == levels[i]] = i
    data["Education"] = education
    return data

def create_spending(data):
    spending_columns = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]
    total_spending = np.repeat(0.0, len(data))

    for col in spending_columns:
        total_spending += data[col]
        
    data["Spending"] = total_spending
    return data.drop(columns=spending_columns, inplace=False)