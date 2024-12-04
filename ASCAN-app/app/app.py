from colorama import init, Fore, Style
import time

# Inicializar colorama para suporte de cores no terminal
init()

def animated_hello_world():
    # Mensagem colorida e animada
    hello = "Hello, World! 🌍"
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    
    print(Fore.WHITE + "Preparando a mensagem..." + Style.RESET_ALL)
    time.sleep(1)
    
    for color in colors:
        print(color + hello + Style.RESET_ALL)
        time.sleep(0.5)
    
    # Mensagem final em arco-íris
    rainbow_hello = ''.join([colors[i % len(colors)] + char for i, char in enumerate(hello)])
    print(rainbow_hello + Style.RESET_ALL)

# Executar a função
if __name__ == "__main__":
    animated_hello_world(host="0.0.0.0", port=5000)
