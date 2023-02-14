
def check_unique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

str = input("Please enter string: ")

if(check_unique(str)):
  print(f"String {str} contains unique value")
else:
  print(f"String {str} contains duplicate value")