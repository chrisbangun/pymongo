import pymongo
from pymongo import MongoClient
import sys

class MongoDB:

  def __init__(self):
    self.mongo_client = MongoClient('localhost',27017)

  def get_collections(self,db_name):
    mongo_db = self.mongo_client[db_name]
    collections = mongo_db.collection_names()
    for collection in collections:
      print collection

  def get_dbs(self):
    dbs = self.mongo_client.database_names()
    list_of_db = str(dbs).split(' ')
    for db in list_of_db:
      db = db.replace("u\"","\"").replace("u\'","\'").replace("[","").replace("]","").replace("'","").replace(",","")
      print u"%s" % db.encode('utf-8')

class Main:
  db_name = ""
  mongoDb = None

  def __init__(self,db_name):
    self.db_name = db_name
    self.mongoDb = MongoDB()

  def get_db_collections(self):
    self.mongoDb.get_collections(self.db_name)

  def get_dbs(self):
    self.mongoDb.get_dbs()

if __name__ == '__main__':
  db_name = ""

  if len(sys.argv) > 1:
    db_name = sys.argv[1]
    main = Main(db_name)
    main.get_db_collections()
  else:
    print "list of DBs"
    main = Main("")
    main.get_dbs()
    print
    print "usage: get-mongo-dbs.py [dbName]"
