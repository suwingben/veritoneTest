import docker
import logging
import subprocess
from datetime import datetime
import os

console_logger = logging.getLogger("console")

#Making a single function to handle all our interaction with the container.
def deepspeechClient(audio_file, test_container):

    client = docker.from_env()
    #Setting start  time
    startTime = datetime.now()
    container = client.containers.run(
        test_container, f"--audio  {audio_file}", "cpus=1", detach=True
    )
    container_id = container.id
    cpu_sanitized_percentage = 0
    cpu_stats = get_container_cpu(container)

    #For whatever reason, cpu_stats was coming back as a list but it wasn't letting me do sum.
    #Have to do a for loop to get every value and then sanitize the percentage to make it a number
    #I'm not 100% sure why this happens though
    for x in cpu_stats:
        cpu_sanitized_percentage += float(x)

    cpu_calculated = cpu_sanitized_percentage / len(cpu_stats)

    endTime = datetime.now()

    #look at the log stream and snag the last line.
    #this might be super risky and needs something a little more precise if the last line of the output is ever changed
    for line in container.logs(stream=True):
        transcription = str(line.strip(), "utf-8")
    #quik maffs
    timeTaken = (endTime - startTime).total_seconds()
    #start test logger to get the goodies
    test_logger = logging.getLogger("test_data_log")

    file_size = get_container_file_info(container_id, audio_file)
    console_logger.info(f"The time taken is: {timeTaken}")
    console_logger.info(f"The the cpu percentage is: {cpu_calculated}")
    console_logger.info(f"The file size is: {file_size}")
    test_logger.info(f"Total Time: {timeTaken}")
    test_logger.info(f"Total CPU: {cpu_calculated}")
    test_logger.info(f"File Size of {audio_file}: {file_size}")

    return transcription


#This will go and run the CLI for docker to get more advanced information at runtime on the container.
def get_container_cpu(container):

    cpu_stats = []

    container.reload()

    while container.attrs["State"]["Running"]:
        percent = subprocess.Popen(
            ["docker", "stats", "--no-stream", "--format", "{{.CPUPerc}}"],
            stdout=subprocess.PIPE,
        ).communicate()

        if percent:
            # Byte strings were coming so everything had to be formatted to UTF-8
            percent_sanitized = str(percent[0], "utf-8").split("%", 1)
            #Couldn't do the math I needed on the other side if there were empty strings, had to replace with 0.
            if percent_sanitized[0] == "":
                percent_sanitized[0] = "0"
            cpu_stats.append(percent_sanitized[0])
        container.reload()

    return cpu_stats

#Grabs the files from the container per test and deletes them so not to use up storage unreasonably.
def get_container_file_info(container_id, audio_file):
    file_download_dir = "../test_file_download/"

    #copy the file using the docker CP command
    #quick and dirty but worked well once i added .communicate
    copy_file = subprocess.Popen(
        [
            "docker",
            "cp",
            f"{container_id}:/DeepSpeech/{audio_file}",
            f"{file_download_dir}/{audio_file}",
        ]
    ).communicate()

    #If a file's found, do some math on the file size so that it's human readable
    #
    if copy_file:
        file_size = str(
            os.path.getsize(f"{file_download_dir}/{audio_file}")
            / 1024**2
        )
        os.remove(f"{file_download_dir}/{audio_file}")

    return file_size
