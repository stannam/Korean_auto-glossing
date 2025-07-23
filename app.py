from flask import Flask, render_template, request
from random import choice
import worker

# this is to always align the transliteration and gloss
def align_results(results:list):
    output_yale = ''
    output_gloss = ''
    for yale, gloss in zip(results[1], results[2]):
        len_yale, len_gloss = len(yale), len(gloss)
        len_diff = len_yale - len_gloss
        output_yale += f"{yale}    "
        output_gloss += f"{gloss}    "
        if len_diff > 0:
            output_gloss += " " * len_diff
        else:
            output_yale += " " * -len_diff
    return output_yale, output_gloss
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
    sentence = choice(sentences)

    # and process the sentence.
    # this gives a default yale romanization, by-word glosses, and a whole-sentence translation
    results = worker.main(sentence)
    sentence = sentence
    yale, gloss = align_results(results)
    translation = results[3]

    try:
        if request.method == "POST":
            sentence = request.form['sentence']
            results = worker.main(sentence)
            sentence = sentence
            yale, gloss = align_results(results)
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
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
