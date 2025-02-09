import logging
import os
from datetime import datetime

LOGFILE=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOGFILE)
os.makedirs(logs_path,exist_ok=True)

LOGFILE_PATH=os.path.join(logs_path,LOGFILE)
logging.basicConfig(filename=LOGFILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

""" if __name__=="__main__":
    logging.info("Logging has started") """