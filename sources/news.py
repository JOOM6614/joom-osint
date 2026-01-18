import requests
from bs4 import BeautifulSoup
from utils.normalizer import calculate_relevance

def fetch_news(query):
    # URL ajustada para o Google News RSS em Pt-BR
    url = f"https://news.google.com/rss/search?q={query}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    results = []
    
    try:
        response = requests.get(url, timeout=10)
        
        # Tenta parser XML primeiro, fallback para HTML se falhar
        try:
            soup = BeautifulSoup(response.content, 'xml')
        except:
            soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('item')
        
        # Limita a 10 resultados para não poluir o terminal
        for item in items[:10]:
            title = item.title.text if item.title else "Sem título"
            link = item.link.text if item.link else "N/A"
            
            # Tenta pegar descrição, limpando HTML básico se houver
            raw_desc = item.description.text if item.description else ""
            clean_desc = BeautifulSoup(raw_desc, "html.parser").get_text()
            
            # O erro anterior estava aqui: garantindo que a indentação esteja alinhada
            # Somamos título + descrição para calcular a relevância
            full_text = f"{title} {clean_desc}"
            score, label = calculate_relevance(query, full_text)
            
            results.append({
                'title': title,
                'link': link,
                'snippet': clean_desc, # Adicionado para usar no display
                'score': score,
                'label': label,
                'source': 'Google News'
            })
            
    except Exception as e:
        print(f"Erro ao buscar notícias: {e}")
    
    return results
