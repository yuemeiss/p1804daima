#!/usr/bin/env python
# coding=utf-8
l = ['boxoffice.csv', 'games.csv', 'imdb.csv', 'olympics-locations.csv', 'olympics-results.csv', 'oscar-actor.csv', 'oscar-film.csv', 'seinfeld-episodes.csv', 'seinfeld-foods.csv']
new_l = [e[:-4] for e in l]
print(new_l)
