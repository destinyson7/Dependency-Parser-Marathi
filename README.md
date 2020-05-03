# Dependency-Parser-Marathi

**Requirements** - 

_Libraries_ -

sklearn, scipy, numpy, pickle

_Files_ -

(already there, ensure, the directory structure is maintained)

Training.txt, Testing.txt, words, pos_tags, and chunk_tags.


**Running the Parser** - 


1. select the model in the Data folder

2. cd into the model

3. To Train the model - python3 train.py ../../Training.txt (optionally, remove the SVM files before training)

4. After training completes, to test - python3 predict.py ../../Testing.txt


_Reading the output_ -

5. The values print in the first two arrays are predictions from SVM and Logistic Regression Models respectively. (depending on what is the model's output, it would either be the arc direction or the arc label )

6. The numeric values are accuracies of the SVM and Logistic Regression models respectively.


**Source of our Data** -

We processed about 15K data from the gold labeled dependency from https://ltrc.iiit.ac.in/downloads/kolhi/ 's Marathi dataset.


**Github Repository link**

https://github.com/destinyson7/Dependency-Parser-Marathi


**Work division**

Tanish (2018114005) - 

Mukund (2018114015) - 



ToDo


It will also contain a breakdown of which team member did which part of the project
