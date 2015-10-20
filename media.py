# -*- coding: utf-8 -*-
"""
 * Created by PyCharm.
 * Project: P1_Movie_Trailer
 * Author name: Iraquitan Cordeiro Filho
 * Author login: iraquitan
 * File: movie
 * Date: 10/14/15
 * Time: 11:11 PM
 * To change this template use File | Settings | File Templates.
"""
import webbrowser


class Movie(object):
    """Class to store movies, with info like title, storyline, year, director,
    poster image and youtube trailer"""
    
    def __init__(self, movie_title, movie_storyline, movie_year,
                 movie_director, poster_image, trailer_youtube):
        """Constructor for Movie class with info about the movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = movie_year
        self.director = movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self, ):
        """Show the movie trailer

        Args:

        Returns:
            :return:
            :rtype:
        """
        webbrowser.open(self.trailer_youtube_url)
