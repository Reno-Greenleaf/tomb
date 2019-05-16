class Labyrinth(dict):
  """ Handles movement from one location to another. """
  def fill(self):
    self.passes = {
      'arc': ('treasury', 'entrance')
    }

  def process(self, pool):
    for passage, locations in self.passes.items():
      actor = pool[passage]
      self._handle_passage(actor, locations, pool)

  def _handle_passage(self, actor, locations, pool):
    if actor['labyrinth']:
      actor.leave()
      self._pass(pool, locations)
      
  def _pass(self, pool, locations):
    first, second = locations

    if pool[first]['labyrinth']:
      pool[first].leave()
      pool[second].enter()
    elif pool[second]['labyrinth']:
      pool[second].leave()
      pool[first].enter()