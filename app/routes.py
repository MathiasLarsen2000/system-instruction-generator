import os
import json
from flask import render_template, current_app as app, abort

# For nå, la oss legge ruter direkte under app-objektet
# Dette kan refaktoreres til Blueprints senere om nødvendig

# Konfigurasjon for data-mappen
DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data') # Peker til rotens data-mappe
SI_FOLDER = os.path.join(DATA_FOLDER, 'system_instructions')


@app.route('/')
def index():
    return render_template('index.html', title='Velkommen')


@app.route('/system_instructions')
def list_system_instructions():
    files = []
    if os.path.exists(SI_FOLDER) and os.path.isdir(SI_FOLDER):
        for f_name in os.listdir(SI_FOLDER):
            if f_name.endswith('.json'): # Vi forventer JSON-filer
                files.append({
                    'name': f_name,
                    'path': f_name # Enkelt filnavn for URLen
                })
    return render_template('list_system_instructions.html', files=files, title="Systeminstrukser")


@app.route('/system_instructions/<filename>')
def view_system_instruction(filename):
    file_path = os.path.join(SI_FOLDER, filename)
    if not os.path.exists(file_path) or not filename.endswith('.json'):
        abort(404)  # Fil ikke funnet

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
        # Konverter json-innhold til en pen streng for visning
        pretty_content = json.dumps(content, indent=2, ensure_ascii=False)
        return render_template('view_system_instruction.html', filename=filename, content=pretty_content, title=content.get("meta", {}).get("agentName", filename))
    except Exception as e:
        # Logg feilen og vis en feilmelding
        app.logger.error(f"Error reading or parsing {file_path}: {e}")
        abort(500) # Internal server error
