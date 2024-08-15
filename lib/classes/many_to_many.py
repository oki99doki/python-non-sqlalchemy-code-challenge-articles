class Article:
    # Create all to collect all articles
    all = []

    def __init__(self, author, magazine, title):
        # initialize Article property (title)
        self.title = title

        # initialize class instances (Author, Magazine)
        self.author = author
        self.magazine = magazine
        
        # count all articles
        Article.all.append(self)

    # Article property returns article's title
    @property
    def title(self):
        return self._title
    
    # Setter checks that title are of type str and have 5-50 chars
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        
class Author:
    def __init__(self, name):
        # initialize Author property (name)
        self.name = name

    # Author property returns author's name
    @property
    def name(self):
        return self._name
    
    # Setter checks that name is of type str, has more than 0 chars and is immutable
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and 0 < len(name):
                self._name = name
    
    # Returns a list of all articles the author has written. Must be of type Article.
    def articles(self):
        # Create empty list
        self_articles = []
        # Iterate over all articles, and for each check if author matchtes, and if it does
        # then add article to list.
        for cur_article in Article.all:
            if (cur_article.author == self ):
                self_articles.append(cur_article)
        # Return list of all articles of specific author
        return self_articles

    # Returns a list of all the articles the magazine has published. Must be of type Article
    def magazines(self):
        this_authors_magazines = []
        for mag in Magazine.all:
            if(mag.name == self):
                this_authors_magazines.append(mag)
        return this_authors_magazines

    # Add new article given a Magaznie instance and title as arguments
    def add_article(self, magazine, title):
        # create new article
        new_Article = Article(self, magazine, title)
        return new_Article

    # Returns unique list of strings with categories of magazines the author has contributed to,
    # returns None if author has no articles.
    def topic_areas(self):
        article_list = self.articles()
        if len(article_list) == 0:
            return None
        # Create empty list for topic_area
        topic_areas = []
        # For each article in list of articles, check if it is not already in list.
        # If it is not in list, then add it to list of article categories.
        for article in article_list:
            if article.category not in topic_areas:
                topic_areas.append(article.category)
        return topic_areas

class Magazine:
    def __init__(self, name, category):
        # initialize MAgazine properties (name, category)
        self.name = name
        self.category = category

    # Property returns magazine's name
    @property
    def name(self):
        return self._name
    
    # Setter checks that name is of type str and has 2-16 chars
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    # Property returns magazine's category
    @property
    def category(self):
        return self._category
    
    # Setter checks that category is of type str and has more than 0 chars
    @category.setter
    def category(self, category):
        if isinstance(category, str) and 0 < len(category):
            self._category = category

    # Create relationship between instances of Author and Magazine classes
    def articles(self):
        self_articles = []
        for cur_article in Article.all:
            if (cur_article.magazine == self ):
                self_articles.append(cur_article)
        return self_articles

    # Create relationship between instances of Author and Magazine classes
    def contributors(self):
        conts = []
        for mag in self.magazines():
            conts.append(mag.name)

    # Goals:
    # Returns a list of the titles strings of all articles written for that magazine
    # Returns None if the magazine has no articles
    def article_titles(self):
        pass
        #return [article for article in self.articles if isinstance(article, Article) and article.magazine == self]

    def contributing_authors(self):
        pass
        # did not complete
        # Pseudo code: create empty list to store unique authors
        '''unique_authors = []'''
        # Pseudo code: for all authors of magazine, check if author is not already in unique author list
        # If it is not in list, then append it to list. Finally return list of unique authors.
        '''for author in self.authors:
            if author not in unique_authors:
                unique_authors.append(author)
        return unique_authors
        '''