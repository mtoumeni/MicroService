import mysql.connector
import json
import logging
import time

logger = logging.getLogger(__name__)
path_log = '/usr/tmp'

''' Read database parameters '''

def read_params_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

''' Export value from database and write in the file '''

def export_from_db_to_file(params,retries=3):
    for i in range(retries):
        try:
            mydb = mysql.connector.connect(
                host=params["param1"],
                user=params["param2"],
                passwd=params["param3"],
                database= params["param4"]
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM measurements")
            myresult = mycursor.fetchall()
            
            path_1 = path_log + '/measurements.json'           
            try:
                
                with open(path_1, "r") as measurement:
                    records = json.load(measurement)  
                    previous_records_number = len(records)
            except Exception as e:
                print("Error",e)
                previous_records_number = 0
            
            json_str = json.dumps(myresult, indent=2)
            with open(path_1, "w") as measurement:
                measurement.write(json_str)

            logging.basicConfig(
            filename= path_log +'/export-log.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
            
            current_records_number = mycursor.rowcount - previous_records_number
            logger.info(f"{current_records_number} new records inserted.")
            return
            
        except Exception as e:
            print("Waiting for MySQL...",e)
            time.sleep(3)
    raise Exception("MySQL not reachable")

def main():
    params = read_params_json('params.json')
    export_from_db_to_file(params)

if __name__ == '__main__':
     main()

