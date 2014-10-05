# Amazon-ETL

### Practicing data transformation and MongoDB import

## Directions
To run, place amazon.py and movies.small.txt in the same directory.
Output are import ready JSON and tsv files.
ETL-Notes.ipynb contains my notes and script tested with movies.sample.txt

## Contents
1. Data Exploration
2. Data Transformation
3. MongoDB import

### 1. Data Exploration

1. Take a look at our data.

```
verkter@localhost:~/Desktop/Amazon-ETL$ wc movies.small.txt 
  49994 1039720 6536908 movies.small.txt
```
We have total of lines of text, which is about 6,250 product reviews. Perhaps, we should take a sample of our dataset to work on our script. 

2. Take a look at first ten lines of the file to get a sense of our data. It appears that review information consists of 8 lines separated by a space.
```
product/productId: B003AI2VGA
review/userId: A141HP4LYPWMSR
review/profileName: Brian E. Erland "Rainbow Sphinx"
review/helpfulness: 7/7
review/score: 3.0
review/time: 1182729600
review/summary: "There Is So Much Darkness Now ~ Come For The Miracle"
review/text: Synopsis: On the daily trek from Juarez, Mexico to El Paso, Texas an ever increasing number of female workers are found raped and murdered in the surrounding desert. Investigative reporter Karina Danes (Minnie Driver) arrives from Los Angeles to pursue the story and angers both the local police and the factory owners who employee the undocumented aliens with her pointed questions and relentless quest for the truth.<br /><br />Her story goes nationwide when a young girl named Mariela (Ana Claudia Talancon) survives a vicious attack and walks out of the desert crediting the Blessed Virgin for her rescue. Her story is further enhanced when the "Wounds of Christ" (stigmata) appear in her palms. She also claims to have received a message of hope for the Virgin Mary and soon a fanatical movement forms around her to fight against the evil that holds such a stranglehold on the area.<br /><br />Critique: Possessing a lifelong fascination with such esoteric matters as Catholic mysticism, miracles and the mysterious appearance of the stigmata, I was immediately attracted to the '05 DVD release `Virgin of Juarez'. The film offers a rather unique storyline blending current socio-political concerns, the constant flow of Mexican migrant workers back and forth across the U.S./Mexican border and the traditional Catholic beliefs of the Hispanic population. I must say I was quite surprised by the unexpected route taken by the plot and the means and methods by which the heavenly message unfolds.<br /><br />`Virgin of Juarez' is not a film that you would care to watch over and over again, but it was interesting enough to merit at least one viewing. Minnie Driver delivers a solid performance and Ana Claudia Talancon is perfect as the fragile and innocent visionary Mariela. Also starring Esai Morales and Angus Macfadyen (Braveheart).

product/productId: B003AI2VGA
```

3. Lets grab first 100 review and double check that last review did not get cut off.
```
verkter@localhost:~/Desktop/Amazon-ETL$ head -n 800 movies.small.txt > movies.sample.txt
```
```
product/productId: B000063W1R
review/userId: A19O5ETNRJN39D
review/profileName: D. Myers
review/helpfulness: 1/1
review/score: 5.0
review/time: 1232064000
review/summary: spell-binding
review/text: I am not a movie fan.  I find it difficult to sit and watch a story for 2 hours (and nearly impossible to 'suspend disbelief').  I will not pretend to write a clinical analysis of movie-making.  I will simply say I have seen this movie twice (and plan to see it again, nearly unheard of in my case) and both times was fully enveloped in this fascinating, beautifully told story.  That editing and departure from the novel occurred in some points is no surprise (just 2 hours), but the essence of the story remains, the victory of good over evil.  Tremendous movie.
```

### 2. Data transformation

Please refer to ETL-Notes.ipynb for the notes on data transformation.

### 3. MongoDB import

```
verkter@localhost:~/Desktop/Amazon-ETL$ mongoimport --host linus.mongohq.com --port 10022 --username verkter --password amazonreviews --db amazon-reviews --collection reviews --type json --file movie.sample.output.json --jsonArray
connected to: linus.mongohq.com:10022
imported 88 objects
```