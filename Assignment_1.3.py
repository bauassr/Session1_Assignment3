 #Assignment 1.3# 
def reverse(s):
      str = ""
      for i in s:
        str = i + str
      return str

print("Please enter your first name :")
First_Name = input()
print("Please enter your last name :")
Last_Name = input()
print("Word Reversed :")
print(Last_Name + " "+ First_Name)
print("Letters Reversed for each Words:")
print(reverse(Last_Name) + " "+ reverse( First_Name))
 