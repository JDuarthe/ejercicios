from flask import Blueprint, request, jsonify
from datetime import datetime
from .src.orders import making_response
from .src.detecting import check_rain
from .src.season import process_data

api = Blueprint('api', 'api')

@api.route('/')
def index():
    return 'Hello'


@api.route('/detecting-change')
def detecting_change():
    my_data = [
        {"date": '1/1/20', "was_rainy": 'FALSE'},
        {"date": '1/2/20', "was_rainy": 'TRUE'},
        {"date": '1/3/20', "was_rainy": 'TRUE'},
        {"date": '1/4/20', "was_rainy": 'FALSE'},
        {"date": '1/5/20', "was_rainy": 'FALSE'},
        {"date": '1/6/20', "was_rainy": 'TRUE'},
        {"date": '1/7/20', "was_rainy": 'FALSE'},
        {"date": '1/8/20', "was_rainy": 'TRUE'},
        {"date": '1/9/20', "was_rainy": 'TRUE'},
        {"date": '1/10/20', "was_rainy": 'TRUE'},
    ]

    rain_filters = {"status": False}
    result = list(filter(lambda value: check_rain(value, rain_filters), my_data))
    return jsonify(result)


@api.route('/season-problem')
def season_problem():
    my_data = [
        {"ORD_ID": "113-8909896-6940296", "ORD_DT": "9/23/19", "QT_ORDD": 1},
        {"ORD_ID": "114-0291773-7262677", "ORD_DT": "1/1/20", "QT_ORDD": 1},
        {"ORD_ID": "114-0291773-7262697", "ORD_DT": "12/15/19", "QT_ORDD": 1},
        {"ORD_ID": "114-9900513-7761000", "ORD_DT": "9/24/20", "QT_ORDD": 1},
        {"ORD_ID": "112-5230502-8173028", "ORD_DT": "1/30/20", "QT_ORDD": 1},
        {"ORD_ID": "112-7714081-3300254", "ORD_DT": "5/2/20", "QT_ORDD": 1},
        {"ORD_ID": "114-5384551-1465853", "ORD_DT": "4/2/20", "QT_ORDD": 1},
        {"ORD_ID": "114-7232801-4607440", "ORD_DT": "10/9/20", "QT_ORDD": 1},
    ]

    data_convert = list(map(process_data, my_data))
    return jsonify(data_convert)


@api.route('/customer-orders')
def customer_order():
    given_status = {'SHIPPED', 'CANCELLED', 'PENDING'}
    my_data = [
        {'customer_order': 'ORD_1567', 'item_name': 'LAPTOP', 'status': 'SHIPPED' },
        {'customer_order': 'ORD_1567', 'item_name': 'MOUSE', 'status': 'SHIPPED' },
        {'customer_order': 'ORD_1567', 'item_name': 'KEYBOARD', 'status': 'PENDING' },
        {'customer_order': 'ORD_1234', 'item_name': 'GAME', 'status': 'SHIPPED' },
        {'customer_order': 'ORD_1234', 'item_name': 'BOOK', 'status': 'CANCELLED' },
        {'customer_order': 'ORD_1234', 'item_name': 'BOOK', 'status': 'CANCELLED' },
        {'customer_order': 'ORD_9834', 'item_name': 'SHIRT', 'status': 'SHIPPED' },
        {'customer_order': 'ORD_9834', 'item_name': 'PANTS', 'status': 'CANCELLED' },
        {'customer_order': 'ORD_7654', 'item_name': 'TV', 'status': 'CANCELLED' },
        {'customer_order': 'ORD_7654', 'item_name': 'DVD', 'status': 'CANCELLED' },
        ]
        
    order_numbers = list(map(lambda elem: [elem.get('customer_order'), elem.get('status')], my_data))
    holder = []
    [holder.append(x) for x in order_numbers if x not in holder] 

    pending_orders = [x for x in holder if 'PENDING' in x]

    shipping_and_cancelled = [x for x in holder if 'PENDING' not in x]

    not_repeated = [z for z in shipping_and_cancelled if z[0] not in [x[0] for x in pending_orders]]

    shipped_orders = [x for x in not_repeated if 'CANCELLED' not in x] 

    cancelled_orders = [z for z in not_repeated if z[0] not in [x[0] for x in shipped_orders]] 


    order_response = making_response(pending_orders, shipped_orders, cancelled_orders)
    return jsonify(order_response)