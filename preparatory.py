# Preparatory quizzes dictionary

prep_dict = {'A thirty-second note triplet is equal in duration to a:': ['Quarter note', 'Half note', 'Eighth note', 'Sixteenth note'],
             'How many 8th notes does a dotted half note have;': [3, 6, 5, 4],
             'The Sol-La interval is equal to a;': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Do#-Re interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Fa-Sol# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Re-Mi# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Si#-Do interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The order of flats is:': ['Fa La Do Mi', 'Mi Sol Si Re Fa', 'Fa Do Sol Re La Mi Si', 'Si Mi La Re Sol Do Fa'],
             'How many semitones are from La to Do#?': [3, 5, 2, 4],
             'A sixteenth note triplet is equal in duration to a:': ['Quarter note', 'Half note', 'Eighth note', 'Sixteenth note'],
             'The Re-Re# interval is equal to a;': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Do-Re# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Mi#-Fa interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'How many 8th notes does a dotted quarter note have;': [3, 7, 5, 2],
             'How many 16th notes does a dotted quarter note have;': [6, 3, 5, 4],
             'How many 16th notes does a quarter note have;': [3, 4, 5, 8],
             'How many 16th notes does a half note have;': [4, 6, 8, 16],
             'The Si-Do# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Si-Do interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Mi-Fa♭ interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'How many semitones are from Fa to Si?': [5, 6, 4, 3],
             'An eighth note triplet is equal in duration to a:': ['Quarter note', 'Half note', 'Eighth note', 'Sixteenth note'],
             'The La#-Si♭ interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'A quarter note triplet is equal in duration to a:': ['Quarter note', 'Half note', 'Eighth note', 'Sixteenth note'],
             'How many 64th notes does a whole note have;': [8, 64, 32, 16],
             'The order of sharps is:': ['Fa La Do Mi', 'Mi Sol Si Re Fa', 'Fa Do Sol Re La Mi Si', 'Si Mi La Re Sol Do Fa'],
             'How many semitones are from Do to Fa?': [5, 6, 4, 3],
             'How many semitones are from Re# to Fa#?': [2, 4, 3, 5],
             'The Sol-La# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'The Mi-Fa interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
             'How many semitones are from Do to the next Do?': [13, 14, 11, 12],
             'How many semitones are from Fa to Do#?': [6, 5, 8, 9],
             }

first_dict = {'How many 16th notes does a dotted quarter note have;': [6, 3, 5, 4],
              'The Do-Re interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The Sol-La interval is equal to a;': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The Sol-La# interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The Re-Re# interval is equal to a;': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The Si-Do interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The Mi#-Fa interval is equal to a:': ['Tone', 'Semitone', 'Tri-semitone', 'Enharmonic equivalent'],
              'The key signature of the Do# major scale is:':['Nothing', 'Fa Do Sol', 'Fa Do', 'Fa Do Sol Re La Mi Si']
              }             

import pandas as pd
import random
import time

prep = pd.read_csv('preparatory.csv')

result = 0

for i in range(3):

    question, answer = random.choice(list(prep_dict.items()))

    the_answer = prep.Answer[prep.Question == question].iloc[0]

    print(f"{i+1}. {question}\n   a. {answer[0]}\n   b. {answer[1]}\n   c. {answer[2]}\n   d. {answer[3]}\n")

    guess = input('Your answer is: ')

    time.sleep(2)

    if guess == the_answer:
        print('\nWell done!\n')
        result += 1
    else:
        print('\nIncorrect answer!\n')    

    time.sleep(4) 

print('-'*40)    
print(f'You answered correctly {result} out of {i+1} questions.')