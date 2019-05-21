#!/usr/bin/python

from pool import Pool
from input_output import IO
from labyrinth import Labyrinth
from access import Access

pool = Pool()
pool.fill()

io = IO()
labyrinth = Labyrinth()
access = Access()
io.fill()
labyrinth.fill()
access.fill()

while True:
  labyrinth.process(pool)
  io.process(pool)
  access.process(pool)