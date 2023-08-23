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


    """
A class that implements an inverted index for text documents.
    """
class InvIndex:


     """
Initializes the inverted index by creating the index map.
docs: List of text documents.
        """
    def __init__(self,docs):
        self.inverted_index_map=self.index_words(docs)

"""
Creates an inverted index from a list of text documents.
        """
    def index_words(self, docs):
        inverted_index = defaultdict(set)

"""
        return: Inverted index as a defaultdict of sets.
"""

        
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

 """
Executes a query on the inverted index and returns matching documents.
    :return: List of document IDs matching the query.
"""
        
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
 """
Searches the inverted index for documents containing a word.
    :param word: Word to search for.
    :param matched_docs: Set of matched document IDs.
    :return: Updated set of matched document IDs.
"""
        matches = self.inverted_index_map.get(word)
        if matches:
            if (len(matched_docs) == 0):
                matched_docs = matched_docs.union(matches)
            else:
                matched_docs = matched_docs.intersection(matches)
        return matched_docs

    def process(self,word):

"""
Processes a word by converting to lowercase and lemmatizing if not a stopword.
    :return: Processed word.
"""
        word_lower = word.lower()
        if word_lower not in stwords:
            word_lemm = lemmatizer.lemmatize(word_lower)
            return word_lemm
        else: return
