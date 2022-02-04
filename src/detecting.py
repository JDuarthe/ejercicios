def check_rain(value, rain_filters):
    if value.get('was_rainy') == 'TRUE' and rain_filters.get('status') == False:
        rain_filters['status'] = True
        return value
    
    if value.get('was_rainy') == 'FALSE' and rain_filters.get('status') == True:
        rain_filters['status'] = False

