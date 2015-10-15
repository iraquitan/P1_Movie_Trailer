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
    """Documentation of Movie class"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor for Movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self, ):
        """Documentation of show_trailer method

        Args:

        Returns:
            :return:
            :rtype:
        """
        webbrowser.open(self.trailer_youtube_url)

