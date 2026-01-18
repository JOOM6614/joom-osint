from colors import GREEN, BOLD, RESET

def show_banner():
    banner = f"""{GREEN}{BOLD}
    ██╗ ██████╗  ██████╗ ███╗   ███╗
    ██║██╔═══██╗██╔═══██╗████╗ ████║
    ██║██║   ██║██║   ██║██╔████╔██║
    ██║██║   ██║██║   ██║██║╚██╔╝██║
    ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
    ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
    
    [ CONSULTAS OSINT - TERMINAL MODE ]
    {RESET}"""
    print(banner)
