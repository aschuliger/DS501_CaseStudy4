import numpy as np

def clean(data):
    data = remove_monotone_columns(data)
    data = normalize_spending_vals(data)
    return data
    

def remove_monotone_columns(data):
    columns_to_keep = []
    for col in data.columns:
        num_of_uniques = len(data[col].unique())
        if num_of_uniques > 1:
            columns_to_keep.append(col)
    return data[columns_to_keep]


def normalize_spending_vals(data):
    # Normalize the spending values to get a better idea as to what a customer buys more of
    spending_vals = ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"]
    return normalize_columns(data, spending_vals)
    
    
def normalize_columns(data, columns):
    for col in columns:
        _min = np.min(data[col])
        _max = np.max(data[col])
        data[col] = (data[col] - _min) / (_max - _min)
    return data