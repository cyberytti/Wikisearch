import os

try:
    from mediawiki import MediaWiki
except ImportError:
    print("The 'mediawiki' library is not installed. Installing...")
    os.system("pip install pymediawiki==0.7.4")
    if os.name == "posix":
    	os.system("clear")
    else:
    	os.system("cls")
    from mediawiki import MediaWiki

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_banner():
    banner = f"""
{Color.HEADER}    ██████╗ ███████╗███╗   ██╗███████╗██╗   ██╗███████╗██████╗ 
    ██╔══██╗██╔════╝████╗  ██║██╔════╝██║   ██║██╔════╝██╔══██╗
    ██████╔╝█████╗  ██╔██╗ ██║█████╗  ██║   ██║█████╗  ██████╔╝
    ██╔══██╗██╔══╝  ██║╚██╗██║██╔══╝  ██║   ██║██╔══╝  ██╔══██╗
    ██████╔╝███████╗██║ ╚████║██║     ╚██████╔╝███████╗██║  ██║
    ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                              
{Color.OKBLUE}        Welcome to WikiSearch!
{Color.ENDC}    """
    print(banner)

try:
    data = {}
    wikipedia = MediaWiki()
    
    print_banner()
    while True:
        print("\nWhat would you like to search for? (Type 'exit' to quit): ")
        text = input(f"{Color.OKGREEN}Search about: {Color.ENDC}")
        
        
        text = text.replace(" ", "")
        string_without_spaces = text.replace(" ", "")
        if string_without_spaces.lower() == 'exit':
            print("Goodbye!")
            break
        
        print(f"\n{Color.OKBLUE}Searching about '{text}'...{Color.ENDC}\n")
        
        search_results = wikipedia.search(text)

        if len(search_results) > 0:
            print(f"{Color.OKGREEN}Search results:{Color.ENDC}")
            for idx, result in enumerate(search_results):
                print(f"{Color.OKBLUE}{idx + 1}. {result}{Color.ENDC}")

            while True:
                try:
                    number = int(input(f"{Color.OKGREEN}\nEnter the number to view details (or 0 to search again): {Color.ENDC}"))
                    if number == 0:
                        break
                    elif 1 <= number <= len(search_results):
                        print(f"\n{Color.OKBLUE}Fetching details about '{search_results[number - 1]}'...{Color.ENDC}\n")
                        print(wikipedia.page(search_results[number - 1]).summary)
                        break
                    else:
                        print(f"{Color.WARNING}Invalid number entered. Please try again.{Color.ENDC}")
                except ValueError:
                    print(f"{Color.WARNING}Invalid input. Please enter a number.{Color.ENDC}")
        else:
            print(f"{Color.WARNING}No results found for '{text}'.{Color.ENDC}")
    
except Exception as error:
    print(f"{Color.FAIL}ERROR: {error}{Color.ENDC}")