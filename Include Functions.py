# Incorporated functions to outline main body and has call functi
class GitIsAwesomeProgram:

    def __init__(self):

        self.menu_options = {

            '1': self.print_git_is_awesome,
            '2': self.greet_user,
            '3': self.quit_program,
        }

    def print_git_is_awesome(self):

        print('Git is awesome')

    def greet_user(self):

        # Get user's name.
        user_input = input("Enter your name: ")

        if user_input.strip():

            # Removes any spaces left in.
            print(f'Hello, {user_input.strip()}!')

        else:

            print('Hello there!')

    def quit_program(self):

        print('Goodbye!')
        exit()

    def display_menu(self):

        # Menu.
        print("\nMenu:")
        print("1. Print 'Git is awesome'")
        print("2. Greet user")
        print("3. Quit")

    def run(self):

        print('Welcome to the Git is Awesome Program!')

        while True:

            self.display_menu()

            choice = input("Enter your choice (1 - 3): ")
            action = self.menu_options.get(choice)

            if action:

                # Searches through 'menu_options' for the user's choice.
                action()

            else:

                print('Invalid choice. Please enter a number between 1 and 3.')


if __name__ == "__main__":

    program = GitIsAwesomeProgram()
    program.run()
