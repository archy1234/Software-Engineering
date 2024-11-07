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

        try:

            user_input = input("Enter your name: ")

            if user_input.strip():
                
                print(f'Hello, {user_input.strip()}!')

            else:

                print('Hello there!')

        except Exception as e:
            print(f"An error occurred: {e}")

    def quit_program(self):

        print('Goodbye!')
        exit()

    def display_menu(self):

        print("\nMenu:")
        print("1. Print 'Git is awesome'")
        print("2. Greet user")
        print("3. Quit")

    def run(self):

        print('Welcome to the Git is Awesome Program!')

        while True:

            self.display_menu()

            try:

                choice = input("Enter your choice (1-3): ")
                action = self.menu_options.get(choice)

                if action:

                    action()

                else:

                    print('Invalid choice. Please enter a number between 1 and 3.')

            except KeyboardInterrupt:

                print("\nOperation cancelled by user.")
                break

            except Exception as e:

                print(f"An unexpected error occurred: {e}")
                break


if __name__ == "__main__":

    try:

        program = GitIsAwesomeProgram()
        program.run()

    except Exception as e:

        print(f"Failed to start the program due to an error: {e}")
