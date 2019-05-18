class IO(object):
  """ Decides which objects should react to a command. """
  def fill(self): pass

  def process(self, pool):
    command = raw_input("> ")

    locations = pool.get_rooms()
    current = []

    for location in locations:
      self._find_current(current, location, pool[location])

    for location in current:
      self._walk_through(location, pool, command)

  def _find_current(self, current, location, actor):
    if actor['labyrinth'].get('current', False):
      current.append(location)

  def _walk_through(self, location, pool, command):
    output = pool[location].obey(command)
    self._print(output)

    for name in pool.get_rooms()[location]:
      output = pool[name].obey(command)
      self._print(output)

  def _print(self, output):
    if output:
      print output