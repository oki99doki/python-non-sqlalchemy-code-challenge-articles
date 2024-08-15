#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    '''
    class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    '''

    # Create instances of Article class
    article1 = Article("John Doe", "Tech Magazine", "Introduction to Python")
    article2 = Article("Jane Smith", "Science Journal", "The Future of Artificial Intelligence")
    article3 = Article("David Johnson", "Sports Weekly", "How to Improve Your Golf Swing")



    # don't remove this line, it's for debugging!
    ipdb.set_trace()
