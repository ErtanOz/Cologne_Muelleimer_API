# Cologne Waste Baskets API

Willkommen beim **Cologne Waste Baskets API**-Projekt! Diese API stellt Geokoordinaten und Informationen über Mülleimer in Köln bereit, basierend auf Daten von OpenStreetMap (OSM). Sie wurde mit Flask entwickelt und ist ideal für GIS-Enthusiasten, Entwickler oder Stadtplaner, die Zugang zu öffentlichen Müllkorb-Standorten suchen.

## Funktionen
- **Endpunkt**: `/api/waste_baskets` – Gibt eine Liste von Mülleimern in Köln mit ID, Breitengrad (`lat`), Längengrad (`lon`) und Beschreibung zurück.
- **Datenquelle**: OpenStreetMap (via Overpass API).
- **Format**: JSON-Antworten, leicht in andere Anwendungen integrierbar.

## Beispielantwort
```json
{
  "status": "success",
  "count": 3,
  "data": [
    {
      "id": 12345678,
      "lat": 50.937531,
      "lon": 6.960279,
      "description": "Müllkorb am Dom"
    },
    {
      "id": 12345679,
      "lat": 50.933333,
      "lon": 6.950000,
      "description": "Müllkorb am Rhein"
    }
  ]
}
```

## Installation und lokale Ausführung

### Voraussetzungen
- Python 3.11 oder höher
- Git

### Schritte
1. **Repository klonen**:
   ```bash
   git clone https://github.com/deinusername/cologne-waste-baskets-api.git
   cd cologne-waste-baskets-api
   ```

2. **Virtuelle Umgebung erstellen** (optional, aber empfohlen):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **API starten**:
   ```bash
   python app.py
   ```

5. **API testen**:
   - Öffne deinen Browser oder nutze ein Tool wie `curl`:
     ```bash
     curl http://localhost:5000/api/waste_baskets
     ```

## Deployment
Die API wurde so entwickelt, dass sie leicht auf Plattformen wie **PythonAnywhere** gehostet werden kann:
1. Erstelle ein Konto bei [PythonAnywhere](https://www.pythonanywhere.com/).
2. Lade `app.py` und `requirements.txt` hoch.
3. Konfiguriere die Webanwendung im Dashboard und starte sie.
4. Deine API ist dann unter `https://deinname.pythonanywhere.com/api/waste_baskets` erreichbar.

## Projektstruktur
```
cologne-waste-baskets-api/
├── app.py              # Haupt-Flask-Anwendung
├── requirements.txt    # Abhängigkeiten
└── README.md           # Projektbeschreibung
```

## Abhängigkeiten
- Flask
- Requests
- Gunicorn (für Produktion)

Siehe `requirements.txt` für genaue Versionen:
```
flask>=2.3.2
requests>=2.31.0
gunicorn>=20.1.0
```

## Einschränkungen
- Die Daten hängen von der Vollständigkeit der OpenStreetMap-Datenbank ab. Nicht alle Mülleimer in Köln sind möglicherweise erfasst.
- Bei hoher Last kann die Overpass API Anfragen begrenzen.

## Mitwirken
Beiträge sind willkommen! Wenn du Fehler findest oder neue Funktionen hinzufügen möchtest:
1. Forke das Repository.
2. Erstelle einen Branch (`git checkout -b feature/deine-idee`).
3. Committe deine Änderungen (`git commit -m "Beschreibung"`).
4. Pushe den Branch (`git push origin feature/deine-idee`).
5. Erstelle einen Pull Request.

## Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

## Kontakt
Hast du Fragen oder Vorschläge? Kontaktiere mich über [deine-email@example.com] oder öffne ein Issue hier auf GitHub.

---

### Anpassungen
- **Username**: Ersetze `deinusername` mit deinem GitHub-Benutzernamen.
- **Email**: Füge deine echte E-Mail-Adresse ein oder entferne den Kontaktabschnitt, wenn du ihn nicht brauchst.
- **Lizenz**: Ich habe die MIT-Lizenz vorgeschlagen, da sie einfach und weit verbreitet ist. Füge eine `LICENSE`-Datei hinzu, wenn du sie nutzen möchtest.

### Wie du das auf GitHub einrichtest
1. Erstelle ein neues Repository auf GitHub (z. B. `cologne-waste-baskets-api`).
2. Kopiere den obigen Text in eine Datei namens `README.md`.
3. Füge deine `app.py` und `requirements.txt` hinzu.
4. Pushe alles hoch:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/deinusername/cologne-waste-baskets-api.git
   git push -u origin main
   ```

Jetzt hast du ein professionelles GitHub-Projekt! Wenn du weitere Anpassungen möchtest (z. B. Badges, Screenshots), lass es mich wissen.
