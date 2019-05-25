from data import access

class Access(object):
  """ Used actor may make available other actors. """
  def fill(self):
    self.off = access.data

  def process(self, pool):
    for name in self.off.keys():
      self._propagate(pool, name)

  def _propagate(self, pool, name):
    if pool[name]['access']['used']:
      self._handle_others(pool, name)

  def _handle_others(self, pool, name):
    for other in self.off.pop(name):
      pool[other].unlock()