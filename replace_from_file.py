#!/usr/bin/env python3
# encoding: utf-8
import fileinput
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

filename_src = '/Users/NewFolk/OneDrive/Евраз/ToDel/Замена в CV/source.txt'
filename_tgt = '/Users/NewFolk/OneDrive/Евраз/ToDel/Замена в CV/target.txt'
filename_map = '/Users/NewFolk/OneDrive/Евраз/ToDel/Замена в CV/IOBJ.txt'

target_file = open(filename_tgt, "w+", encoding="utf-8")
source_file = open(filename_src, encoding="utf-8")
Subs = open(filename_map, encoding="utf-8")
tgt_line = ""
mapper = []
for l in Subs:
	s = l.rstrip().split(sep=";")
	mapper.append(s)

for line in source_file:
	tgt_line = line
	for s in mapper:
		tgt_line = tgt_line.replace(s[0], s[1])
	target_file.write(tgt_line)

target_file.close()