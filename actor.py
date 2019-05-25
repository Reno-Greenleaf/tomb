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


class Location(Behaviour):
  """ This is where other actors and main character are placed. """
  def obey(self, command):
    if command == 'look around':
      return self['io']['description']
    else:
      return self.actor.obey(command)

  def enter(self):
    self['labyrinth']['current'] = True
    self.actor.enter()

  def leave(self):
    self['labyrinth']['current'] = False
    self.actor.leave()


class Passage(Behaviour):
  """ Connects two locations. """
  def obey(self, command):
    if command == self['io']['use_command']:
      self['labyrinth']['current'] = True
      return self['io']['usage']
    elif command == 'look around':
      return self._describe()
    else:
      return self.actor.obey(command)

  def _describe(self):
    if self['labyrinth']['right']:
      return self['io']['right_description']
    else:
      return self['io']['left_description']

  def entered(self, right=True):
    self['labyrinth']['right'] = right
    self.actor.entered(right)


class Switch(Behaviour):
  """ Can provide access to other actors. """
  def obey(self, command):
    if command == 'look around':
      return self._describe()
    elif command == self['io']['use_command']:
      return self._use()

  def unlock(self):
    self['access']['locked'] = False
    self.actor.unlock()

  def _describe(self):
    if self['access']['used']:
      return self['io'].get('used_description', '')
    elif self['access']['locked']:
      return self['io'].get('locked_description', self['io']['description'])
    else:
      return self['io']['description']

  def _use(self):
    if self['access']['used']:
      return self['io'].get('used_usage', '')
    elif self['access']['locked']:
      return self['io'].get('locked_usage', '')
    else:
      self['access']['used'] = True
      return self['io']['usage']
