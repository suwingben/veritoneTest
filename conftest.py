import logging
import pytest
import datetime
import os


logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
console_logger = logging.getLogger("console")



#logic around building out a few folders needed for the test. I think I could have gone into the rollup fixture and used it more as a teardown to get rid of that download folder.
#I wonder if this could be a different fixture?
log_directory = "../logs/"
file_download_dir = "../test_file_download/"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
log_path = os.path.join(log_directory, timestamp)
if not os.path.exists(log_path):
    os.makedirs(log_path)
if not os.path.exists(file_download_dir):
    os.makedirs(file_download_dir)
if not os.path.exists(log_directory):
    os.makedirs(log_directory)



#This needs to be set to autouse so that it'll be run at the beginning of every test iteration.
#Learning how to use the handlers was pretty silly. Loading the fixture without clearing out the handlers had some pretty hilarious results.
#For example, the log file for audio_1.wav was loaded with the test data for all the subsequent tests.
@pytest.fixture(autouse=True)
def gather_the_logs(request):

    logger = logging.getLogger("test_data_log")
    logger.handlers= []
    logger.addHandler(logging.FileHandler(f"{log_path}/{request.node.callspec.params['audio_file']}.log"))
    logger.propagate = False



#Have to scope this to session so that we can run it after the entire run.
@pytest.fixture(scope="session", autouse=True)
def roll_up_the_logs(request):

    yield

    rollup_log = logging.getLogger("roller")

    rollup_log.addHandler(
        logging.FileHandler(f"{log_path}/rollup_log_file.log")
    )
    time_aggregate = []
    accuracry_aggregate = []
    cpu_aggregate = []


    #Search the directory holding the logs defined at the top.
    #Snag all the files and read them for specific phrases.
    #Split on the colon and get the goodies afterwards.
    #Proper punctuation made the math messy because strings, so no punctuation in the logs :(
    for filename in os.listdir(log_path):
        with open(f'{log_path}/{filename}') as file:
            for line in file.readlines():
                if "Total Time" in line:
                    time_aggregate.append(float(line.split(":")[1]))
                elif "Accuracy" in line:
                    accuracry_aggregate.append(float(line.split(":")[1]))
                elif "Total CPU" in line:
                    cpu_aggregate.append(float(line.split(":")[1]))


    #Do the math and roll up all the log data.
    rollup_log.info("Test Summary:")
    rollup_log.info(f"Average CPU usage: {sum(cpu_aggregate)/len(cpu_aggregate)}")
    rollup_log.info(f"Average Accuracy percentage: {sum(accuracry_aggregate)/len(accuracry_aggregate)}")
    rollup_log.info(f"Average time taken(in seconds):{sum(time_aggregate)/len(time_aggregate)}")
