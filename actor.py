class Entrance(dict):
  """ Room to start from. """
  def __init__(self):
    self['labyrinth'] = {}

  def load(self):
    self['labyrinth']['current'] = True
    self['io'] = "You're in the entrance."

  def obey(self, command):
    if command == 'look around':
      return self['io']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Treasury(dict):
  """ Room to visit. """
  def __init__(self):
    self['labyrinth'] = {}

  def load(self):
    self['labyrinth']['current'] = False
    self['io'] = "You're in the treasury."

  def obey(self, command):
    if command == 'look around':
      return self['io']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Arc(dict):
  """ Connects treasury and entrance. """
  def __init__(self):
    self['labyrinth'] = {}

  def load(self):
    self['labyrinth']['current'] = False
    self['labyrinth']['right'] = False
    self['io'] = "An arc leads to another room."

  def obey(self, command):
    if command == 'go through arc':
      self['labyrinth']['current'] = True
    elif command == 'look around':
      return self._choose_description()

  def _choose_description(self):
    if self['labyrinth']['right']:
      return "The arc leads to entrance."
    else:
      return "The arc leads to treasury."

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False

  def entered(self, right=True):
    self['labyrinth']['right'] = right


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