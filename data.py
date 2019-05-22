data = {
  'entrance': {
    'labyrinth': {'current': True},
    'io': {'description': "You're in the entrance."}
  },
  'treasury': {
    'labyrinth': {'current': False},
    'io': {'description': "You're in the treasury."}
  },
  'arc': {
    'labyrinth': {'current': False, 'right': False},
    'io': {
      'right_description': "The arc leads to entrance.",
      'left_description': "The arc leads to treasury.",
      'usage': "You're going through the arc."
    }
  },
  'key': {
    'access': {'used': False, 'locked': False},
    'io': {
      'description': "A key lies on the floor.",
      'usage': "You've taken the key.",
      'used_usage': "It's taken already."
    }
  },
  'container': {
    'access': {'locked': True, 'used': False},
    'io': {
      'description': "There's a metal container here.",
      'used_description': "Opened container stands here.",
      'usage': "The key fits. You've opened the container.",
      'used_usage': "It's open already.",
      'locked_usage': "The container is locked."
    }
  },
  'artifact': {
    'access': {'used': False, 'locked': True},
    'io': {
      'description': "An antient artifact lies in the container.",
      'usage': "You've taken the artifact.",
      'used_usage': "It's taken already.",
      'locked_usage': "What artifact?"
    }
  }
}