class Fan:
    """
    Creates a fan with a brand, number of blades, and speed.
    """
    
    def __init__(self, brand: str, num_blades: int, speed: int):
        """
        Creates a new Fan object.
        
        :param brand: The brand of the fan.
        :param num_blades: The number of blades the fan has.
        :param speed: The initial speed of the fan.
        """
        self.brand = brand
        self.num_blades = num_blades
        self.speed = speed 
    
    def speed_up(self) -> None:
        """
        Increases the fan speed by 1.
        
        :return: None
        """
        self.speed += 1
        print(f"{self.brand} fan speed increased to {self.speed}.")

    def speed_down(self) -> None:
        """
        Decreases the fan speed by 1. Can't go below 0.
        
        :return: None
        """
        if self.speed > 0:
            self.speed -= 1
            print(f"{self.brand} fan speed decreased to {self.speed}.")
        else:
            print(f"{self.brand} fan is already at the lowest speed.")

    def set_speed(self, new_speed: int) -> None:
        """
        Sets the fan speed to a set value with parameter called new_speed. Can't be negative.
        
        :param new_speed: The new speed value.
        :return: None
        """
        if new_speed >= 0:
            self.speed = new_speed
            print(f"{self.brand} fan speed set to {self.speed}.")
        else:
            print("Speed can not be negative.")
    
    def print_info(self) -> None:
        """
        Prints all instance variables of the fan.
        
        :return: None
        """
        print(f"Fan Info - Brand: {self.brand}, Blades: {self.num_blades}, Speed: {self.speed}")


def main() -> None:
    """
    Creates instances of the Fan class and demonstrates its methods.
    
    :return: None
    """
    fan1 = Fan("Vornado", 3, 2)
    fan2 = Fan("Dyson", 5, 0)
    
    fan1.speed_up()
    fan1.set_speed(4)
    fan2.speed_up()
    fan2.speed_down()
    
    fan1.print_info()
    fan2.print_info()


if __name__ == "__main__":
    main()
