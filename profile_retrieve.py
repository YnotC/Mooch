import pymysql
import getpass
from flask import Flask
from datetime import datetime

#connection = pymysql.connect(host = 'localhost', user = 'root', password = getpass.getpass(), database = 'humane')

"""
def create_database:
    with connection.cursor() as cursor():
        cursor().execute('DROP DATABASE IF EXISTS profiles')
        cursor().execute('CREATE DATABASE profiles')
        cursor().execute('USE profiles')
        cursor().execute('CREATE TABLE user (email VARCHAR(30) PRIMARY KEY, name VARCHAR(20), venmo_id VARCHAR(30), item_id INT, lat DECIMAL(10,8), lng DECIMAL(11,8))')
        cursor().execute('CREATE TABLE user_images (user_image_path VARCHAR(100) PRIMARY KEY, email VARCHAR(30), FOREIGN KEY (user_id) REFERENCES user(user_id))')
        cursor().execute('CREATE TABLE item (item_id INT PRIMARY KEY, name VARCHAR(20), price double(3,2), avail_start DATETIME, avail_end DATETIME = NULL, description VARCHAR(MAX) = '', FOREIGN KEY (email) REFERENCES user(email))')
        cursor().execute('CREATE TABLE requests (request_id INT PRIMARY KEY AUTO_INCREMENT, keywords VARCHAR(50), avail_start VARCHAR(20), avail_end VARCHAR(20)')

def insert_user(params):
    r = params
    with connection.cursor() as cursor:
        sql = 'insert into users values (%s, %s, %s, %8f, %8f)'
        user_attrs = (r.args['email'], r.args['name'], r.args['venmo_id'], r.args['lat'], r.args['lng'])
        cursor.execute(sql, args = user_attrs)

def insert_item(params):
    r = params
    with connection.cursor() as cursor:
        sql = 'insert into item values (%d, %s, %2f, %s, %s, %s, %s)'
        item_attrs = (r.args['item_id'], r.args['name'], r.args['price'], r.args['avail_start'], r.args['avail_end'], r.args['description'], r.args['email'])
        cursor.execute(sql, args = item_attrs)

def insert_image(params):
    r = params
    with connection.cursor() as cursor:
        sql = 'insert into user_images values (%s, %s)'
        image_attrs = (r.args['user_image_path'], r.args['email'])
        cursor.execute(sql, args = image_attrs)

def insert_request(params):
    r = params
    with connection.cursor() as cursor:
        sql = 'insert into user_images values (%s, %s, %s)'
        request_attrs = (r.args['keywords'], r.args['avail_start'], r.args['avail_end'])
        cursor.execute(sql, args = request_attrs)

def get_all_users:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM user JOIN user_images USING(email)')
        profiles = cursor.fetchall()
        profile_dict = {'Users': ['']}
        for profile in profiles:
            profile_dict['Users'].append({'email': profile[0], 'name': profile[1], 'venmo_id': profile[2], 'lat': profile[3], 'lng': profile[4], 'user_image': profile[5]})
        del profile_dict['Users'][0]
        return profile_dict

def get_specific_user(param):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM user JOIN user_images USING(email) WHERE user.email = ' + param.args['email'])
        profiles = cursor.fetchall()
        profile_dict = {'email': profile[0], 'name': profile[1], 'venmo_id': profile[2], 'lat': profile[3], 'lng': profile[4], 'user_image': profile[5]}
        return profile_dict
"""
def get_all_items():
     with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM item_list')
        items = cursor.fetchall()
        item_dict = {'Items': ['']}
        for item in items:
            item_dict['Items'].append({'item_id': [0], 'name': item[1], 'price': item[2], 'avail_start': CONVERT(datetime, item[3]), 'avail_end': CONVERT(datetime, item[4]), 'description': item[5], 'email': item[6]})
        del item_dict['Items'][0]
        return item_dict
"""
def get_specific_item(email):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM item_list JOIN user USING(email) WHERE user.email = ' + email)
        items = cursor.fetchall()
        item_dict = {'item_id': [0], 'name': item[1], 'price': item[2], 'avail_start': CONVERT(datetime, item[3]), 'avail_end': CONVERT(datetime,item[4]), 'description': item[5], 'email': item[6], 'venmo_id': item[7], 'lat': item[7], 'lng': item[9], 'user_image': item[10]}
        return item_dict
"""
# def search_items(keyword, avail_start, avail_end):
#    with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM item_list \
#             JOIN user USING(email) \
#             WHERE item_list.name LIKE '%" + keyword + "%' \
#             AND " + CONVERT(datetime, avail_start) + " BETWEEN " + item_list.avail_start + " AND " + item_list.avail_end \
#             "AND " + CONVERT(datetime, avail_start) + "BETWEEN " + item_list.avail_end + " AND " + item_list_avail_end)
#         items = cursor.fetchall()
#         item_dict = {'item_id': [0], 'name': item[1], 'price': item[2], 'avail_start': CONVERT(datetime, item[3]), 'avail_end': CONVERT(datetime,item[4]), 'description': item[5], 'email': item[6], 'venmo_id': item[7], 'lat': item[7], 'lng': item[9], 'user_image': item[10]}
#         return item_dict
"""
def get_requests:
   with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM requests')
        requests = cursor.fetchall()
        requests_dict = {'Requests': ['']}
        for request in requests:
            requests_dict['Requests'].append('request_id': requests[0], 'keywords': requests[1], 'avail_start': requests[2], 'avail_end': requests[3])
        del requests_dict[0]
        return requests_dict

def"""
"""
command, param

request:
query
start
end - blank if empty
"""


"""create_database()"""


"""takes in a tuple of (command, params)"""
@profile_retrieve.route('/moochapi/v1',methods['GET'])
def v1():
    method_name = request.args.get('method_name', default = "NONE", type = str)
    keyword = request.args.get('keyword', default = "NONE", type = str)
    avail_start = request.args.get('avail_start', default = 'NONE', type = str)
    avail_end = request.args.get('avail_end', default = 'NONE', type = str)
    if method_name == 'GET_ALL_ITEMS':
        return 'Hello World'
        """get_all_items()"""
        """
    elif method_name == 'SEARCH_ITEMS':
        return search_items(keyword, avail_start, avail_end)"""
    """elif method_name == 'INSERT_USER':
        return insert_user(requests[1])
    elif method_name == 'INSERT_ITEM':
        return insert_item(requests[1])
    elif method_name == 'INSERT_IMAGE':
        return insert_image(requests[1])
    elif method_name == 'INSERT_REQUEST':
        return insert_request(requests[1])
    elif method_name == 'GET_REQUESTS':
        return get_requests()
    elif method_name == 'GET_PROFILE_INFORMATION':
        return get_specific_user()
    else:
        return "PLS FIX CODE"""""
