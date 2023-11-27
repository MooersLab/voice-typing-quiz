# voice-typing-quiz

## Purpose
Interactive quiz to fresh recall of the commands used in Voice Typing in Google Docs.
Voice Typing is found under the Tools pulldown menu.

Recall of these commands fades in several days after first exposure to them.
The recall decreases more slowly with repeated exposure.
This quiz supports improving the recall.


# Content
The quiz has 92 questions.
The answers are generally obvious from the question.

A PDF version of the quiz is provided for those who are unable to run the interactive quiz.


## Features

- randomizes questions on each run
- reports number of correct answers
- reports time spent on quiz


## Recommeded usage
Run through questions repeatedly until recall is better than 90 percent and then get back to work.
One pass may take 10 minutes initially. 
After several passes, you will be able to use Voice Typing in an agile fashion.
Retaking the every 2-3 days five times were reduce the decay of your recall of the commands.
Unfortunately, most of us are too busy for such a disciplined approach.


## Disclaimer
This is a programming tool, not an educational tool.
It provides no explanations and no context.
It just improves recall of commands in a rote manner.


## Prerequisites
You need a recent version of Python3.
You also need one external module.
Install the module **pytictoc** with pip or conda.

```bash
pip install --user --upgrade pytictoc
```

or with conda

```bash
conda activate <env name>
conda install pytictoc
```

If you have an older version of python3, install the module **tictoc** instead.

## Run one of two ways.

You will be asked to enter a number between 1 and 1. Enter 1.
Then the interactive quiz will run.

### Run in terminal

```bash
./qVoiceTyping
```

Enter control-D to interupt the quiz.

### Run in Jupyter
Use in Jupyter Notebook, JupyterLab, [JupyterLab.app](https://blog.jupyter.org/jupyterlab-desktop-app-now-available-b8b661b17e9a), or [nteract.app](https://nteract.io/).
Probably works in Colab too.
Select the approprite Python kernel that taps into the Python interpreter with pytictoc installed.

The advantages of this approach is that results can be stored in the Notebook and its more fun to run the quiz in the notebook.

Check on present working directory in Jupyter by entering the following in a code cell.

```bash
!pwd
```

The file qVoiceTyping.py must be in the pwd or you must give the full file path to qVoiceTyping.py.
Enter the following in another code cell.

```bash
%run -i "qVoiceTyping.py"
```
