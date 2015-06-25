import requests
import re
import json

def search(arg):

# arg contains a dict with a single key:value
# term is PO accession term and is mandatory

    # Validate against a regular expression
    term = arg['term']
    #term = term.upper()
    p = re.compile('[A-Z,a-z,0-9]', re.IGNORECASE)
    if not p.search(term):
        raise Exception('Invalid search term')

    r = requests.get('http://iplant.plantontology.org/services/PO_web_service.php?request_type=term_search&search_value=' + term + '&inc_synonyms&branch_filter=plant_anatomy&max=20&prioritize_exact_match')

    # Raise exception on bad HTTP status
    r.raise_for_status()
    try:
       return r.headers['Content-Type'], r.content
    except ValueError:
        raise Exception('Undefined error: '.format(response.text))

def list(arg):
    raise Exception('Not implemented yet')
