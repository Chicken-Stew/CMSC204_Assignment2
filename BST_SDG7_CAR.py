# Program for BST based on fuel efficiency of cars (in L/100 km)

class CarNode:
    def __init__(self, brand, l_per_100km, hybrid, engine_type, horsepower):
        self.brand = brand
        self.l_per_100km = l_per_100km  # Fuel efficiency in liters per 100 km
        self.hybrid = hybrid  # True if hybrid, false otherwise
        self.engine_type = engine_type  # Gasoline, Diesel, Electric, etc.
        self.horsepower = horsepower  # Engine power
        self.left = None
        self.right = None

class CarBinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, brand, l_per_100km, hybrid, engine_type, horsepower):
        new_car = CarNode(brand, l_per_100km, hybrid, engine_type, horsepower)
        if self.root is None:
            self.root = new_car
        else:
            node = self.root
            while node:
                if l_per_100km < node.l_per_100km:  # Lower L/100 km is better
                    if node.left is None:
                        node.left = new_car
                        return
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_car
                        return
                    node = node.right

    # Search
    def search(self, brand):
        node = self.root
        while node is not None:
            if node.brand == brand:
                hybrid_status = "Hybrid" if node.hybrid else "Non-Hybrid"
                print(f"Found: {node.brand} - {node.l_per_100km} L/100 km, {hybrid_status}, {node.engine_type}, {node.horsepower} HP")
                return
            if brand < node.brand:
                node = node.left
            else:
                node = node.right
        print(f"{brand} not found.")

    # Delete
    def delete(self, brand):
        node = self.root
        parent = None
        while node is not None and node.brand != brand:
            parent = node
            if brand < node.brand:
                node = node.left
            else:
                node = node.right

        if node is None:
            print(f"{brand} not found.\n")
            return
        # Node with no children
        if node.left is None and node.right is None:
            if node != self.root:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        # Node with 2 children
        elif node.left is not None and node.right is not None:
            successor_parent = node
            successor = node.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            node.brand, node.l_per_100km, node.hybrid, node.engine_type, node.horsepower = \
                successor.brand, successor.l_per_100km, successor.hybrid, successor.engine_type, successor.horsepower
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        # Node with 1 child
        else:
            child = node.left if node.left else node.right
            if node != self.root:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child
        print(f"{brand} has been deleted.")

# EXAMPLE: INSERTING
car = CarBinarySearchTree()
car.insert("Toyota Prius", 4.2, True, "Hybrid", 121)
car.insert("Tesla Model 3", 1.81, True, "Electric", 283)
car.insert("Ford F-150", 11.76, False, "Gasoline", 290)
car.insert("Honda Accord", 7.13, False, "Gasoline", 192)
car.insert("Honda Civic", 6.53, False, "Gasoline", 158)
car.insert("Toyota Camry", 7.35, False, "Gasoline", 203)
car.insert("Tesla Model S", 1.90, True, "Electric", 670)
car.insert("Ford Mustang", 10.69, False, "Gasoline", 450)
car.insert("Toyota Corolla", 6.92, False, "Gasoline", 169)
car.insert("Honda Insight", 4.28, True, "Hybrid", 151)
car.insert("Ford Ranger Diesel", 8.40, False, "Diesel", 210)
car.insert("Honda CR-V Diesel", 7.84, False, "Diesel", 160)
car.insert("Toyota Fortuner", 9.5, False, "Diesel", 204)

# EXAMPLE: SEARCHING
print("\nSearching for Toyota Prius:")
car.search("Toyota Prius") # Should return

# EXAMPLE: DELETING
print("\nDeleting Tesla Model 3 from the database:")
car.delete("Tesla Model 3") # Should be deleted
print("\nDeleting Toyota Innova from the database:")
car.delete("Toyota Innova") # Should not be found
