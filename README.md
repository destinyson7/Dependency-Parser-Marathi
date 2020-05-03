# Dependency-Parser-Marathi

**Requirements** - 

_Libraries_ -

sklearn, scipy, numpy, pickle

_Files_ -

Please ensure that the directory structure is maintained.

**Preprocessing the Data**

For Models 1 to 12

1. cd into the codes directory
2. Get the training data and combine all the files into 1 file named combined.txt
3. Cleaning the Data
```python
    python3 clean.py combined.txt   
    python3 more_clean.py cleaned.txt
```
4. Removing the sentences from the corpus which are chunked wrongly.
```python
    python3 remove_wrongly_chunked_sentences.py more_cleaned.txt head_mapping.json   
```
5. Numbering the sentences
```python
    python3 number_sentences.py correct_sentences.txt   
``` 
6. Extracting Heads of Each Chunk
```python
    python3 head_finding.py numbered.txt   
``` 
7. Extracting Dependency Relations between the heads
```python
    python3 dependencies_finding.py head_sentences.txt
``` 
8. Applying Arc Eager Algorithm to remove the sentences which cannot be parsed. The non-parsable sentences will be the ones which have projectivity issues.
```python
   python3 arc_eager.py dependency_sentences.txt
``` 
9.  Extracting Some Pairs of Chunks that are unrelated.
```python
    python3 get_unrelated_dependencies.py parsable_dependency_sentences.txt
``` 

For Models 13 to 17
1. cd into the Morphological Features directory
2. Follow steps 2 to 9 above

After preprocessing the corpus size falls down to 7.5K from 13K in the training data! The other 5.5K sentences either had insufficient data, or were wrongly chunked, or were non parsable due to projectivity issues.

**Pre-Training the Data**

1. Rename the final file named parsable_dependency_sentences_with_unrelated_pairs.txt to Training.txt
2. Preprocess the Testing and Development Data too and rename them to Testing.txt and Development.txt

For Models 1 to 12

3. cd into the Data folder
4. Move all the three files Training.txt, Development.txt and Testing.txt into the Data folder.
5. Run four python codes:
   
   1.  
    ```python
        python3 get_distinct_chunk_tags.py Training.txt Development.txt Testing.txt
    ```
   2. 
    ```python
        python3 get_distinct_pos_tags.py Training.txt Development.txt Testing.txt
    ```
   3. 
    ```python
        python3 get_distinct_words_tags.py Training.txt Development.txt Testing.txt
    ```
   4.  
    ```python
        python3 get_distinct_morph_vectors.py Training.txt Development.txt Testing.txt
    ``` 
6. Append the data from Development.txt into the Training.txt file

For Models 13 to 17

3. Move all the files Training.txt, Development.txt and Testing.txt into the Morphological Features directory
4. cd into the "Data/For Model 13 to 15" directory
5. Run four python codes:
   
   1.  
    ```python
        python3 get_distinct_chunk_tags.py ../../Morphological Features/Training.txt ../../Morphological Features/Development.txt ../../Morphological Features/Testing.txt
    ```
   2. 
    ```python
        python3 get_distinct_pos_tags.py ../../Morphological Features/Training.txt ../../Morphological Features/Development.txt ../../Morphological Features/Testing.txt
    ```
   3. 
    ```python
        python3 get_distinct_words_tags.py ../../Morphological Features/Training.txt ../../Morphological Features/Development.txt ../../Morphological Features/Testing.txt
    ```
   4.  
    ```python
        python3 get_distinct_morph_vectors.py ../../Morphological Features/Training.txt ../../Morphological Features/Development.txt ../../Morphological Features/Testing.txt
    ``` 

    These four files will extract all the distinct POS Tags, Word Tags, Words and Morphological Features' Vectors and store them into files in the same folder

5. Append the data from Development.txt into the Training.txt file
    
     
**Running the Models** - 

1. cd into the Data/Models directory
2. cd into any model number

For Models 1 to 12

3. Train the Model by running 
    ```python
        python3 train.py ../../Training.txt
    ``` 
4. Test the Model by running
    ```python
        python3 predict.py ../../Testing.txt
    ``` 

For Models 13 to 17

3. Train the Model by running 
    ```python
        python3 train.py ../../../Morphological Features/Training.txt
    ``` 
4. Test the Model by running
    ```python
        python3 predict.py ../../../Morphological Features/Testing.txt
    ``` 

_Reading the output_ -

5. The values printed in the first two arrays are predictions from SVM and Logistic Regression Models respectively. (depending on what is the model's output (what we are predicting - the L/R/U relationship or the dependency relation), it would either be the arc direction or the arc label)

6. The numeric values are accuracies of the SVM and Logistic Regression models respectively.


**Source of our Data** -

We processed about 15K data from the gold labeled dependency from https://ltrc.iiit.ac.in/downloads/kolhi/ 's Marathi dataset.


**Github Repository Link**

[Click](https://github.com/destinyson7/Dependency-Parser-Marathi)


**Work Division**

The work was done in such a way that each member contributed to each of the tasks.

Tanish (2018114005) - Mostly Coding Part

Mukund (2018114015) - Mostly Theoretical Part

We both feel that we have contributed equally on this project.

**Under the Guidance of**

Manish Shrivastava, Assistant Professor, IIIT Hyderabad
Pruthwik Mishra, PhD Student, IIIT Hyderabad
Alok Debnath, Introduction to NLP Course TA, IIIT Hyderabad