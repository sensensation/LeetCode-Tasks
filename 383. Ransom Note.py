class Solution:
  def canConstruct(self, ransomNote, magazine):
    list1 = list(magazine)
    for i in ransomNote:
      if i in list1:
        list.remove(i)
      else:
        return 0
    return 1
