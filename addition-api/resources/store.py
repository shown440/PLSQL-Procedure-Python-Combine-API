import cx_Oracle
import json

from flask import Flask, request

from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
# from datetime import datetime, timedelta

# from models.store import StoreModel
from db import db



pran_rfl_serviceId = "2"
######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################


class StoreList(Resource):
    # @jwt_required()
    def get(self, id, a, b):
        if id == 2:
            con = cx_Oracle.connect('shifullah/shifullah@10.11.201.251:1521/stlbas')
            cur = con.cursor()

            a = a
            b = b
            c = cur.var(cx_Oracle.NUMBER)
            cur.callproc('test_addition', [a,b,c])
            sum = c.getvalue()

            cur.close()
            con.close()
            return {"Summation": str(sum)}, 200
        else:
            return {"message":"Service ID is unknown"}

# class StoreList(Resource):
#     # @jwt_required()
#     def get(self, id):
#         if id == 2:
#             return {"transactions-detail":[store.json() for store in StoreModel.query.all()]}, 200
#         else:
#             return {"message":"Service ID is unknown"}


# class Store(Resource):
#     # @jwt_required()
#     def get(self, id, todate, fromdate): # , date
#         if str(id) == pran_rfl_serviceId:
#             store = StoreModel.find_by_name(todate, fromdate) # , date
#             if store:
#                 to_datetime_obj = datetime.strptime(todate, '%d-%m-%Y')
#                 from_datetime_obj = datetime.strptime(fromdate, '%d-%m-%Y')
#                 to_datetime = to_datetime_obj.date()
#                 from_datetime = from_datetime_obj.date() + timedelta(days=1)
#                 #print("#####################",to_datetime, " and ", from_datetime)

#                 return {"transactions-datewise":[store.json() for store in StoreModel.query.filter(StoreModel.TRANTIME.between(to_datetime, from_datetime)).all()]}, 200

#             return {"message":" Here is no transactions between {x} and {y}".format(x=todate, y=fromdate)}, 400    #.format(name)
#         else:
#             return {"message":"Service ID is unknown"}
