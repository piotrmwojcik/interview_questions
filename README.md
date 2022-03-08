# PhD interview coding question

The code in this repo solves the problem of labeling connected areas in a given image.

## Running the code

Please clone the repo:

`git clone https://github.com/piotrmwojcik/interview_questions`

then, inside the directory, type:

`conda env create -f env.yaml`

Activate the environment:

`conda activate interview_phd`

Now, unit test suit can be launched by the following command:

`export PYTHONPATH=$PYTHONPATH:src; python -m unittest -v tests/test_connected_components.py`
