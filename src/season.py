from datetime import datetime
def process_data(value):
    obj_date = datetime.strptime(value["ORD_DT"], '%m/%d/%y')
    if obj_date.month > 2 and obj_date.month < 7:
        if obj_date.month > 3 and obj_date.month < 6:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Spring"}
        if obj_date.month == 3 and obj_date.day >= 19:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Spring"}
        if obj_date.month == 6 and obj_date.day <= 19:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Spring"}
    
    if obj_date.month > 5 and obj_date.month < 10:
        if obj_date.month > 6 and obj_date.month < 9:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Summer"}
        if obj_date.month == 6 and obj_date.day >= 20:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Summer"}
        if obj_date.month == 9 and obj_date.day <= 21:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Summer"}

    if obj_date.month > 8 and obj_date.month <= 12:
        if obj_date.month > 9 and obj_date.month < 12:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Fall"}
        if obj_date.month == 9 and obj_date.day >= 22:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Fall"}
        if obj_date.month == 12 and obj_date.day <= 20:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Fall"}
    
    if obj_date.month <= 3:
        if obj_date.month < 3:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Winter"}
        if obj_date.month == 3 and obj_date.day <= 18:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Winter"}
        if obj_date.month == 12 and obj_date.day > 20:
            return {"ORD_ID": value["ORD_ID"], "SEASON": "Winter"}

    return {"ORD_ID": value["ORD_ID"], "SEASON": "not-set"}



