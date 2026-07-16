from flask import Flask
from app import app

# Vercel uses the WSGI entrypoint from the imported Flask app.
# The Python runtime should detect `app` automatically.

# If needed, expose the app directly.

if __name__ == '__main__':
    app.run(debug=True)
