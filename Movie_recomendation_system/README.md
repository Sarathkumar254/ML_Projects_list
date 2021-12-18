# Content-Based-Movie-Recommender-System-with-sentiment-analysis

Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie\

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and\ 
using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using beautifulsoup4 and performed sentiment \
analysis on those reviews.



# Project Overview
## Similarity Score :
How does it decide which item is most similar to the item user likes? Here we use the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/49829889/146650553-e74b4358-266c-4107-ab38-12f77fed11bb.png)


More about Cosine Similarity : https://www.machinelearningplus.com/nlp/cosine-similarity/

Sources of the datasets\
1.IMDB 5000 Movie Dataset: https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset \
2.Movies Dataset: https://www.kaggle.com/rounakbanik/the-movies-dataset \
3.List of movies 2018: https://en.wikipedia.org/wiki/List_of_American_films_of_2018 \
4.List of Movies 2019: https://en.wikipedia.org/wiki/List_of_American_films_of_2019 \
5.List of Movies 2020: https://en.wikipedia.org/wiki/List_of_American_films_of_2020




