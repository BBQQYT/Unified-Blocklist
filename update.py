import re
import requests

# Список ваших источников
URLS = [
    # 1. Эталонный базовый hosts
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    
    # 2. Главный калибр: Чистые доменные версии HaGeZi (избавляет от ошибок парсинга)
    "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/domains/ultimate.txt",
    "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/domains/dyndns.txt",
    
    # 3. Закрываем дыру с куки-баннерами (Consent) на 100%
    "https://cdn.jsdelivr.net/gh/hagezi/dns-blocklists@latest/domains/anti-cookie.txt",
    
    # 4. Мощнейший агрегатор OISD Big (чистый доменный формат) — добьет остатки рекламы и метрик
    "https://big.oisd.nl/domaintext",
    
    # 5. Защита от трекинга и телеметрии от команды AdGuard
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt", # Tracking Protection
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",   # Базовый DNS
    
    # 6. Мобильная реклама и EasyList
    "https://raw.githubusercontent.com/x-o-r-r-o/Pi-Hole-Block-Lists/master/mobile-ads.txt",
    "https://easylist-downloads.adblockplus.org/advblock.txt"
]

def extract_domains(text):
    domains = set()
    
    # Более гибкие регулярные выражения
    hosts_re = re.compile(r'^(?:0\.0\.0\.0|127\.0\.0\.1)\s+([a-zA-Z0-9._-]+)')
    adblock_re = re.compile(r'^\|\|([a-zA-Z0-9._-]+)(?:\^|$)')
    domain_re = re.compile(r'^[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+$')

    for line in text.splitlines():
        line = line.strip()
        
        # Строгие исключения: пропускаем комментарии, правила исключений (@@) и косметику (##)
        if not line or line.startswith(('#', '!', '[', '::1', 'localhost', '@@', '#', '[', '/')):
            continue
            
        # Убираем Adblock-модификаторы в конце строки, если они есть (все что после $)
        if '$' in line and not line.startswith('||'):
            line = line.split('$')[0].strip()

        # 1. Формат hosts (0.0.0.0 domain.com)
        match = hosts_re.match(line)
        if match:
            domains.add(match.group(1).lower())
            continue
            
        # 2. Формат Adblock (||domain.com^...)
        match = adblock_re.match(line)
        if match:
            # Очищаем от возможных остатков модификаторов, если регулярка зацепила лишнее
            domain = match.group(1).split('^')[0].split('$')[0].lower()
            domains.add(domain)
            continue
        
        # 3. Чистый домен (встречается в OISD и доменах HaGeZi)
        if domain_re.match(line):
            domains.add(line.lower())
            
    return domains
def main():
    unique_domains = set()
    
    for url in URLS:
        print(f"Скачиваю: {url}")
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                domains = extract_domains(response.text)
                unique_domains.update(domains)
                print(f"Успешно: извлечено доменов — {len(domains)}")
            else:
                print(f"Ошибка скачивания {url}: статус {response.status_code}")
        except Exception as e:
            print(f"Ошибка при обработке {url}: {e}")

    # Исключаем локалхосты, если они проскочили
    ignored = {'localhost', 'localhost.localdomain', 'local'}
    unique_domains = {d for d in unique_domains if d not in ignored and '.' in d}

    sorted_domains = sorted(list(unique_domains))
    
    # 1. Сохраняем как чистый список доменов (для AdGuard Home, Mihomo, sing-box)
    with open("domains.txt", "w", encoding="utf-8") as f:
        for domain in sorted_domains:
            f.write(f"{domain}\n")
            
    # 2. Сохраняем как стандартный hosts-файл (для Pi-hole или системного hosts)
    with open("hosts.txt", "w", encoding="utf-8") as f:
        f.write("# Unified blocklist generated automatically\n")
        for domain in sorted_domains:
            f.write(f"0.0.0.0 {domain}\n")

    print(f"Готово! Всего уникальных доменов собрано: {len(sorted_domains)}")

if __name__ == "__main__":
    main()
