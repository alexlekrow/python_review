## Running API with uvicron

The server can be ran from the API root directory with `uvicron main:app --reload`

## Managing Dev Dependencies

Cache API dependencies with `pip freeze > requirements.txt`.

These dependencies can be downloaded in other environments with
`pip install -r requirements.txt`
