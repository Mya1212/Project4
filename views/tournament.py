    
class TournamentViews:

    def display_main_menu(self):
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Tournament menu")
        print("[2] Player menu")
        print("[3] Exit program")

    def display_tournament_menu(self):
        print("\n\n=== TOURNAMENT MENU ===\n")
        print("[1] Tournament list")
        print("[2] Create tournanment")
        print("[3] Return main menu")

    def error_input(self):
        print("error")

    def display_message(self, message: str):
        """Print a message in the console"""
        print(f"\n{message}\n")