class IO(object):
  """ Decides which objects should react to a command. """
  def fill(self):
    self.contents = {
      'treasury': ('container', 'artifact'),
      'entrance': ('key',)
    }
    self.current_room = 'entrance'

  def process(self, pool):
    command = raw_input("> ")

    pool[self.current_room].obey(command)
    print pool[self.current_room].get('output', '')

    for name in self.contents[self.current_room]:
      pool[name].obey(command)
      print pool[name].get('output', '')