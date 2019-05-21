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
      self._walk_through(pool, location, command)

  def _find_current(self, current, location, actor):
    if actor['labyrinth'].get('current', False):
      current.append(location)

  def _walk_through(self, pool, location, command):
    if command == 'look around':
      output = pool[location].obey(command)
      self._print(output)
      self._print_content(pool, location)
    else:
      addressed = command.split()[-1]
      self._print_addressed(pool, addressed, location, command)

  def _print_content(self, pool, location):
    for name in pool.get_rooms()[location]:
      output = pool[name].obey('look around')
      self._print(output)

  def _print_addressed(self, pool, addressed, location, command):
    if addressed in pool.get_rooms()[location]:
      output = pool[addressed].obey(command)
      self._print(output)

  def _print(self, output):
    if output:
      print output