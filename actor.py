class Entrance(dict):
  """ Room to start from. """
  def load(self):
    self['labyrinth'] = True
    self['io'] = "You're in the entrance."

  def obey(self, command):
    if command == 'look around':
      return self['io']

  def enter(self):
    self['labyrinth'] = True

  def leave(self):
    self['labyrinth'] = False


class Treasury(dict):
  """ Room to visit. """
  def load(self):
    self['labyrinth'] = False
    self['io'] = "You're in the treasury."

  def obey(self, command):
    if command == 'look around':
      return self['io']

  def enter(self):
    self['labyrinth'] = True

  def leave(self):
    self['labyrinth'] = False


class Arc(dict):
  """ Connects treasury and entrance. """
  def load(self):
    self['labyrinth'] = False
    self['io'] = "An arc leads to another room."

  def obey(self, command):
    if command == 'go through arc':
      self['labyrinth'] = True
    elif command == 'look around':
      return self['io']

  def enter(self):
    self['labyrinth'] = True

  def leave(self):
    self['labyrinth'] = False


class Container(dict):
  """ Holds the artifact. """
  def load(self):
    self['io'] = "There's a metal container here."

  def obey(self, command):
    if command == 'look around':
      return self['io']


class Key(dict):
  """ Opens container. """
  def load(self):
    self['io'] = "A key lies on the floor."

  def obey(self, command):
    if command == 'look around':
      return self['io']


class Artifact(dict):
  """ Final goal. """
  def load(self):
    self['io'] = "An antient artifact is in the container."

  def obey(self, command):
    if command == 'look around':
      return self['io']