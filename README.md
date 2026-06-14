<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=200&section=header&text=Unified%20Blocklist%20%F0%9F%9B%A1%EF%B8%8F&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35" />
  <h1>🛡️ Сводный Блоклист Доменов и Hosts</h1>
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=20&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=700&lines=%E2%9A%A1+%D0%90%D0%B2%D1%82%D0%BE%D0%BE%D0%B1%D0%BD%D0%BE%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5+%D1%80%D0%B0%D0%B7+%D0%B2+%D0%B4%D0%B5%D0%BD%D1%8C%3B%F0%9F%9B%A1%EF%B8%8F+6+%D0%BC%D0%BE%D1%89%D0%BD%D1%8B%D1%85+%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2%3B%F0%9F%93%A6+%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D1%8B%3A+domains.txt+%7C+hosts.txt" />
  <p>
    <img src="https://img.shields.io/github/stars/BBQQYT/Unified-Blocklist?style=for-the-badge&color=ff6b6b" />
    <img src="https://img.shields.io/github/last-commit/BBQQYT/Unified-Blocklist?style=for-the-badge&color=6366f1" />
    <img src="https://img.shields.io/github/license/BBQQYT/Unified-Blocklist?style=for-the-badge&color=10b981" />
  </p>
</div>

---

## 🚀 О проекте

**Unified Blocklist** — это автоматизированный инструмент для сборки единого, очищенного от дубликатов списка блокировки нежелательных доменов, трекеров и рекламы. 

Скрипт на Python запускается **каждые сутки в 03:00 UTC** через GitHub Actions, скачивает самые актуальные списки от ведущих ИБ-сообществ, нормализует их форматы, удаляет мусор и коммитит результат обратно в репозиторий.

---

## ✨ Возможности

- 🔄 **Полный автомат:** Списки всегда актуальны без вашего участия.
- 🧹 **Умная фильтрация:** Очистка от служебных записей, комментариев и `localhost`.
- 🗜️ **Дедупликация:** Объединяет сотни тысяч строк в единый уникальный массив.
- 📦 **Два формата на выбор:**
  - `domains.txt` — только чистые домены (идеально для AdGuard Home, NextDNS, sing-box, Mihomo).
  - `hosts.txt` — классический формат `0.0.0.0 domain.com` (для Pi-hole или системного файла hosts).

---

## 📋 Использование (Raw ссылки)

Просто добавьте одну из этих ссылок в ваш блокировщик рекламы или DNS-сервер:

* **Список доменов (Adblock/sing-box):** `https://raw.githubusercontent.com/BBQQYT/Unified-Blocklist/main/domains.txt`
* **Формат Hosts (Pi-hole/Система):** `https://raw.githubusercontent.com/BBQQYT/Unified-Blocklist/main/hosts.txt`

---

## 🛠️ Стек технологий

- **Автоматизация:** GitHub Actions (Cron)
- **Язык обработки:** Python 3.x
- **Парсинг данных:** Regular Expressions (Регулярные выражения)

---

## 🙏 Благодарности и Источники

Этот проект существует исключительно благодаря титаническому труду создателей оригинальных списков блокировки. Огромное спасибо авторам и сообществам, чьи данные используются в этом сборщике:

- 🛡️ **[StevenBlack/hosts](https://github.com/StevenBlack/hosts)** — за эталонный и самый стабильный hosts-список.
- 🕸️ **[AdGuard Team](https://github.com/AdGuardTeam/AdGuardSDNSFilter)** — за мощный фильтр AdGuard DNS.
- 📱 **[x-o-r-r-o](https://github.com/x-o-r-r-o/Pi-Hole-Block-Lists)** — за специализированный список блокировки мобильной рекламы.
- 💎 **[HaGeZi](https://github.com/hagezi/dns-blocklists)** — за ультимативные листы `ultimate` и `dyndns` (лучшая защита от трекеров и скама).
- 🧬 **[EasyList / Adblock Plus](https://easylist.to/)** — за классический и проверенный временем `advblock.txt`.

---

## 📄 Лицензия

Скрипт сборщика распространяется под лицензией MIT. Права на сами блокируемые домены целиком и полностью принадлежат авторам оригинальных списков.
