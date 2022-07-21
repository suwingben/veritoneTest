import docker
import logging
import subprocess
from datetime import datetime




def deepspeechClient(audio_file,test_container):
    client = docker.from_env()

    container = client.containers.run(test_container, f'--audio  {audio_file}',detach=True)



    for line in container.logs(stream=True):
        transcription = str(line.strip(),'utf-8')


    return transcription



    # I really don't know how I'm going to solve this getting runtime information on the container.
    # i wonder if the container is stopped once the operation is done.
    # if i can get that from the way that I get stats, I think it should be easy to get that
    # need to track time too



