class Actor(dict):
  """ Common behavior for ingame objects. """
  def unlock(self):
    self['access']['locked'] = False


class Entrance(Actor):
  """ Room to start from. """
  def __init__(self):
    self['labyrinth'] = {}
    self['io'] = {}

  def load(self):
    self['labyrinth']['current'] = True
    self['io']['description'] = "You're in the entrance."

  def obey(self, command):
    if command == 'look around':
      return self['io']['description']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Treasury(Actor):
  """ Room to visit. """
  def __init__(self):
    self['labyrinth'] = {}
    self['io'] = {}

  def load(self):
    self['labyrinth']['current'] = False
    self['io']['description'] = "You're in the treasury."

  def obey(self, command):
    if command == 'look around':
      return self['io']['description']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Arc(Actor):
  """ Connects treasury and entrance. """
  def __init__(self):
    self['labyrinth'] = {}
    self['io'] = {}

  def load(self):
    self['labyrinth']['current'] = False
    self['labyrinth']['right'] = False
    self['io']['right_description'] = "The arc leads to entrance."
    self['io']['left_description'] = "The arc leads to treasury."
    self['io']['usage'] = "You're going through the arc."

  def obey(self, command):
    if command == 'go through arc':
      self['labyrinth']['current'] = True
      return self['io']['usage']
    elif command == 'look around':
      return self._choose_description()

  def _choose_description(self):
    if self['labyrinth']['right']:
      return self['io']['right_description']
    else:
      return self['io']['left_description']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False

  def entered(self, right=True):
    self['labyrinth']['right'] = right


class Container(Actor):
  """ Holds the artifact. """
  def __init__(self):
    self['access'] = {}
    self['io'] = {}

  def load(self):
    self['io']['description'] = "There's a metal container here."
    self['io']['used_description'] = "Opened container stands here."
    self['io']['usage'] = "The key fits. You've opened the container."
    self['io']['used_usage'] = "It's open already."
    self['io']['locked_usage'] = "The container is locked."
    self['access']['locked'] = True
    self['access']['used'] = False

  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'open container':
      return self._use()

  def _describe(self):
    if self['access']['used']:
      return self['io']['used_description']
    else:
      return self['io']['description']

  def _use(self):
    if self['access']['used']:
      return self['io']['used_usage']
    elif self['access']['locked']:
      return self['io']['locked_usage']
    else:
      self['access']['used'] = True
      return self['io']['usage']


class Key(Actor):
  """ Opens container. """
  def __init__(self):
    self['access'] = {}
    self['io'] = {}

  def load(self):
    self['io']['description'] = "A key lies on the floor."
    self['io']['usage'] = "You've taken the key."
    self['io']['used_usage'] = "It's taken already."
    self['access']['used'] = False
    self['access']['locked'] = False

  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'take key':
      return self._use()

  def _use(self):
    if self['access']['used']:
      return self['io']['used_usage']
    else:
      self['access']['used'] = True
      return self['io']['usage']

  def _describe(self):
    if self['access']['used']:
      return ''
    else:
      return self['io']['description']


class Artifact(Actor):
  """ Final goal. """
  def __init__(self):
    self['access'] = {}
    self['io'] = {}

  def load(self):
    self['io']['description'] = "An antient artifact lies in the container."
    self['io']['usage'] = "You've taken the artifact."
    self['io']['locked_usage'] = "What artifact?"
    self['io']['used_usage'] = "It's taken already"
    self['access']['locked'] = True
    self['access']['used'] = False

  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'take artifact':
      return self._use()

  def _describe(self):
    if self['access']['used'] or self['access']['locked']:
      return ''
    else:
      return self['io']['description']

  def _use(self):
    if self['access']['used']:
      return self['io']['used_usage']
    elif self['access']['locked']:
      return self['io']['locked_usage']
    else:
      self['access']['used'] = True
      return self['io']['usage']