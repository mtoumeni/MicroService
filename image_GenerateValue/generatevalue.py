import mysql.connector
import random
import json
import logging
import time

logger = logging.getLogger(__name__)
path_log = '/usr/tmp'
''' Read database parameters '''

def read_params_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

''' Generate random value, save it in the database and write in the log file '''

def genarate_value(params,retries=3):
    for i in range(retries):
        try:
            mydb = mysql.connector.connect(
                host=params["param1"],
                user=params["param2"],
                passwd=params["param3"],
                database= params["param4"]
            )
            MES_value = random.uniform(37, 38)
            MES_value = round(MES_value,2)
            mycursor = mydb.cursor()
            Formula = "INSERT INTO measurements (MES) VALUES (%s)"
            mycursor.execute(Formula, (MES_value,))

            mydb.commit()
            
            logging.basicConfig(
            filename= path_log +'/generateValue.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
            
            logger.info(f"{mycursor.rowcount} new record inserted: {MES_value}")
            return

        except Exception as e:
            print("Waiting for MySQL...",e)
            time.sleep(3)
    raise Exception("MySQL not reachable")

def main():
    params = read_params_json('params.json')
    genarate_value(params)

if __name__ == '__main__':
     main()
