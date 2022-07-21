# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import docker
import jiwer
import psutil
from jiwer import wer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

client = docker.from_env()

container = client.containers.run("harbor.ops.veritone.com/challenges/deepspeech", " --audio audio1.wav", detach=True)



stats = client.containers.get(container.id).stats(stream=False)

print(stats)

for line in container.logs(stream=True):
    print(str(line.strip()))


actual_phrase = "razu you must hurry you must stay the path "


print(str(container))

error_rate = jiwer.wer(actual_phrase, str(line.strip()))

print(error_rate)


CPUDelta =float(stats["cpu_stats"]["cpu_usage"]["total_usage"]) - float(stats["precpu_stats"]["cpu_usage"]["total_usage"])


SystemDelta = float(stats["cpu_stats"]["system_cpu_usage"]) - float(stats["precpu_stats"]["system_cpu_usage"])


cpu_count = len(stats['cpu_stats']["cpu_usage"]["percpu_usage"])



percentage = (CPUDelta / SystemDelta) * 100 * cpu_count


print(percentage)

print_hi('PyCharm')

print(stats)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
