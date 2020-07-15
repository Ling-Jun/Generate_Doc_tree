## Development
Set up environment

* Setup up virtual environment with Anaconda, or VENV

>
    $ conda create --name env_name
>
    $ conda activate env_name

* Install Python 3.7.6

* Install dependencies with pip: In our case, all the necessary libraries are provided by the default libraries, so requirements.txt file is empty. For packages needing 3rd party libraries, requirements.txt file wouldn't be.
See [here](https://github.com/Ling-Jun/LSTM-Stock-price/blob/master/requirements.txt)

>
    $ pip install -r requirements.txt


* Alternatively, you can install doctree with (once navigated to doctree directory)

`$ pip install -e .`

## How to generate a doc tree:
Navigate to the folder containing showDirTree.py file, run the following from CLI.

`$ python showDirTree.py --path (uri)`

The default route is set as 'D:/Git/GitWorkingDir/LSTM-Stock-price', change it accordingly.
