# ITW601 PMS

## Installation Instructions

### Node.js Dependencies

To install all required Node.js dependencies for the client folder:

1. Navigate to the client directory:

```bash
cd client
```

2. Install dependencies using npm:

```bash
npm install
```

This will install all the dependencies listed in the `package.json` file.

### Python/Flask Setup

To set up the Python virtual environment and install Flask:

1. Navigate to the server directory:

```bash
cd server
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

-   On macOS/Linux:

```bash
source venv/bin/activate
```

-   On Windows:

```bash
.\venv\Scripts\activate
```

4. Install all Python dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

5. To deactivate the virtual environment when you're done:

```bash
deactivate
```

Note: Make sure you have Python 3.x installed on your system before creating the virtual environment.
