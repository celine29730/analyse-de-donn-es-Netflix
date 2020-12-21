import mysql.connector
import pandas as pd

link = mysql.connector.connect(**{
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'netflix',
    'port': '8082'
    })
cursor=link.cursor()


data_netflix = pd.read_csv("netflix_titles.csv", sep=',')
data_reduit = data_netflix.dropna()



director = list(data_reduit["director"].values)
director_set = set()
for i in range(len(director)):
    liste = director[i]
    dir_ = liste.split(", ")
    for y in dir_:
        director_set.add(y)

for item in director_set:
    query = "INSERT INTO director(director_name) VALUES (%s)", (item)
    cursor.execute(query)
    link.commit()
print('coucou')


country = list(data_reduit["country"].values)
country_set = set()


for i in range(len(country)):
    liste = country[i]
    dir_ = liste.split(", ")
    for y in dir_:
        country_set.add(y)

for item in country_set:
    query = "INSERT INTO country(country_name) VALUES (%s)", (item)
    cursor.execute(query)
    link.commit()
print('coucou')

'''
# INSERT INTO `director` (`director_name`) SELECT DISTINCT `COL 5` FROM `table 10`
# INSERT INTO `actor` (`actor_name`) SELECT DISTINCT `COL 6` FROM `table 10`
# INSERT INTO `listed_in` (`liste_name`) SELECT DISTINCT `COL 12` FROM `table 10`



# procédure pour récupérer le nom d'un film en fonction de la liste des acteurs
DELIMITER |
CREATE PROCEDURE films_actor_all (IN actor_studio VARCHAR(256))
BEGIN
SELECT title FROM film
INNER JOIN actor_film ON film.show_id = actor_film.id_film
INNER JOIN actor ON actor_film.id_actor = actor.id_actor WHERE actor_name = actor_studio;
END |
DELIMITER ;

CALL films_actor_all()

#procédure pour récupérer le nom d'un film en fonction du ou des producteurs
DELIMITER |
CREATE PROCEDURE films_director_all (IN actor_studio VARCHAR(256))
BEGIN
SELECT title FROM film
INNER JOIN director_film ON film.show_id = director_film.id_film
INNER JOIN director ON director_film.id_director = director.id_director WHERE director_name = actor_studio;
END |
DELIMITER ;

CALL films_director_all()

#procédure pour récupérer le nom d'un film en fonction de sa catégorie
DELIMITER |
CREATE PROCEDURE gived_listed_in (IN actor_studio VARCHAR(256))
BEGIN
SELECT title FROM film
INNER JOIN dlisted_in_film ON film.show_id = listed_in_film.id_film
INNER JOIN listed_in ON listed_in_film.id_liste = listed_in.id_liste WHERE liste_name = actor_studio;
END |
DELIMITER ;

CALL gived_listed_in()

#procédure pour récupérer le nom d'un film en fonction de son pays

DELIMITER |
CREATE PROCEDURE all_film_country (IN give_country VARCHAR(256))
BEGIN
SELECT title FROM film
INNER JOIN country_film ON film.show_id = country_film.id_country
INNER JOIN country ON country_film.id_country = country.id_country WHERE country_name = give_country;
END |
DELIMITER ;

CALL all_film_country()

DELIMITER |
CREATE PROCEDURE film_date
(IN annee INT)
BEGIN
SELECT * FROM avions WHERE release_year < annee;
END|
DELIMITER ;
CALL film_date(2000);

CREATE VIEW  all_actor_film AS select actor.actor_name  AS
select actor_name FROM actor 
JOIN actor, film_actor ON actor.id_actor = film_actor.id_actor  
JOIN film, film_actor ON film.show_id = film_actor.show_id;

# vue

CREATE VIEW all_film SELECT title, director_name, actor_name, country_name, liste_name, release_year, rating, duration, description FROM film, actor, director, listed_in, country
INNER JOIN actor_film ON film.show_id = actor_film.id_film
INNER JOIN actor ON actor_film.id_actor = actor.id_actor
INNER JOIN director_film ON film.show_id = director_film.id_film
INNER JOIN director ON director_film.id_director = director.id_director
INNER JOIN dlisted_in_film ON film.show_id = listed_in_film.id_film
INNER JOIN listed_in ON listed_in_film.id_liste = listed_in.id_liste
INNER JOIN country_film ON film.show_id = country_film.id_country
INNER JOIN country ON country_film.id_country = country.id_country


CREATE VIEW all_film AS SELECT title, director_name, actor_name, country_name, liste_name, release_year, rating, duration, description FROM film
NATURAL JOIN actor
NATURAL JOIN country
NATURAL JOIN director
NATURAL JOIN listed_in
'''