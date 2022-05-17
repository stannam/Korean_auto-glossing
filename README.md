# Korean_auto-glossing
Let computer gloss Korean examples for you!

It provides:
 * [Leipzig-like interlinear glossing](https://www.eva.mpg.de/lingua/resources/glossing-rules.php) with
   * perfect Yale romanization
   * not-bad morphological analysis
   * google translation for the sentence
 
While I worked on a syntax qualifying paper, glossing all Korean examples was a tedious task. Interlinear glosses should be consistent, and being consistent is what computers excel at (especially when the task is boring). So why not make it do the job for you?

It uses Kkma (part of [konlpy.tag subpackage](https://konlpy.org/en/latest/api/konlpy.tag/#module-konlpy.tag._kkma)) for morphological analysis, [googletrans](https://github.com/ssut/py-googletrans) for translation, and hangul_to_jamo (part of the [kPNNpy subpackage](https://github.com/stannam/KPNN)) for the Yale romanization of Korean.

## Usage
run main.py with a Korean sentence. For example,

```bash
python3 main.py 아버지께서 방에 들어가신다.
```

... and the terminal returns.

```bash
input:   아버지께서 방에 들어가신다.
Yale:    Apeci-kkeyse           pang-ey         tuleka-si-nta.
gloss:   father-NOM.HON         room-ADVZ       enter-HON-DECL
translation:     'Father enters the room.'
```
