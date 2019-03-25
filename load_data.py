import csv
import mysql.connector
import MySQLdb
import re 
import datetime
import os

conn = MySQLdb.connect(host=os.getenv("DB_HOST"), 
                    port=int(os.getenv("PORT")),
                    user = os.getenv("USERNAME"),
                    passwd = os.getenv("PASSWORD"),
                    db = os.getenv("DATABASE"))
cursor = conn.cursor()


# Methods to add data to correct table in the database
def add_to_article_db(data, cursor):
    cursor.execute("""INSERT INTO article( headline, description, publish_date, author_1, author_2, thumbnail1_url, thumbnail2_url, thumbnail3_url ) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", 
        (data))
def add_to_video_db(data, cursor):
    cursor.execute("""INSERT INTO video( title, description, publish_date, duration, video_series, thumbnail1_url, thumbnail2_url, thumbnail3_url ) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""", 
        (data))
def add_to_category_db(data, cursor):
    cursor.execute("""INSERT INTO category( category_type, description) 
        VALUES(%s, %s)""", 
        (data))
def add_to_cateogry_article_db(data, cursor):
    cursor.execute("""
    INSERT INTO category_article(category_id, article_id)
    VALUES (%s, %s)
    """ ,
    (data))  

def add_to_cateogry_video_db(data, cursor):
    cursor.execute("""
    INSERT INTO category_video(category_id, video_id)
    VALUES (%s, %s)
    """ ,
    (data))



csv_data = csv.reader(file('codefoo.csv'))
with open('main.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile)
    # Remaking csv file to get only the data I need. 
    for row in csv_data:
        filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[21], row[25]])


with open('main.csv', "r") as csv_reader:
    reader = csv.reader(csv_reader, delimiter=',')

    for row in reader:
        
        row_id, content_id,	content_type,	title,	headline,	description,	publish_date,	duration,	video_series,	author_1,	author_2,	tag_1,	tag_2,	tag_3,	thumbnail_1_URL,	thumbnail_2_URL, thumbnail_3_URL = row

        ## Reformat publish_date format to match sql datetime
        # if publish_date:
        #     f = "%Y-%m-%dT%H:%M:%S+%f"
        #     publish_date = datetime.datetime.strptime(publish_date, f)

        ## Add article data to article table
        # if "article" in content_type:
        #     article_data =  headline, description,publish_date, author_1, author_2, thumbnail_1_URL, thumbnail_2_URL, thumbnail_3_URL
        #     add_to_article_db(article_data, cursor)

        ## Add video data to video table
        # if "video" in content_type:
        #     f = "%Y-%m-%dT%H:%M:%S+%f"
        #     publish_date = datetime.datetime.strptime(publish_date, f)
        #     video_data = title, description, publish_date, duration, video_series, thumbnail_1_URL, thumbnail_2_URL, thumbnail_3_URL
        #     add_to_video_db(video_data, cursor)

        ## Add all categories to categories tabel
        # Sweepstakes data
        # if "Win a" in headline  or "Win a" in description: 
        #     desc = " ".join([headline, description])
        #     sweepstakes_data = "sweepstakes", desc
        #     add_to_category_db(sweepstakes_data, cursor)
        # Deals data
        # if "Deals" in  headline  or "Deals" in description: 
        #     desc = " ".join([headline, description])
        #     deals_data = "Deals", desc
        #     add_to_category_db(deals_data, cursor)
        # # PS4 Data
        # if "PS4" in headline or "PS4 " in description:
        #     desc = " ".join([headline, description])
        #     ps4_data = "PS4", desc
        #     add_to_category_db(ps4_data, cursor)
        # # Nintendo Data
        # if "Nintendo" in headline or "Nintendo" in description:
        #     desc = " ".join([headline, description])
        #     nintendo_data = "Nintendo", desc
        #     add_to_category_db(nintendo_data, cursor)
        # # Xbox Data
        # if "Xbox" in headline or "Xbox" in description:
        #     desc = " ".join([headline, description])
        #     xbox_data = "Xbox", desc
        #     add_to_category_db(xbox_data, cursor)
        # # PC Data
        # if "PC" in headline or "PC" in description:
        #     desc = " ".join([headline, description])
        #     pc_data = "PC", desc
        #     add_to_category_db(pc_data, cursor)
        # # Movie News Data
        # if "Movie" in headline or "Movie" in description:
        #     desc = " ".join([headline, description])
        #     movie_data = "Movie", desc
        #     add_to_category_db(movie_data, cursor)
        # # TV News Data
        # if "TV" in headline or "TV" in description:
        #     desc = " ".join([headline, description])
        #     tv_data = "TV", desc
        #     add_to_category_db(tv_data, cursor)
        # # Game news Data
        # if "Game" in headline or "Game" in description:
        #     desc = " ".join([headline, description])
        #     game_data = "game", desc
        #     add_to_category_db(game_data, cursor)
        # # Game guides Data 
        # if "Walkthrough" in headline or "Walkthrough" in description:
        #     desc = " ".join([headline, description])
        #     guide_data = "Guides", desc
        #     add_to_category_db(guide_data, cursor)


"""
Logic for adding data to join table categories_articles
Still need to manually change the category_type to the category you need as well as change the if statement to the string you are looking for. 

EX: 
category_type would be "TV"

And in the If statement it would if "TV" exists in headline or description 
"""
# cursor.execute("""
# select 'article' as article,
#        article_id as article_id, 
#        description, 
#        headline
# from article
# union all
# select 'category' as category,
#        category_id as cateogry_id,
#        description, 
#        category_type
# from category
# where category_type = 'TV';
# """)

# all_ca_ids = list()
# articles = list()
# categories = list()
# for round in cursor:
#     if "TV" in round[3] or "TV" in round[2]:
#         if round[0] == 'article':
#             articles.append([round[0], round[1], round[2], round[3]])
#         if round[0] == 'category':
#             categories.append([round[0], round[1], round[2]])

#         all_ca_ids.append(round[1])
# if len(articles) != len(categories):
#     all_ca_ids = []
#     for art in articles:
#         for cat in categories:
#             if art[2] in cat[2] or art[3] in cat[2]:
#                 print("CAT", cat[1])
#                 print("ART", art[1])
#                 all_ca_ids.append(art[1])
#                 all_ca_ids.append(cat[1])
#     article_ids = all_ca_ids[::2]
#     category_ids = all_ca_ids[1:][::2]
# else:      
#     article_ids = all_ca_ids[:len(all_ca_ids)//2]
#     category_ids = all_ca_ids[len(all_ca_ids)//2:]

# print(article_ids)
# print(category_ids)
# for idx in range(0, len(article_ids)):
#     data = category_ids[idx], article_ids[idx]
#     print(data)
#     add_to_cateogry_article_db(data, cursor)




"""
Logic for adding data to join table categories_videos
Still need to manually change the category_type to the category you need as well as change the if statement to the string you are looking for. 

EX: 
category_type would be "Deals"

And in the If statement it would if "Deals" exists in headline or description 

"""

# cursor.execute("""
# select 'video' as video,
#        video_id as video_id, 
#        description, 
#        title
# from video
# union all
# select 'category' as category,
#        category_id as cateogry_id,
#        description, 
#        category_type
# from category
# where category_type = 'Deals';
# """)

# all_cv_ids = list()
# videos = list()
# categories = list()
# for round in cursor:
#     if "Deals" in round[3] or "Deals" in round[2]:
#         if round[0] == 'video':
#             videos.append([round[0], round[1], round[2], round[3]])
#         if round[0] == 'category':
#             categories.append([round[0], round[1], round[2]])

#         all_cv_ids.append(round[1])
# if len(videos) != len(categories):
#     all_cv_ids = []
#     for vid in videos:
#         for cat in categories:
#             if vid[2] in cat[2] or vid[3] in cat[2]:
#                 print("CAT", cat[1])
#                 print("VID", vid[1])
#                 all_cv_ids.append(vid[1])
#                 all_cv_ids.append(cat[1])
#     video_ids = all_cv_ids[::2]
#     category_ids = all_cv_ids[1:][::2]
# else:
#     print("THEY ARE THE SAME LENGTH")      
#     video_ids = all_cv_ids[:len(all_cv_ids)//2]
#     category_ids = all_cv_ids[len(all_cv_ids)//2:]

#     video_ids = all_cv_ids[::2]
# print(video_ids, "VIDEO LIST OF IDS")
# print(category_ids, "CATEGORY LIST OF IDS")
# video_ids = all_cv_ids[::2]
# for idx in range(0, len(video_ids)):
#     video_ids = all_cv_ids[::2]
#     data = category_ids[idx], video_ids[idx]
#     print(data)
#     add_to_cateogry_video_db(data, cursor)


#close the connection to the database.
conn.commit()
cursor.close()
print("Done")