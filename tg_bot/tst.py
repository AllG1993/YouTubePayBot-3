import os
import sys
from pathlib import Path
import google_sheets_api

p = Path(Path.cwd().parent, 'ytpb-3-test-creds.json')

print(os.path.abspath('..'))
print(os.path.dirname(os.path.abspath('')) + '/ytpb-3-test-creds.json')
