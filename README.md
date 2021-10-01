# Analysis of Ernest Hemingway Books
---
## The following books were included in the study:
#### ACROSS THE RIVER AND INTO THE TREES
#### GREEN HILLS OF AFRICA
#### MEN WITHOUT WOMEN
#### THE OLD MAN AND THE SEA
#### THE SUN ALSO RISES

---

## The analysis consists of the following steps:

1. The so-called "stop words" were excluded from the text. (*Stopwords are the English words which does not add much meaning to a sentence*)
2. A dictionary of words was created for each book, indicating the word and the number of its occurrences in the book.
3. Here are one example of plot with most frequent words in the book "MEN WITHOUT WOMEN":
![MEN WITHOUT WOMEN](https://github.com/HarTigran/Project-6-Small-Data-Engineering-NLP-and-AI-APIs-with-No-Code-Low-Code-/blob/main/Pics/WWM.png)

4. Entity analysis was done on all books to determine the location and faces in the book (Boto3 accuracy score above 06).
5. At this stage, the analysis result suggest that, Ernest Hemingway in these 5 books used about 150 places and 150 persons.
6. The list of locations was scanned through the wiki API with a check condition in the summary of the provided location - country, state, or city.
7. These are the result: 

---
**15 Countries**

![Country](https://github.com/HarTigran/Project-6-Small-Data-Engineering-NLP-and-AI-APIs-with-No-Code-Low-Code-/blob/main/Pics/Countries.png)

---
**13 States**

![State](https://github.com/HarTigran/Project-6-Small-Data-Engineering-NLP-and-AI-APIs-with-No-Code-Low-Code-/blob/main/Pics/States.png)

--- 
**22 Cities** (AWS identified cities only in the USA)

![Cities](https://github.com/HarTigran/Project-6-Small-Data-Engineering-NLP-and-AI-APIs-with-No-Code-Low-Code-/blob/main/Pics/Cities.png)
