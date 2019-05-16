#!/usr/bin/python

from pool import Pool
from input_output import IO
from labyrinth import Labyrinth

pool = Pool()
pool.fill()

io = IO()
labyrinth = Labyrinth()
io.fill()
labyrinth.fill()

while True:
  labyrinth.process(pool)
  io.process(pool)