import docker
import logging
import subprocess
from datetime import datetime
import os

console_logger = logging.getLogger("console")


def deepspeechClient(audio_file, test_container):

    client = docker.from_env()

    startTime = datetime.now()
    container = client.containers.run(
        test_container, f"--audio  {audio_file}", "cpus=1", detach=True
    )
    container_id = container.id
    cpu_sanitized_percentage = 0
    cpu_stats = get_container_cpu(container)

    for x in cpu_stats:
        cpu_sanitized_percentage += float(x)

    cpu_calculated = cpu_sanitized_percentage / len(cpu_stats)

    endTime = datetime.now()
    for line in container.logs(stream=True):
        transcription = str(line.strip(), "utf-8")

    timeTaken = (endTime - startTime).total_seconds()
    test_logger = logging.getLogger("test_data_log")

    file_size = get_container_file_info(container_id, audio_file)
    console_logger.info(f"The time taken is: {timeTaken}")
    console_logger.info(f"The the cpu percentage is: {cpu_calculated}")
    console_logger.info(f"The file size is: {file_size}")
    test_logger.info(f"Total Time: {timeTaken}")
    test_logger.info(f"Total CPU: {cpu_calculated}")
    test_logger.info(f"File Size of {audio_file}: {file_size}")

    return transcription


def get_container_cpu(container):

    cpu_stats = []

    container.reload()

    while container.attrs["State"]["Running"]:
        percent = subprocess.Popen(
            ["docker", "stats", "--no-stream", "--format", "{{.CPUPerc}}"],
            stdout=subprocess.PIPE,
        ).communicate()

        if percent:
            percent_sanitized = str(percent[0], "utf-8").split("%", 1)
            if percent_sanitized[0] == "":
                percent_sanitized[0] = "0"
            cpu_stats.append(percent_sanitized[0])
        container.reload()

    return cpu_stats


def get_container_file_info(container_id, audio_file):
    file_download_dir = "../test_file_download/"


    copy_file = subprocess.Popen(
        [
            "docker",
            "cp",
            f"{container_id}:/DeepSpeech/{audio_file}",
            f"{file_download_dir}/{audio_file}",
        ]
    ).communicate()

    if copy_file:
        file_size = str(
            os.path.getsize(f"{file_download_dir}/{audio_file}")
            / 1024**2
        )
        os.remove(f"{file_download_dir}/{audio_file}")

    return file_size
