import requests
from utils.normalizer import calculate_relevance

def fetch_wikipedia(query):
    url = "https://pt.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }
    results = []
    
    try:
        response = requests.get(url, params=params, timeout=10).json()
        search_results = response.get('query', {}).get('search', [])
        
        for item in search_results:
            title = item['title']
            snippet = item['snippet'].replace('<span class="searchmatch">', '').replace('</span>', '')
            score, label = calculate_relevance(query, title + " " + snippet)
            
            results.append({
                'title': title,
                'snippet': snippet,
                'score': score,
                'label': label,
                'source': 'Wikipedia'
            })
    except Exception as e:
        print(f"Erro Wiki: {e}")
        
    return results
