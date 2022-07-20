import docker
import logging
import subprocess
from datetime import datetime




def deepspeechClient:
    client = docker.from_env()

    container = client.containers.run("harbor.ops.veritone.com/challenges/deepspeech", " --audio audio1.wav",
                                      detach=True)




    stats = client.containers.get(container.id).stats(stream=False)



    print(stats)

    for line in container.logs(stream=True):
        print(str(line.strip()))




    CPUDelta =float(stats["cpu_stats"]["cpu_usage"]["total_usage"]) - float(stats["precpu_stats"]["cpu_usage"]["total_usage"])


    SystemDelta = float(stats["cpu_stats"]["system_cpu_usage"]) - float(stats["precpu_stats"]["system_cpu_usage"])


    cpu_count = len(stats['cpu_stats']["cpu_usage"]["percpu_usage"])



    percentage = (CPUDelta / SystemDelta) * 100 * cpu_count



def check_deepSpeech_running:

#I really don't know how I'm going to solve this.
#i wonder if the container is stopped once the operation is done.
#if i can get that from the way that I get stats, I think it should be easy to get that