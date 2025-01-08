For this task we are working with a movie review dataset. In this dataset, the ratings, budgets, and other information on popular movies released in 2014 and 2015 were collected from social media websites such as YouTube, Twitter (now called X), IMDB, etc.

**What can we tell about the rating of a movie from its budget and aggregated number of  followers in social media channels?**

![image](https://github.com/user-attachments/assets/7f6f1c9b-a95d-4ede-8415-a8fe08655484)
![image](https://github.com/user-attachments/assets/0a928968-32d2-4fd6-8ef7-2b1e41d083bf)

Using the plot function in our program between the ratings and factors like the budget and aggregate followers, we can tell that there is not a very clear relation. There is definitely somewhat of a positive relation, but data is so scattered that it becomes hard to generalize the ratings variable based solely on budget and aggregate followers. As there are cases that follow a linear relationship, for instance, movies that have high ratings because of their high budget, but there is also a good number of movies that do not necessarily follow that rule, still having high ratings with a lower budget. It is the same case for the aggregate followers, not having much weight on the ratings variable.

**If we incorporate the type of interaction the movie has received (number of likes, dislikes, and comments) in social media channels, does it improve our prediction?**

![image](https://github.com/user-attachments/assets/e6d03574-b52a-47b0-bd0b-29cce9759ae9)
![image](https://github.com/user-attachments/assets/5346301b-e915-4cb8-a1a9-fb8e959c2a41)
![image](https://github.com/user-attachments/assets/f772de6d-20ae-4ff6-925f-677d64cfcd2c)

After plotting and normalizing the type of interaction the movie has received versus the overall rating, data still remains scattered and spread, showing no real relationship or not much weight in predicting the rating of the movie, as even still after normalization we can find data on two sides of the spectrum. For the likes feature, there’s only a few cases that follow a linear relation, showing both a high number of likes reflected in a high rating, however, most of the data is mixed, showing a few likes yet a high rating and viceversa, few likes and low ratings. The dislikes feature, shows again no real sign of a strong relation, as most data is toward the lower end, still we find movies with both high and low ratings. It’s the same case with the comments feature, where a high number of comments is not necessarily reflected in a high rating, in fact the data shows both a high and low rating, regardless of the comments. So overall, this additional features do not improve the prediction.

**-Among all the factors we considered in the last two models, which one is the best predictor of movie rating?**

Among all the factors considered we could argue that the budget feature is the best predictor for the movie rating, as even though the data remains scattered, there is a stronger relation compared to the other factors.

With the budget feature being the best predictor for movie ratings we will use gradient descent to find the optimal intercept (bias) and gradient (weight) for the dataset.
 


