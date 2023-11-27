#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode
# For information on the q symbols package
# http://ftp.cvut.cz/tex-archive/macros/latex/contrib/qsymbols/qsymbols.pdf
# q symbols package

# prevent python2 from reading print('asd','add') as a tuple.


from __future__ import print_function

from random import shuffle
from pytictoc import TicToc

import datetime
import sys
import inspect
import types

print(" ")
print("Usage: ./qVoiceTyping.py")
print(" ")


'''
Note that raw_input() in Python2 is replaced with input() in Python3.

This is a very simple program that runs an interactive quiz
composed of fill in the blank and  short answers.

The quiz is assembled from a list of tuples
of questions, answers, and information source.

A List is a mutable type meaning that lists can
be modified after they have been created.
List keep order, which makes them amendable to shuffling.

A tuple is similar to a list except it is immutable.
Tuples have structure, lists have order.

Adding new tuples manually is error prone due to all of the
single quotes and commas. These are easy to omit.
Use a snippet like tup3 ior sublime text 3
with placeholders to avoid omitting this symbols.


<snippet>
    <content><![CDATA[
('${1:paster over me}','${2:paste here}','${3:paste here}'),
]]></content>
    <!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
<tabTrigger>tup3</tabTrigger>
    <!-- Optional: Set a scope to limit where the snippet will trigger -->
<scope>source.python</scope>
</snippet>


Inspired by: https://www.youtube.com/watch?v=VR-yNEpGk3g

Modified to include source information in the tuple, and
to print more explanatory information such as the number
of questons in the quiz.

What is not allowed in an element of the tuple without escaping it:
    single quotes,
    double quotes,
    parentheses,
    curly braces,
    square brackets,
    colons,
    backslash,
    tilde,
    pound sign.


What is allowed?

Two ways to escape characters in a string.

escaped = a_string.translate(str.maketrans({"-":  r"\-",
  "]":  r"\]",
  "\": r"\",
  "^":  r"\^",
  "$":  r"\$",
  "*":  r"\*",
  ".":  r"\."}))


import re
escaped = re.escape(a_string)

unicode for writing equations to the terminal
source http://xahlee.info/comp/unicode_math_operators.html

α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς τ υ φ χ ψ

Superscript: ⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾

Natural Numbers ℕ,
Integers ℤ,
Rational Numbers ℚ,
Real Numbers ℝ,
Complex Numbers ℂ

circled {plus, times, …} ⊕ ⊖ ⊗ ⊘

empty set ∅

element of ∈ ∋

integrals ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ⨋ ⨌ ⨍ ⨎ ⨏ ⨐ ⨑ ⨒ ⨓ ⨔ ⨕ ⨖ ⨗ ⨘ ⨙ ⨚ ⨛ ⨜

n-nary sum ∑ ⨊ ⨁

n-nary product ⨀ ⨂ ∏ ∐ ⨉

Copyright Notice
================

Copyright (C) 2019
Blaine Mooers and University of Oklahoma Board of Regents

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details:
http://www.gnu.org/licenses/.
The source code in this file is copyrighted, but you can
freely use and copy it as long as you do not change or remove any of
the copyright notices.

Blaine Mooers, PhD
blaine-mooers@ouhsc.edu
975 NE 10th St, BRC 466
University of Oklahoma Health Sciences Center,
Oklahoma City, OK, USA 73104

Blaine Mooers

First version to write out a functional quiz using questions assembled
in a sqlite database of questions.
'''
__author__ = "Blaine Mooers"
__copyright__ = "2019 Board of Regents for the University of Oklahoma"
__license__ = "MIT Licencse"
__version__ = "0.1.0"
# Versioning follows follows MAJOR.MINOR[.PATCH] where major releases are
# not backward compatable.
__credits__ = [""]
# Credits are for people who have
#    tested the code,
#    reported bug fixes,
#    made suggestions, etc.
__date__ = "31 October 2019"
__maintainner__ = "Blaine Mooers"
__email__ = "blaine-mooers@ouhsc.edu"
__status__ = "Developement"

DT = datetime.datetime.now().strftime("yr%Ymo%mday%dhr%Hmin%Msec%S");

'''
The seconds are included so that the program can be rerun in less
than a minute without over writing a previous copy.
Note that the captial S gives the secconds in the current minute.
Lowercase s gives the number of seconds from some reference time.
'''

TSTAMP = str(DT);

