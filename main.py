import time
import os
from banner import show_banner
from menu import display_menu, get_choice, clear_screen
from colors import *
from sources.wikipedia import fetch_wikipedia
from sources.news import fetch_news
from utils.normalizer import save_report

def run_osint(mode, target):
    all_data = []
    if mode in [1, 3]:
        print_color(f"[*] Vasculhando Wikipedia para: {target}...", YELLOW)
        all_data.extend(fetch_wikipedia(target))
    
    if mode in [1, 2]:
        print_color(f"[*] Rastreando Google News para: {target}...", YELLOW)
        all_data.extend(fetch_news(target))
    
    return all_data

def process_results(results):
    if not results:
        print_color("\n[!] Nenhuma ocorrência relevante encontrada.", RED)
        return

    # Ordenação por Score de Relevância
    sorted_res = sorted(results, key=lambda x: x['score'], reverse=True)
    
    print_color(f"\n[+] {len(sorted_res)} Resultados encontrados:\n", GREEN)
    
    for r in sorted_res:
        print_color(f"[{r['label']}] {r['source']}", CYAN)
        print_color(f"TÍTULO: {r['title']}", BOLD)
        if 'link' in r: print(f"LINK: {r['link']}")
        if 'snippet' in r: print(f"RESUMO: {r['snippet'][:150]}...")
        print("-" * 30)
        time.sleep(0.1)

    save_report(sorted_res)
    print_color("\n[✔] Consulta finalizada e salva em last_report.txt", GREEN)

def start():
    while True:
        clear_screen()
        show_banner()
        display_menu()
        choice = get_choice()

        if choice == '0':
            print_color("Saindo... Até logo, agente.", YELLOW)
            break
        
        elif choice in ['1', '2', '3']:
            target = input("\n🔎 Nome do alvo/palavra-chave: ")
            if not target.strip():
                print_color("Erro: Alvo vazio!", RED)
            else:
                res = run_osint(int(choice), target)
                process_results(res)
        
        elif choice == '5':
            if os.path.exists("last_report.txt"):
                print_color("\n--- ÚLTIMO RELATÓRIO ---", BOLD)
                with open("last_report.txt", "r", encoding="utf-8") as f:
                    print(f.read())
            else:
                print_color("\n[!] Nenhum relatório encontrado.", RED)

        elif choice == '6':
            if os.path.exists("last_report.txt"):
                os.remove("last_report.txt")
                print_color("\n[!] Histórico apagado com sucesso.", GREEN)

        elif choice == '8':
            print_color("\nAJUDA:", BOLD)
            print("Use [1] para varredura total. O sistema utiliza scraping leve")
            print("e APIs oficiais para evitar bloqueios no Termux.")

        input("\nPressione [Enter] para voltar ao menu...")

if __name__ == "__main__":
    start()
