import nltk
import collections
import re
#nltk.download()
#nltk.download('wordnet')
# nltk.download('stopwords')
# nltk.download('punkt')

from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import snowball
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

global stwords
global lemmatizer

stwords = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


class InvIndex:

    def __init__(self,docs):
        self.inverted_index_map=self.index_words(docs)


    def index_words(self, docs):
        inverted_index = defaultdict(set)

        for docId, f in enumerate(docs):
            docId+=1
            f=self.remove_punctuation(f)
            for sent in sent_tokenize(f):
                for word in word_tokenize(sent):
                    word_lower = word.lower()
                    if word_lower not in stwords:
                        word_lemm= lemmatizer.lemmatize(word_lower)
                        inverted_index[word_lemm].add(docId)
        return inverted_index

    def remove_punctuation(self, file):
        return (re.sub(r'[^\w\s]', "", file))

    def run_query(self,query):
        #processing:
        matched_document_nums=set()
        for word in word_tokenize(query):
            processed_word=self.process(word)
            matched_document_nums=self.search(processed_word, matched_document_nums)

        matched_docs=[]
        for num in matched_document_nums:
             matched_docs.append('d'+str(num))
        return matched_docs


    def search(self,word, matched_docs):
        matches = self.inverted_index_map.get(word)
        if matches:
            if (len(matched_docs) == 0):
                matched_docs = matched_docs.union(matches)
            else:
                matched_docs = matched_docs.intersection(matches)
        return matched_docs

    def process(self,word):
        word_lower = word.lower()
        if word_lower not in stwords:
            word_lemm = lemmatizer.lemmatize(word_lower)
            return word_lemm
        else: return
