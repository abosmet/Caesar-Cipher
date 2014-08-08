#!/usr/bin/python
#
class Caesar:
  """
  This class creates a basic Caesar cipher from the alphabet.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  #
  def __init__(self,shift=3,test=None):
    """
    Object instantiation. Creates keys for the cipher and the reverse cipher
      for encryption and decryption.
    Inputs:
      shift      <int>      Cipher displacement, how many spaces to move to the
                              left from initial character for encrypted char.
                              Default: 3
      test       <booleal>  Set to True to activate test mode. Default None
    Outputs:
      Returns a Caesar object.
    """
    self.key = {}
    self.rev_key = {}
    letters = list(Caesar.alphabet)
    for i in range(0,len(letters)):
      new_index = i - shift
      rev_index = i + shift
      if new_index < 0:
        new_index += len(letters)
      if rev_index >= len(letters):
        rev_index -= len(letters)
      self.key[letters[i]] = letters[new_index]
      self.rev_key[letters[i]] = letters[rev_index]
    if test:
      print("Key:", self.key)
      print("KEYS@@@@@@@@@@@@", self.key.keys())
      from jmcore import rprint
      rprint(self.key)
  #
  def encrypt(self,message):
    """
    Encrypts a string using instance's encryption key.
    Inputs:
      message:   <string>  String to encrypt.
    Outputs:
      encrypted: <string>  Encrypted string.
    """
    split = list(message)
    keys = self.key.keys()
    for i in range(0,len(split)):
      if split[i] in keys:
        split[i] = self.key[split[i]]
    encrypted = ''.join(split)
    return encrypted
  #
  def decrypt(self,message):
    """
    Decrypts a string using instance's decryption key.
    Inputs:
      message:   <string>  String to decrypt.
    Outputs:
      decrypted: <string>  Decrypted string.
    """
    split = list(message)
    keys = self.rev_key.keys()
    for i in range(0,len(split)):
      if split[i] in keys:
        split[i] = self.rev_key[split[i]]
    decrypted = ''.join(split)
    return decrypted
  #
# End Class Caesar
#
def main():
  """
  Run a test for module functionality. This will create a Caesar object and
    use it to encrypt a message and decrypt the result.
  """
  cipher = Caesar()
  text = "This is a test sentence.1@2#3$4%5"
  crypt = cipher.encrypt(text)
  print(crypt)
  decrypt = cipher.decrypt(crypt)
  print(decrypt)
  return
#
if __name__ == "__main__":
  main()
  print("PYTHON STOP")
  exit()
#
#
#
#
# EOF
