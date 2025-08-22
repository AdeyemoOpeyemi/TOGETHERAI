prompts = [
    {
        "name": "Lagos Fun Activities",
        "model": "google/gemma-3n-E4B-it",
        "messages": [
            {"role": "system", "content": "You are to provide the location of fun places"},
            {"role": "assistant", "content": "You are a travel expert"},
            {"role": "user", "content": "What are some fun things to do in Lagos?"}
        ]
    },
    {
        "name": "Explain Machine Learning",
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "messages": [
            {"role": "system", "content": "You should explain everything machine learning, emmerging technologies, improvements and limitations and ongoing research addressed at solving these limitations"},
            {"role": "assistant", "content": "You are a data science specialist"},
            {"role": "user", "content": "Explain the key concepts of the text delimited by triple backticks in simple terms. ```Machine learning is a field of artificial intelligence that enables computers to learn from data and make prediction.```"}
        ]
    }
]
