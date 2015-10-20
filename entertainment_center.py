# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: P1_Movie_Trailer
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: enterteinment_center
 * Date: 10/14/15
 * Time: 11:14 PM
 * To change this template use File | Settings | File Templates.
"""
import fresh_tomatoes_custom
import media


# Create various Movie's class instances
toy_story = media.Movie('Toy Story',
                        "A cowboy doll is profoundly threatened and jealous "
                        "when a new spaceman figure supplants him as top toy "
                        "in a boy's room.",
                        1995,
                        'John Lasseter',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',  # noqa
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie('Avatar',
                     "A paraplegic marine dispatched to the moon Pandora on a "
                     "unique mission becomes torn between following his "
                     "orders and protecting the world he feels is his home.",
                     2009,
                     'James Cameron',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',  # noqa
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

v_for_vendetta = media.Movie('V for Vendetta',
                             "Following world war, London is a police state "
                             "occupied by a fascist government, and a "
                             "vigilante known only as V (Hugo Weaving) uses "
                             "terrorist tactics to fight the oppressors of "
                             "the world in which he now lives.",
                             2005,
                             'James McTeigue',
                             'https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg',  # noqa
                             'https://www.youtube.com/watch?v=lSA7mAHolAw')

school_of_rock = media.Movie('School of Rock',
                             "After being kicked out of a rock band, Dewey "
                             "Finn becomes a substitute teacher of a strict "
                             "elementary private school, only to try and turn "
                             "it into a rock band.",
                             2003,
                             'Richard Linklater',
                             'http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg',  # noqa
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

hercules = media.Movie('Hercules',
                       "The son of the Greek Gods Zeus and Hera is stripped "
                       "of his immortality as an infant and must become a "
                       "true hero in order to reclaim it.",
                       1995,
                       'Ron Clements and John Musker',
                       'https://31.media.tumblr.com/8fb4acba91d558615119d25c40789140/tumblr_inline_n571ften4m1rtf1yw.jpg',  # noqa
                       'https://www.youtube.com/watch?v=NDMZHhcBHaQ')

garden_state = media.Movie('Garden State',
                           "A quietly troubled young man returns home for his "
                           "mother's funeral after being estranged from his "
                           "family for a decade.",
                           2004,
                           'Zach Braff',
                           'http://www.masculinity-movies.com/wp-content/uploads/2012/04/600full-garden-state-poster.jpg',  # noqa
                           'https://www.youtube.com/watch?v=u82n0e1mgmQ')

hunger_games = media.Movie('Hunger Games',
                           "Katniss Everdeen voluntarily takes her younger "
                           "sister's place in the Hunger Games, a televised "
                           "fight to the death in which two teenagers from "
                           "each of the twelve Districts of Panem are chosen "
                           "at random to compete.",
                           2012,
                           'Gary Ross',
                           'http://www.movieguide.org/wp-content/uploads/2012/06/98068201-0cc9-42ed-81ee-dcd480c4cba8.jpg',  # noqa
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

lotr_1 = media.Movie('LOTR 1 - The Fellowship of the Ring',
                     "A meek hobbit of the Shire and eight companions set out "
                     "on a journey to Mount Doom to destroy the One Ring and "
                     "the dark lord Sauron.",
                     2001,
                     'Peter Jackson',
                     'http://www.movieposter.com/posters/archive/main/105/MPW-52979',  # noqa
                     'https://www.youtube.com/watch?v=V75dMMIW2B4')

lotr_2 = media.Movie('LOTR 2 - The Two Towers',
                     "While Frodo and Sam edge closer to Mordor with the help "
                     "of the shifty Gollum, the divided fellowship makes a "
                     "stand against Sauron's new ally, Saruman, and his "
                     "hordes of Isengard.",
                     2002,
                     'Peter Jackson',
                     'https://wtfbabe.files.wordpress.com/2012/11/two-towers-poster.jpg',  # noqa
                     'https://www.youtube.com/watch?v=LbfMDwc4azU')

lotr_3 = media.Movie('LOTR 3 - The Return of the King',
                     "Gandalf and Aragorn lead the World of Men against "
                     "Sauron's army to draw his gaze from Frodo and Sam as "
                     "they approach Mount Doom with the One Ring.",
                     2003,
                     'Peter Jackson',
                     'http://sites.psu.edu/202d031/wp-content/uploads/sites/15365/2014/09/LOTR-King.jpg',  # noqa
                     'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

matrix = media.Movie('The Matrix',
                     "A computer hacker learns from mysterious rebels about "
                     "the true nature of his reality and his role in the war "
                     "against its controllers.",
                     1999,
                     'The Wachowski Brothers',
                     'https://www.movieposter.com/posters/archive/main/9/A70-4902',  # noqa
                     'https://www.youtube.com/watch?v=vKQi3bBA1y8')

movies = [toy_story, avatar, v_for_vendetta, school_of_rock, hercules,
          garden_state, hunger_games, lotr_1, lotr_2, lotr_3, matrix]

# Use customized fresh_tomatoes_custom to create webpage with Movies instances
fresh_tomatoes_custom.open_movies_page(movies)
