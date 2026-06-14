import re
import requests

# Ссылки переведены на прямые репозитории + исправлен OISD
URLS = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/ultimate.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/dyndns.txt",
    "https://big.oisd.nl", 
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt", 
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",   
    "https://raw.githubusercontent.com/x-o-r-r-o/Pi-Hole-Block-Lists/master/mobile-ads.txt",
    
    # Исправленные чистые DNS-версии для Рунета от AdGuard
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/adservers.txt",
    "https://raw.githubusercontent.com/AdguardTeam/AdguardFilters/master/CyrillicFilters/RussianFilter/sections/spyware.txt"
]

def extract_domains(text):
    domains = set()
    
    hosts_re = re.compile(r'^(?:0\.0\.0\.0|127\.0\.0\.1)\s+([a-zA-Z0-9._-]+)')
    adblock_re = re.compile(r'^\|\|([a-zA-Z0-9._-]+)(?:\^|$)')
    domain_re = re.compile(r'^[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+$')

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(('#', '!', '[', '::1', 'localhost', '@@', '/', '||#')):
            continue
        
        if '$' in line and not line.startswith('||'):
            line = line.split('$')[0].strip()

        # 1. Формат hosts
        match = hosts_re.match(line)
        if match:
            domains.add(match.group(1).lower())
            continue
            
        # 2. Формат Adblock
        match = adblock_re.match(line)
        if match:
            domain = match.group(1).split('^')[0].split('$')[0].lower()
            domains.add(domain)
            continue
        
        # 3. Чистый домен (для списков OISD и HaGeZi-domains)
        if domain_re.match(line):
            domains.add(line.lower())
            
    return domains

def main():
    unique_domains = set()
    
    # Добавляем заголовки, чтобы прикинуться обычным браузером
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    for url in URLS:
        print(f"Скачиваю: {url}")
        try:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code == 200:
                domains = extract_domains(response.text)
                unique_domains.update(domains)
                print(f"Успешно: извлечено доменов — {len(domains)}")
            else:
                print(f"Ошибка скачивания {url}: статус {response.status_code}")
        except Exception as e:
            print(f"Ошибка при обработке {url}: {e}")

    ignored = {'localhost', 'localhost.localdomain', 'local'}
    unique_domains = {d for d in unique_domains if d not in ignored and '.' in d}

    sorted_domains = sorted(list(unique_domains))
    
    with open("domains.txt", "w", encoding="utf-8") as f:
        for domain in sorted_domains:
            f.write(f"{domain}\n")
            
    with open("hosts.txt", "w", encoding="utf-8") as f:
        f.write("# Unified blocklist generated automatically\n")
        for domain in sorted_domains:
            f.write(f"0.0.0.0 {domain}\n")

    print(f"Готово! Всего уникальных доменов собрано: {len(sorted_domains)}")

if __name__ == "__main__":
    main()
