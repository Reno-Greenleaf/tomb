class Entrance(dict):
  """ Room to start from. """
  def obey(self, command):
    if command == 'look around':
      self['output'] = "You're in the entrance."


class Treasury(dict):
  """ Room to visit. """
  def obey(self, command):
    if command == 'look around':
      self['output'] = "You're in the treasury."


class Container(dict):
  """ Holds artifact. """
  def obey(self, command):
    if command == 'look around':
      self['output'] = "There's a metal container here."


class Key(dict):
  """ Opens container. """
  def obey(self, command):
    if command == 'look around':
      self['output'] = "A key lies on the floor."


class Artifact(dict):
  """ Final goal. """
  def obey(self, command):
    if command == 'look around':
      self['output'] = "An antient artifact is in the container."