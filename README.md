# Data Science - Movie project

## Main Purpose
We have had movies for over 60 years, but is there a connection between the success of the film and its cast features? This is the question we will explore in this project.
## Research Question
Is it possible to predict whether a film will succeed according to the movie cast features?

## Acquisition
* Crawling from wikipedia
* Crawling from idbm

### Using with libraries:
* BS4 - beautiful soup
* Selenium
* Pandas
* Requests
* matplotlib
* seaborn
* sklearn

## Data Cleaning

* Concatenation of all the information into one table
* Clean mismatch between IMDB and Wikipedia
* Handling NULL Values 
* Handling length of movie format
* Split columns 


## Visualisation

**Right Graph** -  Movie length distribution – as we can seemost length of movies is between 80 to 120

**Left Graph** - Movie rating distribution – as we can see most rating of movies is average  

![image](https://user-images.githubusercontent.com/68842383/150825527-0ba5bbd8-c687-4bfe-94ba-f9e85e2986e5.png)



Top 10 frequent genres – most of movies is belongto Comedy, Action, Drama 

![image](https://user-images.githubusercontent.com/68842383/150825827-1a19b8a9-8b64-49e7-8191-6ca4e219d34e.png)


As we can see, there is no correlation between length of movie and rating

![image](https://user-images.githubusercontent.com/68842383/150825901-737da9b7-8af5-48a9-88fd-808d3b3b033f.png)


Women's movies are generally rated average, unlike men which are rated On the whole scale of values

![image](https://user-images.githubusercontent.com/68842383/150825975-14f3f0af-79e5-456b-b8a8-8a1e6a4d0be0.png)


## Machine Learning

Using the `sklearn` library and linear regression we were able
to train a model that predicts the rating of movies based 
on crew features. We add some columns based on our data,
that described the quality of director, writer, starts and genre.

According to the success rates of the prediction,
 it is possible to see and even predict whether a film
 will succeed according to the quality of the cast.
 
 
![image](https://user-images.githubusercontent.com/68842383/150826352-ea1cd044-6cc2-4dce-a84d-0a0cb9d24e5e.png)

## Conclusions

The closer the prediction value is to 1, the more accurate the prediction. We have reached a predict value of 0.874, which is very close and therefore confirms the research question.

Therefore there is a connection between the film crew and the rating!

