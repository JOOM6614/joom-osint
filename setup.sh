#!/bin/bash

# Cores para o terminal
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RESET='\033[0m'

echo -e "${CYAN}[*] Iniciando configuração do JOOM CONSULTAS...${RESET}"

# Verifica se está no Termux para usar pkg, senão tenta apt (Linux padrão)
if command -v pkg &> /dev/null; then
    echo -e "${GREEN}[+] Ambiente Termux detectado.${RESET}"
    echo -e "${CYAN}[*] Atualizando repositórios...${RESET}"
    pkg update -y && pkg upgrade -y
    
    echo -e "${CYAN}[*] Instalando Python e Git...${RESET}"
    pkg install python git libxml2 libxslt -y
else
    echo -e "${GREEN}[+] Ambiente Linux detectado.${RESET}"
    # Assume apt (Debian/Ubuntu/Kali)
    sudo apt update
    sudo apt install python3 python3-pip -y
fi

echo -e "${CYAN}[*] Instalando dependências Python (requests, bs4, lxml)...${RESET}"
pip install requests beautifulsoup4 lxml

echo -e "${CYAN}[*] Verificando estrutura de pastas...${RESET}"
mkdir -p sources utils

echo -e "${GREEN}=========================================="
echo -e "   INSTALAÇÃO CONCLUÍDA COM SUCESSO! 🚀"
echo -e "   Para iniciar, digite: python main.py"
echo -e "==========================================${RESET}"
