import os
from flask import Flask, render_template, request, redirect, url_for
from random import choice
import worker

app = Flask(__name__)


@app.route('/',  methods=["GET", "POST"])
def main():
    # Upon launching, choose a placeholder sentence to appear. List 'sentences' holds example Korean sentences.
    sentences = ['고양이는 예쁘다.',    # Cats are pretty.
                 '다람쥐는 점프한다.',  # The squirrel jumps.
                 '아버지가 가방에 들어가신다.',   # Father enters the room.
                 '통사론 재미없어.',    # Syntax is no fun.
                 '음운론이 최고야',     # Phonology is the best.
                 '집에 올 시간이 지났다.',   # They should have arrived home already.
                 '언어학은 재밌어.'     # Linguistics is fun.
                 ]
    sentence = ''

    # and process the sentence.
    # this gives a default yale romanization, by-word glosses, and a whole-sentence translation
    results = worker.main(sentence)
    sentence = sentence
    yale = '\t\t'.join(results[1])
    gloss = '\t\t'.join(results[2])
    translation = results[3]

    try:
        if request.method == "POST":
            sentence = request.form['sentence']
            results = worker.main(sentence)
            sentence = sentence
            yale = '\t\t'.join(results[1])
            gloss = '\t\t'.join(results[2])
            translation = results[3]
        return render_template('main.html',
                               sentence=sentence,
                               yale=yale,
                               gloss=gloss,
                               translation=translation)
    except Exception as e:
        return render_template('main.html',
                               sentence=str(e),
                               yale='',
                               gloss='',
                               translation='')

