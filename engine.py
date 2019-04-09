#!/usr/bin/python

from pool import Pool
from input_output import IO

pool = Pool()
io = IO()
pool.fill()
io.fill()

while True:
  io.process(pool)