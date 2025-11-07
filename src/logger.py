#this is a file which notes down each step of execution and its a text file
import logging # built in module which provides framework for emitting log messages from Python programs
import os # built in module which interacts with os to  create files,folders,their management,environment variables,and I/O stuff
from datetime import datetime #

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # here .log is and extesion (similar to .txt or .py) it means it will store logs inside it
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # this is to store the path of current working directory of executionnnn( or LOG_FILE)?
os.makedirs(logs_path,exist_ok=True) # it will make a directory as the path is suggesting if it's aleady there then it won't say anyting(nor Error message cuz exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
    
)


 