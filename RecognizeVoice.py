import speech_recognition as sr
from geopy.geocoders import Nominatim
import winsound

def zoom_in(q):
    place = q.replace("zoom in", "")
    print("Zooming In...")
    coordinates = get_coordinates(place)
    return "ZoomIn", coordinates

def zoom_out():
    return "ZoomOut", ""

def navigate_to(q):
    place = q.replace("navigate to", "")
    print("Navigating to...")
    coordinates = get_coordinates(place)
    return "Navigate", coordinates

def remove_markers(q):
    if not " all " in q:
        place = q.replace("remove markers", "")
        if len(place.replace(" ", ""))>0:
            coordinates = get_coordinates(place)
            return "Remove Markers", coordinates
    return "RemoveMarkers", ""

def add_mark(q):
    place = q.replace("add mark", "")
    coordinates = get_coordinates(place)
    return "AddMarker", coordinates

def handle_street_view():
    return "StreetView",""

def handle_terrain_view():
    return "TerrainView",""

def handle_satellite_view():
    return "SatelliteView",""

def handle_hide_layers():
    return "HideLayers",""

def get_coordinates(q):
    """Get coordinates from a query."""
    print("Getting Coordinates...")
    geolocator = Nominatim(user_agent="VoiceGIS")
    location = geolocator.geocode(q)
    print(location)
    if location != None:
        return [location.latitude, location.longitude]
    else:
        return ""

def classify_and_execute(q):
    """Classify the query and execute the corresponding action."""
    actions = {
        "zoom in": zoom_in,
        "zoom out": zoom_out,
        "navigate to": navigate_to,
        "remove markers": remove_markers,
        "add marker": add_mark,
        "street view": handle_street_view,
        "terrain view": handle_terrain_view,
        "satellite view": handle_satellite_view,
        "hide layers": handle_hide_layers,
    }
    
    for keyword, action in actions.items():
        if keyword in q.lower():
            try:
                result = action(q)
            except:
                result = action()
            return result
    else:
        print("No matching command found.")

def recognize():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        r.adjust_for_ambient_noise(source, 1)
        print("Say something!")
        winsound.Beep(450,250)
        try:
            audio = r.listen(source, phrase_time_limit=5)
            print("Processing...")
            query = r.recognize_google(audio, language='en-IN').lower()
            print("Processed audio!")
            print("Query: " + query)
            print("Executing Command...")
            command, coordinates = classify_and_execute(query)
            return command, coordinates
        except Exception as e:
            print(f"An error occurred: {e}")
            return "unknown_command", "unknown_coordinates"

# Example usage
#recognize()