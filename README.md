# Korean_auto-glossing
Let computer gloss Korean examples for me!

 * Leipzig-like interlinear glossing with
   * perfect Yale romanization
   * not-bad morphological analysis
   * google translation for the sentence
 
I was lazy and clumsy enough to need help glossing Korean sentences while I worked on a syntax qualifying paper. Interlinear glosses in syntax should be consistent and being consistent is something computers do best. So why not make it do the job for you?

It use Kkma (part of konlpy.tag subpackage) for morphological analysis, googletrans for translationand hangul_to_jamo (part of the kPNNpy subpackage) for transliteration (the Yale romanization of Korean).

