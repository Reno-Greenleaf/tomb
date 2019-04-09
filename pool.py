from actor import Entrance, Treasury, Container, Key, Artifact

class Pool(dict):
  """ Contains ingame objects. """
  def fill(self):
    self['entrance'] = Entrance()
    self['treasury'] = Treasury()
    self['container'] = Container()
    self['key'] = Key()
    self['artifact'] = Artifact()