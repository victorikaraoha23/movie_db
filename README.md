# Movie DB

A small command-line movie collection manager. Movies are kept in `movies.json`
and can be exported to CSV, JSON or TXT.

## Setup

```bash
uv sync
```

Optional: to look movies up on [OMDb](https://www.omdbapi.com/) while adding
them, copy `.env.example` to `.env` and fill in your API key.

```bash
copy .env.example .env
```

## Usage

```bash
uv run main.py
```

```
1. Add a movie          - type the details, or fetch them from OMDb by title
2. View all movies      - list the collection
3. Search for a movie   - match on part of a title, or on a year
4. Delete a movie       - remove by title (asks first)
5. Export collections   - write CSV / JSON / TXT
6. Save & Exit          - write movies.json and quit
```

Your collection is saved to `movies.json` in the current directory, on "Save &
Exit" and on Ctrl+C.

## Tests

```bash
uv run python test_collection.py
uv run python test_file_handler.py
uv run python test_exporter.py
```

## Layout

| File | Purpose |
| --- | --- |
| `main.py` | entry point |
| `controller.py` | wires the menu, collection, storage and export together |
| `cli.py` | prompts and display helpers |
| `movie.py` | `Movie` model with validation |
| `collection.py` | `MovieCollection` add / remove / find / search / sort |
| `file_handler.py` | JSON save and load |
| `exporter.py` | CSV / JSON / TXT export |
| `api_client.py` | OMDb lookup |
| `config.py` | loads `OMBD_API_KEY` from `.env` |
