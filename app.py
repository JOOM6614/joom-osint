from flask import Flask, render_template, request, jsonify
from sources.wikipedia import fetch_wikipedia
from sources.news import fetch_news

app = Flask(__name__)

# Rota para carregar o site
@app.route('/')
def index():
    return render_template('index.html')

# API que o Javascript vai chamar
@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query vazia'}), 400

    results = []
    
    # Executa as buscas (aqui é o coração do OSINT)
    try:
        # Adiciona flag de fonte para o front saber qual ícone usar
        wiki_res = fetch_wikipedia(query)
        for w in wiki_res: w['type'] = 'wiki'
        
        news_res = fetch_news(query)
        for n in news_res: n['type'] = 'news'

        results.extend(wiki_res)
        results.extend(news_res)
        
        # Ordena por relevância (score)
        results = sorted(results, key=lambda x: x.get('score', 0), reverse=True)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
