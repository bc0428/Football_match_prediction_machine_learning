# Football_match_prediction_machine_learning
Using machine learning algorithms to predict football match result and total goals soley based on betting odds
</br></br></br>

<h2> Background </h2>
This project aims at investigating the potential of using betting odds as a predictive factor in football matches. Dataset of English Premier League from 2016 to Feb 2022 was obtained from (https://www.football-data.co.uk/data.php/) and being used for training, validation and testing.

</br><h2> Data Cleaning </h2>
The 6-yaers-worth of data was first cleaned using mySQL. Selected features of each matches are: odds for home, away to win, draw, over and under 2.5 goals; home win index (odds of away win/home win), over 2.5 goals index (odds of under 2.5 goals/over 2.5 goals), goal difference, shots on target difference and total goals.

</br><h3> Football match result prediction </h3>
Classification algorithms from python package--scikitlearn were used to classify the match result into 'H', 'A' or 'D' which are home win, away win or draw respectively. Results were compared and evaluated by the confusion matrix, accuracy of algorithms used are as follows:</br>
| K-nearest neighbors | Logistic Regression | Random Forest | Multi-layer Perceptron | 
| ------------------- | ------------------- | ------------- | ---------------------- |
| 0.53 | 0.575 | 0.477 | 0.577 |</br></br>

</br><h3> Total goals in a match prediction </h3>
Regression algorithms also from scikitlearn were used to predict total goals in a match. Results were evaluated using mean squared error:</br>

| Polynomial Regression | Support Vector | 
| --------------------- | -------------- | 
| 2.73                  | 2.83            | </br></br>
