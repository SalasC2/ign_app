# Description

# How the tables work
- ### The database is designed as a many to many relationship where the Article Table has a relationship with the Category table and the Video table has a relationship with the Category Table. 
    - Categories can have many videos and videos can have many categories
    - Categories can have many articles and articles can have many categories
- ### I decided to create a seperate Category table to categorize each article and video to get different data. 
    - For example you can get articles by the category Deals to only get articles by deals and you can get videos by the category walkthrough. 
- ### Article Table are designed to get all the data from the csv that are typed as article
- ### Video Table are designed to get all the data from the csv that are typed as video
- ### Category Table are designed to get all the data from the csv that meet a certain category type 
    * Categories are categorized by
    * |  Sweepstakes | > Sweepstakes are categorized by being able to win prizes
      |  Deals | > Deals are categorized by Daily Deals
      |  PS4  | > PS4 is categorized by any mention of PS4 Games, reviews or Walkthrough
      | Nintendo | > Nintendo is categorized by any mention of Nintendo Games, reviews or Walkthrough
      | Xbox | > Xbox is categorized by any mention of Xbox Games, reviews or Walkthrough
      | PC | > PC is categorized by any mention of PC Games, reviews or Walkthrough 
      | Movie | > Movie is categorized by any mention of Movie Review or Updates
      |  TV | > TV is categorized by any mention of TV reviews or updates
      | Game | Game is categozied by any mention of any game news or updates 
      | Guides | Guides is categorized by any mention of any Walkthrough or guides for a game

# How to use
- ### Run `python requirements.txt` to install all dependencies
- ### Run `cp templates.env .env` and fill your .env with the necessary data
- ### Run codefoo.csv on load_data.py, this will create a new csv with all the necessary data this script needs in a csv file main.csv
- ### Add data to article table, video table, category table by load_data file and add articles logic, add videos logic, and add categories logic
- ### In order to insert data into join table for category_article and category_video, you have to manually change the category_type inside the sql statements as well as change the if statements right at the beginning of the loop after the sql call.
- ### Once all data is uploaded simply run your flask server by runing python api.py and then go to any of the routes below to test 

```  
    /getArticles
        * Returns all articles
    /getVideos
        * Returns all videos
    /getArticlesByCategory/<string:category_type>
        * Returns all articles by a specific category
    /getVideosByCategory/<string:category_type>
        * Returns all videos by a specific category
```
# Schema Design 
| Tables |  
|---|
|  Article | 
|  Category | 
|  Video  |
|category_article|
|category_video| 
_______

|Article|
|---|
|article_id|
|headline|
|description|
|publish_date|
|author_1|
|author_2|
|thumbnail1_url|
|thumbnail2_url|
|thumbnail3_url|

________

|Video|
|---|
|video_id|
|title|
|description|
|publish_date|
|duration|
|video_series|
|thumbnail1_url|
|thumbnail2_url|
|thumbnail3_url|

---

|Category|
|---|
|category_id|
|category_type|
|description|

---

|category_article|
|---|
|category_id|
|category_type|
|description|

---

|category_video|
|---|
|category_id|
|category_type|
|description|