def all_q():
    q_all = [
        ("To apply a lowercase to a selection, say ______.", "lowercase", "1", "1"),
    ("To apply a subscript to a selection, say ______.", "subscript", "1", "1"),
    ("To apply a superscript to a selection, say ______.", "superscript", "1", "1"),
    ("To apply a title case to a selection, say ______ ____.", "title case", "1", "1"),
    ("To apply a underline to a selection, say ______.", "underline", "1", "1"),
    ("To apply a uppercase to a selection, say ______.", "uppercase", "1", "1"),
    ("To apply blue to the background of a selection, say ______ ____ _____.", "background color blue", "1", "1"),
    ("To apply bold to a selection, say ______.", "bold", "1", "1"),
    ("To apply heading level 1 to a selection, say ______ ___ __.", "apply heading 1", "1", "1"),
    ("To apply heading level 6 to a selection, say ______ ____ _.", "apply heading 6", "1", "1"),
    ("To apply italicize to a selection, say ______.", "italicize", "1", "1"),
    ("To apply italics to a selection, say ______.", "italics", "1", "1"),
    ("To apply normal text, say ______ _____ ______.", "apply normal text", "1", "1"),
    ("To apply strikethrough to a selection, say ______.", "strikethrough", "1", "1"),
    ("To apply subtitle to a selection, say ______ _____.", "apply subtitle", "1", "1"),
    ("To apply the color blue to a selection, say ______ _____ ____.", "text color blue ", "1", "1"),
    ("To apply title to a selection, say ______ _____.", "apply title", "1", "1"),
    ("To center align a selection, say ____ ____.", "align center", "1", "1"),
    ("To clear the formatting of a selection, say ___ ____.", "clear formatting", "1", "1"),
    ("To copy a link, say ___ ___ .", "copy link", "1", "1"),
    ("To copy the selection, say ____.", "copy", "1", "1"),
    ("To create a bulleted list out of a selection, say ____ ____ _____", "create bulleted list", "1", "1"),
    ("To create a numbered list out of a selection, say ____ ____ _____", "create numbered list", "1", "1"),
    ("To cut the selection, say ____.", "cut", "1", "1"),
    ("To decrease indent of a paragraph, say ____ ____.", "decrease indent", "1", "1"),
    ("To decrease the font size of a selection, say ______ ____ ______.", "decrease font size", "1", "1"),
    ("To delete a column in a table, say ____ ___.", "delete column", "1", "1"),
    ("To delete a link, say ___ ___ .", "delete link", "1", "1"),
    ("To delete a row in a table, say ____ ___.", "delete row", "1", "1"),
    ("To delete a table of contents, say ___ ___ __ ____ __ .", "delete of table of contents", "1", "1"),
    ("To delete a table, say ____ ___.", "delete table", "1", "1"),
    ("To delete the last word, say ____ ____ _____.", "delete last word.", "1", "1"),
    ("To delete the selection, say ____.", "delete", "1", "1"),
    ("To delete the word 'book', say ____ ____ .", "delete book", "1", "1"),
    ("To exit table, say ____ ___.", "exit table", "1", "1"),
    ("To go to the end of the paragraph, say ____ ___ __ ___ __ ___ _______. ", "go to the end of the paragraph", "1", "1"),
    ("To go to the word 'books', say ___ ____ ___.", "go to books", "1", "1"),
    ("To have the computer speak the row and column headers of a table, say ____ ____ _____ _____ _____ _____.", "speak table row and column headers", "1", "1"),
    ("To have the computer speak from the cursor location, say ____ ____ _____ _____.", "speak from cursor location", "1", "1"),
    ("To have the computer speak speak table column header, say ____ ____ _____ _____.", "speak table column header", "1", "1"),
    ("To have the computer speak table cell location, say ____ ____ _____ _____.", "speak table cell location", "1", "1"),
    ("To have the computer speak table row header, say ____ ____ _____ _____.", "speak table row header", "1", "1"),
    ("To have the computer speak the cursor location, say ____ ____ _____.", "speak cursor location", "1", "1"),
    ("To have the computer speak the selection formatting, say ________ _______ ________.", "speak selection formatting", "1", "1"),
    ("To have the computer speak the selection, say ____ ____ .", "speak selection", "1", "1"),
    ("To highlight with blue a selection, say ______ _____.", "highlight blue", "1", "1"),
    ("To increase indent of a paragraph, say ____ ____.", "increase indent", "1", "1"),
    ("To increase the font size of a selection, say ______ ____ ______.", "increase font size", "1", "1"),
    ("To insert a bookmark, say _____ _____ .", "insert bookmark", "1", "1"),
    ("To insert a bullet in a bulleted list, say___ ____.", "insert bullet", "1", "1"),
    ("To insert a column in a table, say ____ ___.", "insert column", "1", "1"),
    ("To insert a comment, say _____ _____ .", "insert comment", "1", "1"),
    ("To insert a footer, say _____ _____ .", "insert footer", "1", "1"),
    ("To insert a footnote, say _____ _____ .", "insert footnote", "1", "1"),
    ("To insert a header, say _____ _____ .", "insert header", "1", "1"),
    ("To insert a horizontal line, say _____ _____ _____ .", "insert horizontal line", "1", "1"),
    ("To insert a link, say ___ ___ and then say the URL you want to use.", "insert link", "1", "1"),
    ("To insert a new column in a table, say ____ ___ ____.", "insert new column", "1", "1"),
    ("To insert a new column on the left in a table, say ____ ___ ____.", "insert new column on the left ", "1", "1"),
    ("To insert a new row above in a table, say ____ ___ ____ ____.", "insert new row above", "1", "1"),
    ("To insert a new row below in a table, say ____ ___ ____ ____.", "insert new row below", "1", "1"),
    ("To insert a new row in a table, say ____ ___ ____.", "insert new row", "1", "1"),
    ("To insert a number in a numbered list, say___ ____.", "insert number", "1", "1"),
    ("To insert a page break, say _____ _____ ______.", "insert page break", "1", "1"),
    ("To insert a row in a table, say ____ ___.", "insert row", "1", "1"),
    ("To insert a table of contents, say ___ ___ __ ____ .", "insert table of contents", "1", "1"),
    ("To insert a table with 5 rows by 5 columns, say ____ ___ __ ___ __ __ _____.", "insert table 5 rows by 5 columns", "1", "1"),
    ("To insert a table, say ____ _____.", "insert table", "1", "1"),
    ("To left align a selection, say ____ ____.", "align left", "1", "1"),
    ("To list commands list, say ____ ____ _____.", "voice commands list", "1", "1"),
    ("To move the cursor to the end of the line, say ____ ____ ____ ___ __ __.", "move to the end of the line", "1", "1"),
    ("To move the cursor to the end of the paragraph, say ____ ___ __ ___ __ ___ _______. ", "move to the end of the paragraph", "1", "1"),
    ("To open Voice Typing help, say ____ ____ _____.", "voice typing help", "1", "1"),
    ("To paste the clipboard, say ____.", "paste", "1", "1"),
    ("To remove a selected column in a table, say ____ ___.", "remove column", "1", "1"),
    ("To remove a selected row in a table, say ____ ___.", "remove row", "1", "1"),
    ("To remove the background color of a selection, say ______ ____ ______.", "remove background color", "1", "1"),
    ("To remove the bold formatting of a selection, say ___ ____.", "remove bold", "1", "1"),
    ("To remove the formatting of a selection, say ___ ____.", "remove formatting", "1", "1"),
    ("To remove the highlight of a selection, say ______ ____ .", "remove highlight", "1", "1"),
    ("To remove the italics formatting of a selection, say ___ ____.", "remove italics", "1", "1"),
    ("To remove the strikethrough formatting of a selection, say ___ ____.", "remove striketrough", "1", "1"),
    ("To remove the underline formatting of a selection, say ___ ____.", "remove underline", "1", "1"),
    ("To resume Voice Typing with the word with 'books', say ____ ___ ___.", "resume with books", "1", "1"),
    ("To resume Voice Typing, say _____.", "resume", "1", "1"),
    ("To right align a selection, say ____ ____.", "align right", "1", "1"),
    ("To set the font size of a selection in the range of 6 to 400, say ______ ____ ______ to set the font size to 12.", "font size 12", "1", "1"),
    ("To set the line spacing double, say ____ _____ ____.", "line spacing double", "1", "1"),
    ("To set the line spacing single, say ____ _____ ____.", "line spacing single", "1", "1"),
    ("To set the line spacing to 2, say ____ ___ ___.", "line spacing 2", "1", "1"),
    ("To stop Voice Typing, say ____ ______.", "stop listening", "1", "1"),
    ("To update a table of contents, say ___ ___ __ ____ .", "update table of contents", "1", "1"),
    ]

    shuffle(q_all)
    print('A quiz about all.')
    print('The quiz is designed to refresh the memory.')
    print('Spending ten minutes with this quiz after a hiatas from voice could \
save you hours via improved efficiency.')
    print('\n')
    print('The non-home keystrokes are abbreviated as follows: ')
    print('\n')
    print('    S for shift key')
    print('    ^ for control key')
    print('    - for minus')
    print('    A for alternate key')
    print('    cmd for command key')
    print('    ret for return or enter')
    print('    del for delete')
    print('    bksp for backspace')
    print('    single quotes for quotes. Escape double quotes.')  
    print('\n')
    print('This quiz has %d fill-in-the-blank or \
short-answer questions.'  % (len(q_all)) )
    print('Each question in the quiz is asked \
just once if it is answered correctly.')
    print('Incorrectly answered questions will \
be recycled until they are answered correctly.')
    print('The questions are randomly shuffled upon \
start-up of the script, so each quiz is a new adventure!')
    print('If you do not know the answer, \
enter "return", and it will be printed to the terminal.')
    print('\n')
    return q_all


