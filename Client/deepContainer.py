import docker
import logging
import subprocess
from datetime import datetime

test_log = logging.getLogger('test_logger')
console_log = logging.getLogger('console')

def deepspeechClient(audio_file,test_container):
    client = docker.from_env()


    startTime = datetime.now()
    container = client.containers.run(test_container, f'--audio  {audio_file}','cpus=1',detach=True)


    cpu_stats = get_container_cpu_stats(container)


    endTime = datetime.now()
    for line in container.logs(stream=True):
        transcription = str(line.strip(), 'utf-8')

    timeTaken = (endTime-startTime).total_seconds()

    console_log.debug(f'The time taken is: {timeTaken}')
    console_log.debug(f'The the cpu percentage is: {cpu_stats}')
    test_log.debug(f'The time taken is: {timeTaken}')
    test_log.debug(f'The cpu percentage is: {cpu_stats}')


    return transcription



def get_container_cpu_stats(container):


    cpu_stats = []


    container.reload()

    while container.attrs['State']['Running']:
        percent = subprocess.Popen(['docker', 'stats', '--no-stream', '--format', '{{.CPUPerc}}'], stdout=subprocess.PIPE).communicate()

        if percent:
            percent_sanitized = str(percent[0],'utf-8').split('%',1)
            cpu_stats.append(float(percent_sanitized[0]))
        container.reload()


    return cpu_stats
