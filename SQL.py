from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
#[<database_setup.MenuItem object at 0x8fd740c>]
cheesepizza = MenuItem(name = "Cheese Pizza",description = "Made with all natural ingridients and fresh mozzarella", course ="Entree", price ="$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()
#[<database_setup.MenuItem object at 0x8fdd78c>]
firstResult = session.query(Restaurant).first()
firstResult.name
u'Pizza Palace'
session.query(Restaurant).all()


