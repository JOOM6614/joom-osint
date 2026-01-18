document.getElementById("searchInput").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        performSearch();
    }
});

async function performSearch() {
    const query = document.getElementById('searchInput').value;
    const resultsArea = document.getElementById('resultsArea');
    const loading = document.getElementById('loading');
    
    if (!query) return;

    // UI Feedback
    resultsArea.innerHTML = '';
    loading.classList.remove('hidden');
    
    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query })
        });
        
        const data = await response.json();
        
        loading.classList.add('hidden');
        
        if (data.length === 0) {
            resultsArea.innerHTML = '<div class="result-card"><p>NENHUM DADO ENCONTRADO NA REDE.</p></div>';
            return;
        }

        data.forEach(item => {
            const card = document.createElement('div');
            // Define cor baseada no score
            let scoreClass = item.score > 40 ? 'relevance-high' : 'relevance-med';
            
            card.innerHTML = `
                <a href="${item.link || '#'}" target="_blank" class="card-link">
                    <div class="result-card">
                        <div class="card-header">
                            <span>[SOURCE: ${item.source.toUpperCase()}]</span>
                            <span class="${scoreClass}">RELEVÂNCIA: ${item.label}</span>
                        </div>
                        <h3 class="card-title">${item.title}</h3>
                        <p class="card-snippet">${item.snippet || 'Acesso restrito ao resumo...'}</p>
                    </div>
                </a>
            `;
            resultsArea.appendChild(card);
        });

    } catch (error) {
        console.error('Falha na conexão:', error);
        loading.classList.add('hidden');
        resultsArea.innerHTML = '<div class="result-card" style="border-color:red"><p>ERRO DE CRIPTOGRAFIA DE DADOS (ERRO 500).</p></div>';
    }
}
