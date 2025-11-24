import asyncio
import re
import httpx
import requests
import random
from bs4 import BeautifulSoup

# Список популярных User-Agent'ов
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/537.36"
]

# Функция для получения случайного User-Agent
def get_random_user_agent():
    return random.choice(USER_AGENTS)

# Асинхронный парсер контента со страниц
async def fetch_page_content(url):
    headers = {
        "User-Agent": get_random_user_agent()
    }
    try:
        async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "Без названия"

            # Убираем ненужные теги
            for tag in soup(["script", "style", "footer", "header", "nav", "aside"]):
                tag.decompose()
            
            # Собираем текст из параграфов и заголовков
            paragraphs = soup.find_all(["p", "h1", "h2", "h3", "div", "span"])
            content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
            
            # Чистим от лишних пробелов и сносок
            content = re.sub(r"\n\s*\n", "\n", content)
            content = re.sub(r"\[.*?\]", "", content)
            
            return title, content.strip()[:5000]  # Ограничиваем длину текста
    except Exception as e:
        print(f"Ошибка при загрузке {url}: {e}")
        return None, None

# Асинхронный процессинг списка ссылок (многопоточно)
async def process_links(links):
    tasks = [fetch_page_content(link) for link in links]
    results = await asyncio.gather(*tasks)
    
    pages_content = {title: content for title, content in results if title and content}
    return pages_content

def is_url_accessible(url):
    try:
        response = requests.head(url, timeout=5)  # Проверка только доступности
        return response.status_code == 200
    except requests.RequestException:
        return False

# Функция парсинга ссылок из DuckDuckGo (POST-запрос)
def duckduckgo_search_links(query):
    url = "https://html.duckduckgo.com/html/"
    headers = {
        "User-Agent": get_random_user_agent()
    }
    data = {"q": query}
    
    try:
        response = requests.post(url, data=data, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    
    for a in soup.find_all("a", class_="result__a", href=True):
        link = a["href"]
        if not link.startswith("http"):
            link = "https:" + link  # Дополняем ссылки
        if is_url_accessible(link):  # Проверяем доступность
            links.append(link)
        if len(links) >= 3:  # Останавливаемся, как только собрали 5 ссылок
            break
    
    return links

# Основная функция поиска
async def main_search_query(query: str):
    top_links = duckduckgo_search_links(query)
    if not top_links:
        return f'По запросу "{query}" ничего не найдено.'

    all_content = await process_links(top_links)
    
    result_message_for_ai = (
        f'Тебе предоставлен следующий запрос: "{query}"\n'
        f"Проанализируй данные ниже, учитывая информацию из каждого источника, и сформулируй правильный ответ на запрос на том же языке, что и запрос:\n\n{all_content}"
    )
    return result_message_for_ai