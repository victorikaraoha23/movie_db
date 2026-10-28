import requests

from config import ombd_api_key

BASE_URL = "https://www.omdbapi.com/"
TIMEOUT = 10


class APIError(Exception):
    """Raised when a movie cannot be looked up on OMDb."""


def _clean(value):
    """Turn OMDb's "N/A" placeholders into None."""
    if not value or value == "N/A":
        return None
    return str(value).strip()


def _to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_movie(title):
    """Look a single movie up on OMDb by title and return it as a dict."""
    if not ombd_api_key:
        raise APIError("OMBD_API_KEY is missing from .env")

    try:
        response = requests.get(
            BASE_URL,
            params={"t": title, "apikey": ombd_api_key},
            timeout=TIMEOUT,
        )
    except requests.RequestException as error:
        # The exception text can contain the URL, and the URL contains the key.
        raise APIError("could not reach OMDb (network error)") from error

    if response.status_code in (401, 403):
        raise APIError("OMDb rejected the API key - check OMBD_API_KEY in .env")
    if not response.ok:
        raise APIError(f"OMDb returned HTTP {response.status_code}")

    try:
        data = response.json()
    except ValueError as error:
        raise APIError("OMDb returned an invalid response") from error

    if data.get("Response") == "False":
        raise APIError(data.get("Error", f"no results for '{title}'"))

    year = str(data.get("Year", ""))[:4]  # series come back as "2010-2015"
    rating = _to_float(data.get("imdbRating"))
    if not year.isdigit() or rating is None:
        raise APIError(f"OMDb returned incomplete data for '{title}'")

    return {
        "title": _clean(data.get("Title")) or title,
        "year": int(year),
        "rating": rating,
        "director": _clean(data.get("Director")),
        "genre": _clean(data.get("Genre")),
        "poster_url": _clean(data.get("Poster")),
    }
