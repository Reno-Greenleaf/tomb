from actor import Actor, Location, Passage, Switch
from data import actors, space

class Pool(dict):
  """ Contains ingame objects. """
  def fill(self):
    for name, properties in actors.data.items():
      self._build(properties, name)

    self.space = space.data

  def get_rooms(self):
    return self.space

  def _build(self, properties, name):
    actor = Actor()
    actor.load(properties)

    if 'labyrinth' in properties:
      actor = Location(actor)

    if 'labyrinth' in properties and 'right' in properties['labyrinth']:
      actor = Passage(actor)

    if 'access' in properties:
      actor = Switch(actor)

    self[name] = actor