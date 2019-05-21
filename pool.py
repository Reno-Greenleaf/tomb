from actor import Entrance, Treasury, Container, Key, Artifact, Arc

class Pool(dict):
  """ Contains ingame objects. """
  def fill(self):
    self['entrance'] = Entrance()
    self['treasury'] = Treasury()
    self['container'] = Container()
    self['key'] = Key()
    self['artifact'] = Artifact()
    self['arc'] = Arc()

    for name in self:
      self[name].load()

    self.space = {
      'treasury': set(['container', 'artifact', 'arc']),
      'entrance': set(['key', 'arc'])
    }

  def get_rooms(self):
    return self.space