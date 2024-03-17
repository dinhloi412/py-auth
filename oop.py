class Player:
    team_name = "Manchester City"  # class variables
    former_teams = []  # class variables

    def __init__(self, name):
        self.name = name  # instance variables

    @classmethod
    def hello(cls):
        print(cls.team_name)


# Tạo 2 objects thuộc class Player
p1 = Player("David Silva")
p2 = Player("Yaya Toure")

# Dùng built-in method `append` để thêm giá trị vào variable `former_teams`
p1.former_teams.append("Celta Vigo")  # dùng sai class variable
p2.former_teams.append("Barcelona")  # dùng sai class variable

# In properties của các objects
print("Name:", p1.name)
print("Team Name:", p1.team_name)
print(p1.former_teams)
print("Name:", p2.name)
print("Team Name:", p2.team_name)
print(p2.former_teams)
print(Player.hello())
