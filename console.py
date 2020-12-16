from models.manufacturer import Manufacturer
from models.product import Product

import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer1 = Manufacturer("Chanel", "012345678")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Dior", "012345679")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Prada", "01568799")
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer("Tom Ford", "0145682229")
manufacturer_repository.save(manufacturer4)

manufacturer5 = Manufacturer("Marc Jacobs", "0145684445")
manufacturer_repository.save(manufacturer5)

manufacturer6 = Manufacturer("Jo Malone", "0132684225")
manufacturer_repository.save(manufacturer6)

manufacturer7 = Manufacturer("Elizabeth Arden", "0152685635")
manufacturer_repository.save(manufacturer7)


product1 = Product("Chance", "Fresh", 20, 60, 70, manufacturer1)
product_repository.save(product1)

product2 = Product("Forever", "Romantic", 25, 50, 60, manufacturer2)
product_repository.save(product2)

product3 = Product("Candy", "Sweet", 9, 50, 60, manufacturer3)
product_repository.save(product3)

product4 = Product("Portifino", "Luxury", 25, 70, 90, manufacturer4)
product_repository.save(product4)

product5 = Product("Daisy", "Fun", 30, 60, 70, manufacturer5)
product_repository.save(product5) 

product6 = Product("Earl Grey and Cucumber", "Sophisticated", 30, 60, 70, manufacturer6)
product_repository.save(product6)

product7 = Product("", "Sophisticated", 30, 60, 70, manufacturer7)
product_repository.save(product7)


