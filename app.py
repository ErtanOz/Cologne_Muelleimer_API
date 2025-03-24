from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Overpass API URL
OVERPASS_URL = "http://overpass-api.de/api/interpreter"

# Funktion, um Mülleimer aus OSM für Köln abzufragen
def get_waste_baskets_in_cologne():
    # Overpass QL Abfrage für Mülleimer in Köln
    query = """
    [out:json];
    area["name"="Köln"]["admin_level"="6"]->.cologne;
    node["amenity"="waste_basket"](area.cologne);
    out body;
    """
    
    # Sende die Anfrage an die Overpass API
    response = requests.post(OVERPASS_URL, data={"data": query})
    
    if response.status_code == 200:
        data = response.json()
        # Extrahiere Geokoordinaten und erstelle Liste
        waste_baskets = [
            {
                "id": node["id"],
                "lat": node["lat"],
                "lon": node["lon"],
                "description": node.get("tags", {}).get("description", "Müllkorb")
            }
            for node in data["elements"]
        ]
        return waste_baskets
    else:
        return {"error": "Fehler beim Abrufen der Daten von Overpass API"}

# API-Endpunkt: Liste aller Mülleimer
@app.route('/api/waste_baskets', methods=['GET'])
def waste_baskets():
    try:
        waste_baskets = get_waste_baskets_in_cologne()
        return jsonify({
            "status": "success",
            "data": waste_baskets,
            "count": len(waste_baskets)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Startpunkt der Anwendung
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
