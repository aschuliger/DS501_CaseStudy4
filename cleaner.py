def clean(data):
    data = remove_monotone_columns(data)
    return data
    

def remove_monotone_columns(data):
    columns_to_keep = []
    for col in data.columns:
        num_of_uniques = len(data[col].unique())
        if num_of_uniques > 1:
            columns_to_keep.append(col)
    return data[columns_to_keep]