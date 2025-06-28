# Prompt Engineering Workbench

En webapplikasjon for å skrive, teste, administrere og sammenligne prompts og systeminstrukser for AI-modeller.

## Oppsett og Kjøring (Foreløpig)

1.  **Installer avhengigheter:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Kjør Flask-applikasjonen:**
    ```bash
    export FLASK_APP=main.py
    # eller set FLASK_APP=main.py på Windows
    export FLASK_ENV=development # For utviklingsmodus
    flask run
    ```
    (Merk: `main.py` vil bli opprettet snart)

## Prosjektstruktur

*   `app/`: Kjerneapplikasjonslogikk.
    *   `__init__.py`: Initialiserer Flask-applikasjonen.
    *   `routes.py`: Definerer URL-ruter.
    *   `static/`: Inneholder statiske filer (CSS, JavaScript, bilder).
    *   `templates/`: Inneholder HTML-maler (Jinja2).
*   `data/`: For brukergenererte data.
    *   `system_instructions/`: Lagring for systeminstruksjonsfiler (f.eks. JSON).
    *   `prompts/`: Lagring for promptfiler.
    *   `outputs/`: Lagring for AI-genererte outputs.
*   `tests/`: For enhetstester og integrasjonstester.
*   `main.py`: Inngangspunkt for å kjøre Flask-applikasjonen.
*   `requirements.txt`: Liste over Python-avhengigheter.
*   `.gitignore`: Spesifiserer filer som skal ignoreres av Git.

## Teknologistack

*   **Backend:** Python, Flask
*   **Frontend:** HTML, CSS, JavaScript (Vanilla)
*   **Datalagring:** Filbasert (primært JSON)

## Bidra

(Detaljer kommer senere)
