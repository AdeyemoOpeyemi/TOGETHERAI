# Together AI API Scripts

This project contains a collection of Python scripts that demonstrate how to use the Together AI API to interact with various language models.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   - Create a file named `.env` in the root of the project.
   - Add your Together AI API key to the `.env` file as follows:
     ```
     api_key="YOUR_API_KEY"
     ```

## Usage

To run the main application, execute the following command:

```bash
python Together_app.py
```

This will prompt you to choose a prompt from a list, and then it will display the response from the language model.
