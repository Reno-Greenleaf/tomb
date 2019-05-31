from actor import Actor, Location, Passage, Switch
from json import load

class Pool(dict):
  """ Contains ingame objects. """
  def fill(self):
    with open('data/actors.json', 'r') as data:
      actors = load(data)

    for name, properties in actors.items():
      self._build(properties, name)

    with open('data/space.json', 'r') as data:
      self.space = load(data)

  def get_rooms(self):
    return self.space

  def _build(self, properties, name):
    actor = Actor()
    actor.load(properties)

    if 'io' not in properties:
      self[name] = actor
      return

    if 'labyrinth' in properties:
      actor = Location(actor)

    if 'labyrinth' in properties and 'right' in properties['labyrinth']:
      actor = Passage(actor)

    if 'access' in properties:
      actor = Switch(actor)

    self[name] = actor