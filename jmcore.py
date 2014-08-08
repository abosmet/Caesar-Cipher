#!/usr/bin/python
#
# Module jmcore is a store of useful functions with usefulness in many places.
# Import these functions by using standard import syntax (eg. from jmcore import rprint).
#
def rprint(ls):
  """
  Prints lists or dictionaries recursively, placing each index on a new line.
  Inputs:
    ls: <list> or <dict> The list or dictionary to be printed
  Outputs:
    Prints values to the terminal
  """
  if type(ls) == dict:
    for key in ls:
      print(ls[key])
  elif type(ls) == list:
    for a in ls:
      print(str(a))
  else:
    raise TypeError("jmcore.rprint: Invalid input. rprint takes dict or list. Input was %s." % (ls))
  return
#
if __name__ == '__main__':
  print("jmcore.py is not a script.")
  print("PYTHON STOP")
#
#
#
#
# EOF
