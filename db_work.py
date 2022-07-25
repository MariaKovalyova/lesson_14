import sqlite3
from typing import Counter



def get_title(title=None):
    
    db = sqlite3.connect('netflix.db')
    cur = db.cursor()
    cur.execute(f"""SELECT title, country, release_year, listed_in, description 
                    FROM netflix 
                    WHERE title like '%{title}%'""")
    s = cur.fetchone()
    db.close()
    
    return {"title": s[0],
 		"country": s[1],
		"release_year": s[2],
		"genre": s[3],
		"description": s[4]}


def get_year_to_year(year_from, year_to):

    db = sqlite3.connect('netflix.db')
    cur = db.cursor()

    cur.execute(f"""SELECT title, release_year
                    FROM netflix 
                    WHERE release_year BETWEEN {year_from} and {year_to}
                    ORDER BY release_year, title
                    LIMIT 100""")
    
    s = cur.fetchall()
    db.close()
    
    result = []
    for title in s:
        result.append({"title": title[0],
                        "release_year": title[1]})
    
    return result


def get_by_rat(rating):

    ratings_list = {"children": "'6'",
                "family": "'G', 'PG', 'PG-13'",
                "adult": "'R', 'NC-17'"}
    
    db = sqlite3.connect('netflix.db')
    cur = db.cursor()

    cur.execute(f"""SELECT title, rating, description 
                    FROM netflix 
                    WHERE rating IN ({ratings_list[rating]})
                    LIMIT 100""")
    
    s = cur.fetchall()
    db.close()
    
    result = []
    for title in s:
        result.append({"title": title[0],
                        "rating": title[1],
                        "description": title[2]})
    
    return result


def get_genre(genre):
    
    db = sqlite3.connect('netflix.db')
    cur = db.cursor()

    cur.execute(f"""SELECT title, description 
                    FROM netflix 
                    WHERE listed_in LIKE '%{genre}%'
                    LIMIT 10""")
    s = cur.fetchall()
    db.close()
    
    result_list = []
    for film in s: 
        result_list.append({
            "title": film[0],
            "description": film[1]
        })
    
    return result_list


def pairs(actor1, actor2):

    db = sqlite3.connect('netflix.db')
    cur = db.cursor()

    cur.execute(f"""SELECT 'cast' 
        FROM netflix
        WHERE 'cast' LIKE '%{actor1}%'
        AND 'cast' LIKE '%{actor2}%' """)

    s = cur.fetchall()
    db.close()

    result_list = []
    for actor in s:
        result_list.extend(actor[0].split(', '))
    counter = Counter(result_list)
    result_list2 = []
    for actor, count in counter.items():
        if actor not in [actor1, actor2] and count > 2:
            result_list2.append(actor)
    
    return result_list2


def search_movie(film_type, release_year, genre):
    db = sqlite3.connect('netflix.db')
    cur = db.cursor()

    cur.execute(f"""SELECT title, description
            FROM netflix
            WHERE type = '%{film_type}%'
            AND release_year = '%{release_year}%'
            AND listed_in LIKE '%{genre}%'""")

    s = cur.fetchall()
    db.close()

    result_list = []
    for film in s:
        result_list.append({
            "titile": film[0],
            "description": film[1]
        })
    return result_list

print(search_movie('TV Show', 2000, 'Drama'))



