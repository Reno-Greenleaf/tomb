from json import load

class Labyrinth(object):
  """ Handles movement from one location to another. """
  def __init__(self):
    self.passage = ''
    self.destination = ''

  def fill(self):
    with open('data/labyrinth.json', 'r') as data:
      self.passes = load(data)

  def process(self, pool):
    for passage in self.passes:
      self._get_current_passage(pool, passage)

    if self.passage == '':
      return

    pool[self.passage].leave()
    left, right = self.passes[self.passage]

    if pool[left]['labyrinth']['current']:
      self.destination = right
      pool[left].leave()
    else:
      self.destination = left
      pool[right].leave()

    pool[self.destination].enter()

    for name in pool.get_rooms()[self.destination]:
      self._notify_passage(pool, name)

    self.passage = ''

  def _get_current_passage(self, pool, passage):
    if pool[passage]['labyrinth']['current']:
      self.passage = passage

  def _notify_passage(self, pool, name):
    if name in self.passes:
      pool[name].entered(self._is_right(name))

  def _is_right(self, passage):
    return self.passes[passage][1] == self.destination
