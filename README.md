# OPEN InfoEducatie 2023

Un proiect Open-Source, self-hostable pentru a face web scraping pe live-uri de pe YouTube cu camere de supraveghere a traficului.

De asemenea functioneaza si ca un REST API pentru a permite oricui sa acceseze datele salvate in baza de date SQLITE din fisierul `database.db`

# Cum functioneaza?

Exista doua parti, scraper-ul si API-ul.

## Scraper

Cat timp fisierul `main.py` ruleaza, datele despre trafic se actualizeaza o data la aproximativ `2 minute` valoare ce, desigur poate fi midificata.

Scraper-ul porneste cate o instanta headless de Selenium pentru fiecare locatie adaugata in fisierul `config.json`. Acesta este un exemplu de config:

```json
{
    "locations": [
        {
            "id": "piata_unirii",
            "name": "Piata Unirii",
            "latitude": 44.4271836,
            "longitude": 26.1010159,
            "yt_live": "https://www.youtube.com/watch?v=rs2be3mqryo&ab_channel=ULTRAVISIONCONSULT"
        },
        {
            "id": "oxford_martin_school",
            "name": "Oxford Martin School",
            "latitude": 51.754939,
            "longitude": -1.254351,
            "yt_live": "https://www.youtube.com/watch?v=St7aTfoIdYQ&ab_channel=OxfordMartinSchool"
        }
    ]
}
```

### Cum se calculeaza traficul?

Folosind Selenium fac 5 screenshot-uri (cu interval de 5 secunde intre ele), o data la 2 minute pentru fiecare locatie. Dupa care utilizez **OpenCV** in combinate cu **cvlib** pentru object detection. Se numara cate vehicule apar in fiecare din cele 5 cadre si se face media aritmetica intre aceste valori, rezultatul este `scorul traficului`.

### Stocarea in baza de date

Pentru stocarea persistenta a datelor folosesc o baza de date SQLITE cu un singur tabel: `locations`.

Cu urmatoarea schema:

```SQL
CREATE TABLE IF NOT EXISTS locations (
       id text PRIMARY KEY NOT NULL UNIQUE,
       name text,
       traffic real,
       timestamp int,
       longitude real,
       latitude real,
       link text
   )
```

## REST API

API-ul este facut folosing Flask, si prezinta un singur GET endpoint `/get_locations` care returneaza in format json toate randurile din tabelul `locations` din baza de date.

Pentru a porni serverul API trebuie sa rulam fisierul `server.py`
