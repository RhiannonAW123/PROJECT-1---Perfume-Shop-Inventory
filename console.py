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

product1 = Product("Chance", "Fresh", 20, 60, 70, manufacturer1)
product_repository.save(product1)

product2 = Product("Forever", "Romantic", 25, 50, 60, manufacturer2)
product_repository.save(product2)

product3 = Product("Candy", "Sweet", 10, 50, 60, manufacturer3)
product_repository.save(product3)