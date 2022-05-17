# Korean_auto-glossing
Let computer gloss Korean examples for you!

It provides:
 * Leipzig-like interlinear glossing with
   * perfect Yale romanization
   * not-bad morphological analysis
   * google translation for the sentence
 
While I worked on a syntax qualifying paper, glossing all Korean examples was a boring task. Interlinear glosses should be consistent (and boring to do). Being consistent in a boring task is something computers do much better than human. So why not make it do the job for you?

It uses Kkma (part of konlpy.tag subpackage) for morphological analysis, googletrans for translationand hangul_to_jamo (part of the kPNNpy subpackage) for transliteration (the Yale romanization of Korean).

## Usage
run main.py with a Korean sentence. For example,

```bash
python3 main.py 아버지께서 방에 들어가신다.
```

throws back

```bash
input:   아버지께서 방에 들어가신다.
Yale:    Apeci-kkeyse           pang-ey         tuleka-si-nta.
gloss:   father-NOM.HON         room-ADVZ       enter-HON-DECL
translation:     'Father enters the room.'
```
