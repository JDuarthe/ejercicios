def making_response(pending_orders, shipped_orders, cancelled_orders):
    result = []
    [result.append({"order_number": x[0], "status": x[1]}) for x in pending_orders]
    [result.append({"order_number": x[0], "status": x[1]}) for x in shipped_orders]
    [result.append({"order_number": x[0], "status": x[1]}) for x in cancelled_orders]
    return result