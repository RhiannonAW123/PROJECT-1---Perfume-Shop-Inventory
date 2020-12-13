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

product1 = Product("Chance", "Romantic", 20, 60, 70, manufacturer1)
product_repository.save(product1)

product2 = Product("Forever", "Sweet", 25, 50, 60, manufacturer2)
product_repository.save(product2)