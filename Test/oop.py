class User:
  pass


user = User()
print(type(user) == User)

class User:

  nation = 'VietNam'
  def __init__(self, name, age, gender, occupation):
    self.name = name
    self.age = age
    self.gender = gender
    self.occupation = occupation

user = User(name='Nguyen Tue Tam', age=19, gender='female', occupation=' student')
print(user.nation, user.name, user.age, user.gender, user.occupation)
