from colors import BLUE, print_color, RESET
import os

def display_menu():
    print_color("================= JOOM CONSULTAS =================", BLUE)
    print("[1] Consulta OSINT completa")
    print("[2] Consulta rápida (notícias)")
    print("[3] Apenas Wikipedia")
    print("[4] Comparar última consulta")
    print("[5] Ver relatórios salvos")
    print("[6] Limpar relatórios")
    print("[7] Configurações")
    print("[8] Ajuda")
    print("[0] Sair")
    print_color("==================================================", BLUE)

def get_choice():
    return input(f"{RESET}👉 Escolha uma opção: ")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
