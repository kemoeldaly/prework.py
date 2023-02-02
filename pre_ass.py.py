# question 1
git def hello_name(USERNAME):
  print("Hello_" + USERNAME+"!")
hello_name('USERNAME')  


#question 2
def first_odds():
  for i in range(1,101):
    if i % 2 != 0:
      print(i)
first_odds()      


#question 3
def max_num_in_list(a_list):
  max_num = 0
  for number in a_list:
    if number > max_num:
      max_num = number
  return max_num

#another for 3
def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
max_num_in_list('a_list')

#question 4
def is_leap_year(a_year):
       return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)
is_leap_year('a_year')

#another way
def is_leap_year(a_year):
  if a_year % 400 == 0:
    return True
  elif a_year % 100 == 0:
    return False
  elif a_year % 4 == 0:
    return True
  else:
    return False


#question 5
def is_consecutive(a_list):
     set up variables
    s_consecutive = True
    last_num = I_LIST[0]
    iterate through list
    for num in a_list[1:]:
      if num != last_num + 1:
       is_consecutive = False
       break

    last_num = num
    return is_consecutive

#another way

def is_consecutive(a_list):
    if len(a_list) <= 1:
     return True
    else:
     sorted_list = sorted(a_list)
    return all(sorted_list[i + 1] - sorted_list[i] == 1 for i in range(len(sorted_list) - 1))

is_consecutive()
                       

