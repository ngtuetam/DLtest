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

user = User(name='Pham Dinh Khanh', age=27, gender='male', occupation='AI Engineer')
print(user.nation, user.name, user.age, user.gender, user.occupation)