class MyClass:
    # _ -> Sirve para indicar que un attribute is private, se puede acceder a el
    # -> protected.
    _my_attribute_private = "Attribute Private..."
    # __ -> Sirve para indicar que un attribute is very private, no se puede
    # acceder a el -> private.
    __my_attribute_very_private = "Attribute very Private..."
    
    # _ -> Sirve para indicar que un method is private, se puede acceder a el
    # -> protected.
    def _my_method_private(self):
        print("Method Private...")
    # __ -> Sirve para indicar que un method is very private, no se puede
    # acceder a el -> private.
    def __my_method_very_private(self):
        print("Method very Private...")

obj = MyClass()

print(obj._my_attribute_private)
# print(obj.__my_attribute_very_private)

obj._my_method_private()
# obj.__my_method_very_private()