def quiz_me(QUESTION_ANSWER_SOURCE):
    """
    This is the function
    that runs the quizzes.
    """
    t = TicToc()
    t.tic()
    numCorrect = 0
    wrong = []
    for question, correct_answer, explanation, source in QUESTION_ANSWER_SOURCE:
        # answer = input(question.encode('utf-8').decode('utf-8') + ' ')

        answer = input(question + ' ')
        if answer == correct_answer:
            print('    Correct! :) \n')
            numCorrect += 1
        else:
            print('      The answer is "' + correct_answer + '".')
            print('        Explanation: "' + explanation + '".')
            print('          Find more information in ' + source + '.\n')
            redo = (question, correct_answer, explanation, source)
            wrong.append(redo)
            # When five wrong answers have accumulated, the questions are
            # repeated they are answered correctly then the next question
            # in the main list is invoked.
            if len(wrong) == 5:
                print('The last five wrongly-answered questions will \
be repeated once before advancing to new questions.')
                for question2, correct_answer2, explanation2, source2 in wrong[:]:
                    answer2 = input(question2 + ' ')
                    if answer2 == correct_answer2:
                        print('    Correct! :) \n')
                        wrong.remove((question2,
                                      correct_answer2, explanation2, source2))
                        print('                        Number of wrongly \
                              answered questions: ' +
                              str(len(wrong)) + '\n')
                    else:
                        print('      The answer is "'+ correct_answer2 + '".')
                        print('        Explanation: "' + explanation + '".')
                        print('            Find more information in '
                              + source2 + '.')
                        redo2 = (question2,
                                 correct_answer2,
                                 explanation2, source2)
                        wrong.append(redo2)
                        print('            Number of wrongly \
                        answered questions: ' + str(len(wrong)) + '\n')
            
# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python

    print('End of quiz with %d questions.' % (len(QUESTION_ANSWER_SOURCE)))
    print('%d questions correct and %d wrong.' % (numCorrect,
                                                  len(QUESTION_ANSWER_SOURCE) -
                                                  numCorrect))
    t.toc()
    print('\n' + 'Time elapsed: ' + str(t.elapsed) + ' seconds.' + '\n' )
    if len(QUESTION_ANSWER_SOURCE) == numCorrect:
        print('Congratulations! You are ready to use voice control! :)')
    else:
        print('\n'
             + 'Please try until again until you get a perfect score three times in a row.' 
             + 'Try again with a spaced interval (two days is optimal). Repeat five times to improve your recall.'
             + 'You can use the alphabet in command mode to enter the letters by voice. Say "enter" in place of hitting "return".' 
             + 'This is a nice way to build "voice" memory of the alphabet. Cool, use your voice to take a quiz on voice control!'
             + 'You need have a terminal.talon configuration file in ~/.talon/user/<yourname>-talon/ with "tag: terminal" on the first line.'
             + '\n' 
             
             + '\n'
             + "Amateurs prepare until they can \
get it right. Professional prepare until they cannot \
get it wrong." 
             + '\n' 
             + '   -- Julie Andrews')
    print('\n')
    print('Literature Cited')
    print('\n')
    lambda cited: list(map(print, cited))
    return


def interactive_quiz():
    """This function runs the quiz interactives.""" 
    while True:
        print("\n")
        print("Select one quiz about VoiceTyping:" + "\n")
        
        print("1.  all")
        print("\n")
        while True:
            value = input("Enter integer between 1 and 1 :")
            try:
                SELECTEDQ = int(value)
            except ValueError:
                print("Enter an integer, please")
                continue
            if 1 <= SELECTEDQ <= 1:
                break
            else:
                print("Out of valid range. Please re-enter integer from this range: 1 - 1")
    
        if SELECTEDQ == 1:
            QUESTION_ANSWER_SOURCE = all_q()
            SUBQUIZ = "All"
            TOPIC = "VoiceTyping"
        quiz_me(QUESTION_ANSWER_SOURCE)
        reply = input('Enter text, [type \"stop\" to quit or hit the Enter (or Return key) to select another quiz]: ')
        print(reply.lower())
        if reply == 'stop':
            break
    return





if __name__== "__main__":
    interactive_quiz()