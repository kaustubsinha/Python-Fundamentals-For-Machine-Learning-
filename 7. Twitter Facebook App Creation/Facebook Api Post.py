# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:16:44 2018

@author: Kaustub Sinha
"""

import facebook as fb
access_token = "EAACEdEose0cBAJt4wNq0QfAZCQjqVerZAfNWDmBVZBwpr2iRH5bFbGBZAuh2tivYpE6oowB2vP9IKIdZCwWBQ1MO7fMjZC3MGjpPEJMaHD7Bnar4w0ZAu9qTUJugPBHvZB6HZC5ZAZBhqEdRCYqExaI7DneJEwBUQUtJvkcDgqJrVq3SGBnM6uuO6n9ae8fTPAV2eMZD"
status = "Hi This is me Kaustub"
graph = fb.GraphAPI(access_token)
post_id = graph.put_wall_post(status)