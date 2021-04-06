import re
from collections import defaultdict

expansionDict = {
    re.compile('alright', re.I | re.U): "a'ight",
    re.compile('am not|is not|has not|are not|have not|did not', re.I | re.U): "ain't",
    re.compile('am not', re.I | re.U): "amn't",
    re.compile('are not', re.I | re.U): "aren't",
    re.compile('because', re.I | re.U): "'cause",
    re.compile('could have', re.I | re.U): "could've",
    re.compile('could not have', re.I | re.U): "couldn't've",
    re.compile('could not', re.I | re.U): "couldn't",
    re.compile('dare not|dared not', re.I | re.U): "daren't", 
    re.compile('dare not', re.I | re.U): "daresn't",
    re.compile('did not', re.I | re.U): "didn't",
    re.compile('does not', re.I | re.U): "doesn't",
    re.compile('do not|does not', re.I | re.U): "don't",
    re.compile("don't know|do not know", re.I | re.U): "dunno",
    re.compile('do you | did you', re.I | re.U): "d'ye",
    re.compile('ever', re.I | re.U): "e'er",
    re.compile('them', re.I | re.U): "'em",
    re.compile('everybody is', re.I | re.U): "everybody's",
    re.compile('everyone is', re.I | re.U): "everyone's",
    re.compile('good day', re.I | re.U): "g'day",
    re.compile('give me', re.I | re.U): 'gimme',
    re.compile('given', re.I | re.U): "giv'n",
    re.compile('going to', re.I | re.U): "gonna",
    re.compile('go not', re.I | re.U): "gon't", # colloquial
    re.compile('got to', re.I | re.U): "gotta",
    re.compile('had not', re.I | re.U): "hadn't",
    re.compile('had have', re.I | re.U): "had've",
    re.compile('has not', re.I | re.U): "hasn't",
    re.compile('have not', re.I | re.U): "haven't",
    re.compile('he had|he would', re.I | re.U): "he'd",
    re.compile('he has|he is', re.I | re.U): "he's",
    re.compile('he shall|he will', re.I | re.U): "he'll",
    re.compile('here is', re.I | re.U): "here's",
    re.compile('he have', re.I | re.U): "he've",
    re.compile('how did|how would', re.I | re.U): "how'd",
    re.compile('how do you do|how od you fare', re.I | re.U): "howdy",
    re.compile('how will', re.I | re.U): "how'll",
    re.compile('how are', re.I | re.U): "how're",
    re.compile('how has|how is|how does', re.I | re.U): "how's",
    re.compile('I had|I would', re.I | re.U): "I'd",
    re.compile('I would have', re.I | re.U): "I'd've",
    re.compile('I shall|I will', re.I | re.U): "I'll",
    re.compile('I am', re.I | re.U): "I'm",
    re.compile('I am about to', re.I | re.U): "I'm'a",
    re.compile('I am going to', re.I | re.U): "I'm'o",
    re.compile('is it not', re.I | re.U): "innit",
    re.compile('I have', re.I | re.U): "I've",
    re.compile('is not', re.I | re.U): "isn't",
    re.compile('it would', re.I | re.U): "it'd",
    re.compile('it shall|it will', re.I | re.U): "it'll",
    re.compile('it has|it is', re.I | re.U): "it's",
    re.compile("I don't know", re.I | re.U): "iunno",
    re.compile("kind of", re.I | re.U): "kinda",
    re.compile("let us", re.I | re.U): "let's",
    re.compile("madam", re.I | re.U): "ma'am",
    re.compile("may not", re.I | re.U): "mayn't",
    re.compile("may have", re.I | re.U): "may've",
    re.compile("me thinks", re.I | re.U): "methinks",
    re.compile('might not', re.I | re.U): "mightn't",
    re.compile('might have', re.I | re.U): "might've",
    re.compile("must not", re.I | re.U): "mustn't",
    re.compile("must not have", re.I | re.U): "mustn't've",
    re.compile("must have", re.I | re.U): "must've",
    re.compile("need not", re.I | re.U): "needn't",
    re.compile("and all", re.I | re.U): "nal",
    re.compile("never", re.I | re.U): "ne'er",
    re.compile("of the clock", re.I | re.U): "o'clock",
    re.compile("over", re.I | re.U): "o'er",
    re.compile("old", re.I | re.U): "ol'",
    re.compile("ought not", re.I | re.U): "oughtn't",
    re.compile("shall not", re.I | re.U): "shalln't",
    re.compile("she had|she would", re.I | re.U): "she'd",
    re.compile("she shall|she will", re.I | re.U): "she'll",
    re.compile("she has|she is", re.I | re.U): "she's",
    re.compile("should have", re.I | re.U): "should've",
    re.compile("should not", re.I | re.U): "shouldn't",
    re.compile("should not have", re.I | re.U): "shouldn't've",
    re.compile("somebody has|somebody is", re.I | re.U): "somebody's",
    re.compile("someone has|someone is", re.I | re.U): "someone's",
    re.compile("something has|something is", re.I | re.U): "something's",
    re.compile("so are", re.I | re.U): "so're", # colloquial
    re.compile("that will|that shall", re.I | re.U): "that'll",
    re.compile("that has|that is", re.I | re.U): "that's",
    re.compile("that would|that had", re.I | re.U): "that'd",
    re.compile("there had|there would", re.I | re.U): "there'd",
    re.compile("there shall|there will", re.I | re.U): "there'll",
    re.compile("there are", re.I | re.U): "there're",
    re.compile("there has|there is", re.I | re.U): "there's",
    re.compile("these are", re.I | re.U): "these're",
    re.compile("these have", re.I | re.U): "these've",
    re.compile("they had|they would", re.I | re.U): "they'd",
    re.compile("they shall|they will", re.I | re.U): "they'll",
    re.compile("they are|they were", re.I | re.U): "they're",
    re.compile("they have", re.I | re.U): "they've",
    re.compile("this has|this is", re.I | re.U): "this's",
    re.compile("those are", re.I | re.U): "those're",
    re.compile("those have", re.I | re.U): "those've", 
    re.compile("it is", re.I | re.U): "'tis",
    re.compile("to have", re.I | re.U): "to've",
    re.compile("it was", re.I | re.U): "'twas",
    re.compile("want to", re.I | re.U): "wanna",
    re.compile("was not", re.I | re.U): "wasn't",
    re.compile("we had|we would|we did", re.I | re.U): "we'd",
    re.compile("we would have", re.I | re.U): "we'd've",
    re.compile("we shall|we will", re.I | re.U): "we'll",
    re.compile("we are", re.I | re.U): "we're",
    re.compile("we have", re.I | re.U): "we've",
    re.compile("were not", re.I | re.U): "weren't",
    re.compile("what did", re.I | re.U): "what'd",
    re.compile("what shall|what will", re.I | re.U): "what'll",
    re.compile("what are|what were", re.I | re.U): "what're",
    re.compile("what has|what is|what does", re.I | re.U): "what's",
    re.compile("what have", re.I | re.U): "what've",
    re.compile("when has|when it", re.I | re.U): "when's",
    re.compile("when will", re.I | re.U): "when'll",
    re.compile("where did", re.I | re.U): "where'd",
    re.compile("where shall|where will", re.I | re.U): "where'll",
    re.compile("where are", re.I | re.U): "where're",
    re.compile("where has|where is|where does", re.I | re.U): "where's",
    re.compile("where have", re.I | re.U): "where've",
    re.compile("which had", re.I | re.U): "which'd",
    re.compile("which would", re.I | re.U): "which'd",
    re.compile("which shall|which will", re.I | re.U): "which'll",
    re.compile("which are", re.I | re.U): "which're",
    re.compile("which have", re.I | re.U): "which've",
    re.compile("who would|who had|who did", re.I | re.U): "who'd",
    re.compile("who would have", re.I | re.U): "who'd've",
    re.compile("who shall|who will", re.I | re.U): "who'll",
    re.compile("who are", re.I | re.U): "who're",
    re.compile("who has|who is|who does", re.I | re.U): "who's",
    re.compile("who have", re.I | re.U): "who've",
    re.compile("why did", re.I | re.U): "why'd",
    re.compile("why are", re.I | re.U): "why're",
    re.compile("why has|why is|why does", re.I | re.U): "why's",
    re.compile("will not", re.I | re.U): "willn't",
    re.compile("will not", re.I | re.U): "won't",
    re.compile("will not", re.I | re.U): "wonnot",
    re.compile("would have", re.I | re.U): "would've",
    re.compile("would not", re.I | re.U): "wouldn't",
    re.compile("would not have", re.I | re.U): "wouldn't've",
    re.compile("you all", re.I | re.U): "y'all",
    re.compile("you all would have", re.I | re.U): "y'all'd've",
    re.compile("you all would not have", re.I | re.U): "y'all'd'n've",
    re.compile("you all are", re.I | re.U): "y'all're",
    re.compile("you had|you would", re.I | re.U): "you'd",
    re.compile("you shall|you will", re.I | re.U): "you'll",
    re.compile("you are", re.I | re.U): "you're",
    re.compile("you have", re.I | re.U): "you've"
}


def text_contraction(texts: [str, list], language_code = 'en', output_dict = False):
    '''
    Return a list of contracted texts
    '''

    flatten = lambda lst: [item for sublist in lst for item in sublist]


    if not language_code == 'en':
        return "Supports only the English Lanugage currently"
    
    if isinstance(texts, str):
        
        texts = [texts]

    contracted_texts = defaultdict(list)

    for text in texts:

        for regex, contraction in expansionDict.items():

            op = regex.sub(contraction, text)

            if op != text:
                contracted_texts[text].append(op)


    if not output_dict:
        
        return flatten(list(contracted_texts.values()))

    return contracted_texts
