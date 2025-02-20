class Robot:
    def __init__(self,model,energy_level=100):
        self._model=model
        self.__energy_level=energy_level

    def get_energy(self):
        return self.__energy_level

    def set_energy(self,energy):
        if 0<= energy <=100:
            self.__energy_level=energy
        else:
            print(f"energy level should be 0 and 100")

    def charge(self,amount):
        self.__energy_level += amount
        if self.__energy_level > 100:
            self.__energy_level=100

robot = Robot("alexa")

try :
    print(robot.__energy_level)

except AttributeError as e:
    print(f"error {e}")

print(f"the current energy level is {robot.get_energy()}")
robot.set_energy(50)
print(f"the updated energy level is {robot.get_energy()}")

robot.charge(85)
print(f"energy level after charging is {robot.get_energy()}")


