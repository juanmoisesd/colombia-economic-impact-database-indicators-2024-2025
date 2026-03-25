"""Base de Datos del Impacto Económico de Colombia 2024-2025: Indicadores Clave y Factores Influyentes.
DOI: https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025 | GitHub: https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Base de Datos del Impacto Económico de Colombia 2024-2025: Indicadores Clave y F. Zenodo. https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025'
def info():print(f"Dataset: Base de Datos del Impacto Económico de Colombia 2024-2025: Indicadores Clave y F\nDOI: https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025\nGitHub: https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025")