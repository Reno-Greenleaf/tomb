from actor import Actor, Entrance, Treasury, Container, Key, Artifact, Arc
from data import data

class Pool(dict):
  """ Contains ingame objects. """
  def fill(self):
    for name, properties in data.items():
      self._build(properties, name)

    self.space = {
      'treasury': set(['container', 'artifact', 'arc']),
      'entrance': set(['key', 'arc'])
    }

  def get_rooms(self):
    return self.space

  def _build(self, properties, name):
    actor = Actor()
    actor.load(properties)

    if name == 'entrance':
      actor = Entrance(actor)

    if name == 'treasury':
      actor = Treasury(actor)

    if name == 'container':
      actor = Container(actor)

    if name == 'key':
      actor = Key(actor)

    if name == 'artifact':
      actor = Artifact(actor)

    if name == 'arc':
      actor = Arc(actor)

    self[name] = actor