class Pet:
    def __init__(self, name):
        self.name = name
        self.food = 50
        self.happiness = 50
        self.health = 100

    def _clamp_attributes(self):
        self.food = max(0, min(100, self.food))
        self.happiness = max(0, min(100, self.happiness))
        self.health = max(0, min(100, self.health))

    def feed(self):
        if self.health == 0:
            print(f"{self.name} is too sick to eat. Visit the vet!")
            return

        print(f"You feed {self.name}.")
        self.food += 25
        self.health += 5
        self._clamp_attributes()
        self.update_attributes()

    def play(self):
        if self.health == 0:
            print(f"{self.name} is too sick to play. Visit the vet!")
            return

        print(f"You play with {self.name}. GJ!")
        self.happiness += 25
        self._clamp_attributes()
        self.update_attributes()

    def visit_vet(self):
        print(f"You take {self.name} to the vet. {self.name} feels much better!")
        self.health = 100
        self._clamp_attributes()
        self.update_attributes()

    def check_status(self):
        print(f"\n {self.name}'s Status")
        print(f"Food:      {self.food}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Health:    {self.health}/100")
        if self.health == 0:
            print("STATUS: CRITICAL! Visit the Vet immediately.")
        elif self.health < 30:
            print("STATUS: Unhealthy (Low Health)")
        else:
            print("STATUS: Good")
        print("-----------------------")

    def update_attributes(self):
        self.food -= 5

        self.happiness -= 5

        if self.food < 20:
            print(f"Warning: {self.name} is hungry! Health is dropping.")
            self.health -= 10
        if self.happiness < 20:
            print(f"Warning: {self.name} is very sad! Health is dropping.")
            self.health -= 10

        self._clamp_attributes()


def main():
    print("Welcome to the Virtual Pet Game!")
    try:
        pet_name = input("Enter a name for your pet: ").strip()
    except (EOFError, KeyboardInterrupt):
        pet_name = "Buddy"
        print("\nUsing default name 'Buddy'.")

    if not pet_name:
        pet_name = "Buddy"

    my_pet = Pet(pet_name)
    print(f"You have adopted {my_pet.name}!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed the Pet")
        print("2. Play with the Pet")
        print("3. Visit the Vet")
        print("4. Check Pet Status")
        print("5. Exit")

        try:
            choice = input("Enter your choice (1-5): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput cancelled or not supported. Exiting.")
            choice = '5'

        if choice == '1':
            my_pet.feed()
        elif choice == '2':
            my_pet.play()
        elif choice == '3':
            my_pet.visit_vet()
        elif choice == '4':
            my_pet.check_status()
        elif choice == '5':
            print(f"Goodbye! {my_pet.name} will miss you.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()