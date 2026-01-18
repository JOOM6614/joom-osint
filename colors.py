import sys

# Cores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RED = "\033[31m"

def print_color(text, color=RESET, end="\n"):
    sys.stdout.write(f"{color}{text}{RESET}{end}")
