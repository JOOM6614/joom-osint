def calculate_relevance(query, text):
    query_words = query.lower().split()
    text_lower = text.lower()
    score = 0
    
    for word in query_words:
        if word in text_lower:
            score += 25  # Peso por palavra-chave encontrada
            
    if score >= 50:
        return score, "🔥 ALTA"
    elif score >= 25:
        return score, "⚠️ MÉDIA"
    else:
        return score, "ℹ️ BAIXA"

def save_report(data):
    with open("last_report.txt", "w", encoding="utf-8") as f:
        for item in data:
            f.write(f"[{item['label']}] {item['title']}\nLink: {item.get('link', 'N/A')}\n\n")
