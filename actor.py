class Actor(dict):
  """ Available when there's no other behavior. """
  def load(self, data):
    for key, value in data.items():
      self[key] = value

  def obey(self, command):
    """ Receive input from input/output. """
    pass

  def render(self):
    """ Discover current state of the actor. """
    return self['io'].pop('output')

  def enter(self):
    """ Inform the actor that it was entered. """
    pass

  def leave(self):
    """ Informs the actor that it was left. """
    pass

  def entered(self, right=True):
    """ Tell from which side of the actor main character entered. """
    pass

  def unlock(self):
    """ Inform the actor that related actor is successfully used. """
    pass


class Behaviour(object):
  """ Adds abilities to actors. """
  def __init__(self, actor):
    self.actor = actor

  def __getitem__(self, key):
    return self.actor[key]

  def __setitem__(self, key, value):
    self.actor[key] = value

  def get(self, key, default):
    return self.actor.get(key, default)

  def load(self, data):
    self.actor.load(data)

  def obey(self, command):
    self.actor.obey(command)

  def render(self):
    return self.actor.render()

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
      self['io']['output'] = self['io']['description']
    else:
      self.actor.obey(command)

  def enter(self):
    self['labyrinth']['current'] = True
    self.actor.enter()

  def leave(self):
    self['labyrinth']['current'] = False
    self.actor.leave()


class Passage(Behaviour):
  """ Connects two locations. """
  def obey(self, command):
    left = command == self['io']['left_use_command'] and self['labyrinth']['right']
    right = command == self['io'].get('right_use_command', self['io']['left_use_command']) and not self['labyrinth']['right']

    if left or right:
      self._use()
    elif command == 'look around':
      self['io']['output'] = self._describe()
    else:
      self.actor.obey(command)

  def _describe(self):
    if self['labyrinth']['right']:
      return self['io']['right_description']
    else:
      return self['io']['left_description']

  def _use(self):
    if self['labyrinth']['right']:
      self['io']['output'] = self['io'].get('right_usage', self['io']['left_usage'])
    else:
      self['io']['output'] = self['io']['left_usage']

    self['labyrinth']['current'] = True

  def entered(self, right=True):
    self['labyrinth']['right'] = right
    self.actor.entered(right)


class Switch(Behaviour):
  """ Can provide access to other actors. """
  def obey(self, command):
    if command == 'look around':
      self['io']['output'] = self._describe()
    elif command == self['io']['use_command']:
      self['io']['output'] = self._use()
    else:
      self.actor.obey(command)

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
