"""
Patron singleton
"""

from tkinter import S

class  Sigleton:
    
    _insteance = None

    def __new__(cls):
        if not cls._insteance:
            cls._insteance = super(Sigleton, cls).__new__(cls)

        return cls._insteance
    
sigelton1 = Sigleton()
print(sigelton1)
sigelton2 = Sigleton()
print(sigelton2)

print(sigelton1 is sigelton2)

# Las dos instancias de singelton son iguales 
# ya que la primera adquiere un valor y la segunda trae ese mismo valor inicial


"""
Extra
"""

class UserSession:

    

    id: int = None
    user_name: str = None
    name: str = None
    email: str = None


    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)

        return cls._instance
        
    def set_user(self, id, user_name, name, email):
        self.id = id
        self.user_name = user_name
        self.name = name
        self.email = email

    def get_user(self):
        return f"{self.id}, {self.user_name}, {self.name}, {self.email}"
    
    def clear_user(self):
        self.id = None
        self.user_name = None
        self.name = None
        self.email = None


session1 = UserSession()
session1.set_user(1, "Nicolacho02", "Nicolas Heguaburu", "nicoheguaburu02@gmail.com" ) #Login
print(session1.get_user())


session2 = UserSession() #Navegacion
print(session2.get_user())

session3 = UserSession()
session3.clear_user()
print(session3.get_user())

print(session2.get_user())
