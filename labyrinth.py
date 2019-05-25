from data import labyrinth

class Labyrinth(object):
  """ Handles movement from one location to another. """
  def fill(self):
    self.passes = labyrinth.data

  def process(self, pool):
    for passage, locations in self.passes.items():
      actor = pool[passage]
      self._handle_passage(actor, locations, pool)

  def _handle_passage(self, actor, locations, pool):
    if actor['labyrinth']['current']:
      self._pass(pool, locations, actor)
      
  def _pass(self, pool, locations, actor):
    actor.leave()
    left, right = locations

    if pool[left]['labyrinth']['current']:
      self._notify_passes(pool, pool.get_rooms()[left], False)
      pool[left].leave()
      pool[right].enter()
    elif pool[right]['labyrinth']['current']:
      self._notify_passes(pool, pool.get_rooms()[right], True)
      pool[right].leave()
      pool[left].enter()

  def _notify_passes(self, pool, content, right):
    for name in content:
      self._notify_pass(pool, name, right)

  def _notify_pass(self, pool, name, right):
    if name in self.passes:
      passage = pool[name].entered(right)