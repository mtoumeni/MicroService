import mysql.connector
import json
import time

''' Read parameters from file to create database '''

def read_params_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

''' Create database, if not exists '''

def create_Mydatabase(params,retries=3):
    for i in range(retries):
        try:
            mydb = mysql.connector.connect(
                host=params["param1"],
                user=params["param2"],
                passwd=params["param3"]
            )
            mycursor = mydb.cursor()
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {params['param4']}")
            print("DATABASE ready")
            return
        except Exception as e:
            print("Waiting for MySQL...",e)
            time.sleep(3)
    raise Exception("MySQL not reachable")

''' Create table, if not exists '''

def create_table(params,retries=3):
    for i in range(retries):
        try:
            mydb = mysql.connector.connect(
                host=params["param1"],
                user=params["param2"],
                passwd=params["param3"],
                database= params["param4"]
            )
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS measurements (id INT AUTO_INCREMENT PRIMARY KEY,MES FLOAT(2))")
            print("TABLE ready")
            return
        except Exception as e:
            print("Waiting for MySQL...",e)
            time.sleep(3)
    raise Exception("MySQL not reachable")

def main():
    print("start")
    parameters = read_params_json('params.json')
    create_Mydatabase(parameters)
    create_table(parameters)
    print("End")

if __name__ == '__main__':
     main()	
