# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:15:37 2017

@author: Bruce Feynman
"""

#get the states and generate the corresponding wmv file.

import generate_the_number_by_arduino as raw_input

import pysynth as ps

states=raw_input.main()
encode_table={1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g"}

song=[]
for state in states:
    note=encode_table[state]
    song.append((note,4))
song=tuple(song)



ps.make_wav(song, fn = "music.wav")


    