#If else statements
#Execute some logic or instructions if (and only if) the condition it's correct
#We can catch with an else in case that the condition doesn't match
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
age = 36

if age < 100:
  if age < 21:
    print("you'ur a minor without access")
  else:
    print("you're younger then a 100 year old") 
else:
  print("yo'ur older than someone with 100 years")   

#Exercise
t = 4
e = 5
if t > e:
  print("What's up")
else:
  print("Deuces")

