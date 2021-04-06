# NLPContractions

A Python package to replace some english words with their shorter versions (contractions) in a sentence to help text augmentation in NLP tasks.

<br/>

## Installation

<br />

### Method - 1: Clone and Install

```
git clone https://github.com/vatsalsaglani/nlp-text-contractions.git
cd contractions
python setup.py install
```

### Method - 2: Pip install with github

```
pip install git+https://github.com/vatsalsaglani/nlp-text-contractions.git
```

<br />

## Usage Documentation
Currently, this package only supports text contractions, Here's how you can use it

<br />

```
from NLPContractions.contraction import text_contraction

texts = ['they are not allowed to modify the title', 'he is from the south']

text_contraction(texts)
>>>["they ain't allowed to modify the title",
   "they aren't allowed to modify the title",
   "they're not allowed to modify the title",
   "he's from the south"]


text = texts[0]
text_contraction(text)
>>>["they ain't allowed to modify the title",
   "they aren't allowed to modify the title",
   "they're not allowed to modify the title"]
```

The input to the function can either be of the type `str` or `list`. The `text_contration` function will output all the possible __contractions__ for the given sentence or list of sentences

<br />

To get the contractions related to sentence when provided with a list of input sentences set the `output_dict` argument in the `text_contraction` function as `True`. It will output a `defaultdict` of type `list` and you can query all the contractions of any particular sentence easily.

```
contracts = text_contraction(texts, output_dict = True)

## outputs a defaultdict of list.
contrats
>>>defaultdict(list,
            {'they are not allowed to modify the title': ["they ain't allowed to modify the title",
              "they aren't allowed to modify the title",
              "they're not allowed to modify the title"],
             'he is from the south': ["he's from the south"]})


## query all contractions for the first sentence
contracts[texts[0]]
>>>["they ain't allowed to modify the title",
   "they aren't allowed to modify the title",
   "they're not allowed to modify the title"]
```

