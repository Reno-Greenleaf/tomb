class IO(object):
  """ Decides which objects should react to a command. """
  def fill(self): pass

  def process(self, pool):
    locations = pool.get_rooms()
    current = []

    for location in locations:
      self._find_current(current, pool[location], location)

    for name in current:
      self._print_pending(pool[name])

    for actor in pool.itervalues():
      self._print_pending(actor)

    command = raw_input("> ")

    for location in current:
      self._walk_through(pool, location, command)

  def _print_pending(self, actor):
    if 'output' in actor.get('io', {}):
      self._print(actor.render())

  def _find_current(self, current, actor, location):
    if actor['labyrinth'].get('current', False):
      current.append(location)

  def _walk_through(self, pool, location, command):
    if command == 'look around':
      pool[location].obey(command)
      self._command_content(pool, location)
    else:
      addressed = command.split()[-1]
      self._command_addressed(pool, addressed, location, command)

  def _command_content(self, pool, location):
    for name in pool.get_rooms()[location]:
      pool[name].obey('look around')

  def _command_addressed(self, pool, addressed, location, command):
    if addressed in pool.get_rooms()[location]:
      pool[addressed].obey(command)

  def _print(self, output):
    if output:
      print output
