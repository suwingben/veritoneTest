import docker
import logging
import subprocess
from datetime import datetime




def deepspeechClient(audio_file,test_container):
    client = docker.from_env()


    startTime = datetime.now()
    container = client.containers.run(test_container, f'--audio  {audio_file}','--cpus="1"',detach=True)


    cpu_stats = get_container_cpu_stats(container)


    endTime = datetime.now()
    for line in container.logs(stream=True):
        transcription = str(line.strip(), 'utf-8')

    timeTaken = (endTime-startTime).total_seconds()

    print(timeTaken)
    print(cpu_stats)

    return transcription



    # I really don't know how I'm going to solve this getting runtime information on the container.
    # i wonder if the container is stopped once the operation is done.
    # if i can get that from the way that I get stats, I think it should be easy to get that
    # need to track time too


def get_container_cpu_stats(container):


    cpu_stats = []


    container.reload()

    while container.attrs['State']['Running']:
        stdout = subprocess.Popen(['docker', 'stats', '--no-stream', '--format', '{{.CPUPerc}}'], stdout=subprocess.PIPE).communicate()

        if stdout:
            cpu = float(stdout[-2])
            cpu_stats.append(cpu)
        container.reload()


    return cpu_stats