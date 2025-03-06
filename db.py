from flask import Flask, request
import bson.json_util as json_util


from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['car_rental']
users_collection = db['users']
cars_collection = db['cars']
rentals_collection = db['rentals']

#
# app = Flask(__name__)
#
#
# # root route
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# # Set up MongoDB connection and collection
# client = MongoClient('mongodb://localhost:27017/')
#
# # Create database named demo if they don't exist already
# db = client['temp_database']
#
# # Create collection named data if it doesn't exist already
# collection = db['data']
#
#
# # Add data to MongoDB route
# @app.route('/add_many_data', methods=['POST'])
# def add_many_data():
#     # Get data from request
#     data = request.json
#
#     # Insert data into MongoDB
#     collection.insert_many(data)
#
#     return 'Data added to MongoDB'
#
#
# @app.route('/add_data', methods=['POST'])
# def add_data():
#     # Get data from request
#     data = request.json
#
#     # Insert data into MongoDB
#     collection.insert_one(data)
#
#     return 'Data added to MongoDB'
#
#
# # Get all data from MongoDb
# @app.route('/list_data')
# def list_data():
#     temp = []
#     # temp_record = collection.find({})
#     temp_record = collection.find({}, {'_id': False})
#     d = json_util.dumps(temp_record)
#     dict_needed = json_util.loads(d)
#     print(temp_record)
#
#     # for data in temp_record:
#     #   print(data)
#     #   temp.append(data)
#     # print("Temp",temp)
#     return {"data": dict_needed}, 200
#     # return 'data from database'
#
#
# # Get data for specific id
# @app.route('/list_one_data/<address>')
# def list_one_data(address):
#     one_record = collection.find({'address': address})
#     one_record = collection.find({'address': address}, {'_id': False})
#     d = json_util.dumps(one_record)
#     dict_needed = json_util.loads(d)
#     return {
#         "data": dict_needed
#     }, 200
#
#
# # Delete data for specific id
# @app.route('/delete_many_data/<address>', methods=['DELETE'])
# def delete_many_data(address):
#     delete_record = collection.delete_many({'address': address})
#     return {
#         "data": f'Records deleted successfully with address{address}'
#     }, 200
#
#
# @app.route('/delete_one_data/<address>', methods=['DELETE'])
# def delete_one_data(address):
#     delete_record = collection.delete_one({'address': address})
#     return {
#         "data": 'Record deleted successfully'
#     }, 200
#
#
# # Update data for specific id
# @app.route('/update_many_data/<address>', methods=['POST'])
# def update_many_data(address):
#     data = request.json
#     print(data['age'])
#     update_record = collection.update_many({'address': address}, {"$set": {'age': data['age']}})
#     return {
#         "data": 'Record updated successfully'
#     }, 200
#
#
# @app.route('/update_one_data/<address>', methods=['POST'])
# def update_one_data(address):
#     data = request.json
#     print(data['age'])
#     update_record = collection.update_one({'address': address}, {"$set": {'age': data['age']}})
#     return {
#         "data": 'Record updated successfully'
#     }, 200
#
#
# @app.route('/delete_index/<index>', methods=['DELETE'])
# def delete_index(index):
#     collection.drop_index(index)
#     return {
#         "data": f'Deleted index with name {index}'
#     }, 200
#
#
# @app.route('/delete_indexes/', methods=['DELETE'])
# def delete_indexes():
#     collection.drop_indexes()
#     return {
#         "data": 'Dropped all indexes'
#     }, 200
#
#
# @app.route('/get_indexes/', methods=['GET'])
# def get_indexes():
#     indexes = collection.list_indexes()
#     print(indexes)
#     return {
#         "data": indexes
#     }, 200
#
#
# if __name__ == '__main__':
#     app.run()
