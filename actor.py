class Actor(dict):
  """ Common behavior for ingame objects. """
  def unlock(self):
    self['access']['locked'] = False


class Entrance(Actor):
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


class Treasury(Actor):
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


class Arc(Actor):
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
      return "You're going through the arc."
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


class Container(Actor):
  """ Holds the artifact. """
  def __init__(self):
    self['access'] = {}

  def load(self):
    self['io'] = "There's a metal container here."
    self['access']['locked'] = True
    self['access']['used'] = False

  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'open container':
      return self._use()

  def _describe(self):
    if self['access']['used']:
      return "Open container stands here."
    else:
      return self['io']

  def _use(self):
    if self['access']['used']:
      return "It's opened already."
    elif self['access']['locked']:
      return "The container is locked."
    else:
      self['access']['used'] = True
      return "The key fits. You've opened the container."


class Key(Actor):
  """ Opens container. """
  def __init__(self):
    self['access'] = {}

  def load(self):
    self['io'] = "A key lies on the floor."
    self['access']['used'] = False
    self['access']['locked'] = False

  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'take key':
      return self._use()

  def _use(self):
    if self['access']['used']:
      return "It's taken already."
    else:
      self['access']['used'] = True
      return "You've taken the key."

  def _describe(self):
    if self['access']['used']:
      return ''
    else:
      return self['io']


class Artifact(Actor):
  """ Final goal. """
  def __init__(self):
    self['access'] = {}

  def load(self):
    self['io'] = "An antient artifact lies in the container."
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
      return self['io']

  def _use(self):
    if self['access']['used']:
      return "It's taken already"
    elif self['access']['locked']:
      return "What artifact?"
    else:
      self['access']['used'] = True
      return "You've taken the artifact."