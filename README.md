# voice-typing-quiz

## Purpose
Interactive quiz to fresh recall of the commands used in Voice Typing in Google Docs.
Recall of these commands fades in several days after first exposure to them.
The recall falls more slowly with repeted exposure.
This quiz supports the improving the recall.

The quiz has 92 questions.
The answers are generally obvious from the question.

A PDF version of the quiz is supplied for those who are not able to run the interactive quiz.

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

## Run one of two ways

### Run in terminal

```bash
./qVoiceTyping
```

Enter control-D to interupt the quiz.

### Run in Jupyter

The advantage of this approach is that results can be stored in the Notebook.

Check on present working directory in Jupyter.

```bash
!pwd
```

The file qVoiceTyping.py must be in the pwd or you must give the full file path to qVoiceTyping.py.

%run -i "qVoiceTyping.py"
```
