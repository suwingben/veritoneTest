# Deepspeech Tester
###### By Suwing Ben

## 1.  Thank you
Thanks for taking time to review my submission for this code test. It made me flex some brain muscles that I hadn't for a long time. So minimally, this was a tremendously rewarding experience to help me "get my groove back"

## 2.  Running
You'll need to already have python 3 and pip installed.

1. Make a new virtual environment
   1. ```python3 -m venv test_run_env```
2. Activate your new virtual environment
   1. ```source test_run_env/bin/activate```
3. Install the required packages
   1. ```pip install -r requirements.txt```
4. Call Pytest to run the tests
   1. ```pytest tests```
5. Close it up when you'e all done.
   1. ```deactivate```

## 3. Reporting
Reports are going to be output into a folder based on the current time stamp (YYYY-MM-DD-HH-MM-SS)

    ```example: logs/2022-07-22-15-39-42```
Logs are being captured per test as [audio_file].log

The aggregate report which contains the average across all runs will also be located in this as
rollup_log_file.log

## 4.  Notes
1. [Parametrize from file](https://parametrize-from-file.readthedocs.io/en/latest/index.html)
was a livesaver in making this parameterized very quickly. Super simple to use and get implemented.
2. I'm snagging the sound files off of the container and depending on where this gets run, you might out of space but it shouldn't matter.
3. YML file should probably have a .dist just to show what test cases we're attempting as well as making sure random nastiness doesn't get commited.
4. I'm trash at commenting my code which will likely be a nightmare for whoever has to read this.
5. I preloaded the INI with some default values regarding how many lines of traceback and default log stuff. You might not need it
6. Make sure you take care of yourself.
## 5. Contributing
Need to change the number of tests running?```test_deepspeech.yml``` just add or remove a grouping from the yml file.

Need to modify the verification? ```verification/verify_wer.py``` has all the goodies you need to change what's being logged and verified with the WER calculation.

Need to modify interaction with the deepSpeech container? ```client/deepContainer.py``` has all the goodies for interactions with the docker container.
