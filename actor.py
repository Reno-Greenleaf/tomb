class Actor(dict):
  """ Available when there's no other behavior. """
  def load(self, data):
    for key, value in data.items():
      self[key] = value

  def obey(self, command):
    return ''

  def enter(self): pass

  def leave(self): pass

  def entered(self, right=True): pass

  def unlock(self): pass


class Behaviour(object):
  """ Adds abilities to actors. """
  def __init__(self, actor):
    self.actor = actor

  def __getitem__(self, key):
    return self.actor[key]

  def __setitem__(self, key, value):
    self.actor[key] = value

  def load(self, data):
    self.actor.load(data)

  def obey(self, command):
    return self.actor.obey(command)

  def enter(self):
    self.actor.enter()

  def leave(self):
    self.actor.leave()

  def entered(self, right=True):
    self.actor.entered(right)

  def unlock(self):
    self.actor.unlock()


class Entrance(Behaviour):
  """ Room to start from. """
  def obey(self, command):
    if command == 'look around':
      return self['io']['description']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Treasury(Behaviour):
  """ Room to visit. """
  def obey(self, command):
    if command == 'look around':
      return self['io']['description']

  def enter(self):
    self['labyrinth']['current'] = True

  def leave(self):
    self['labyrinth']['current'] = False


class Arc(Behaviour):
  """ Connects treasury and entrance. """
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


class Container(Behaviour):
  """ Holds the artifact. """
  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'open container':
      return self._use()

  def unlock(self):
    self['access']['locked'] = False

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


class Key(Behaviour):
  """ Opens container. """
  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'take key':
      return self._use()

  def unlock(self):
    self['access']['locked'] = False

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


class Artifact(Behaviour):
  """ Final goal. """
  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == 'take artifact':
      return self._use()

  def unlock(self):
    self['access']['locked'] = False

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