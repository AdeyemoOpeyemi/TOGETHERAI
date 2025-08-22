from together import Together
import os
from dotenv import load_dotenv
from promptlist import prompts

def main():
    """
    Main function to run the Together AI chat application.
    """
    load_dotenv()
    api_key = os.getenv("api_key")

    if not api_key:
        print("Error: API key not found. Please create a .env file and add your api_key.")
        return

    client = Together(api_key=api_key)

    print("Please select a prompt to run:")
    for i, prompt_data in enumerate(prompts):
        print(f"{i + 1}. {prompt_data['name']}")

    try:
        choice = int(input("Enter the number of the prompt: ")) - 1
        if 0 <= choice < len(prompts):
            selected_prompt = prompts[choice]

            print(f"\nRunning prompt: {selected_prompt['name']}...")

            response = client.chat.completions.create(
                model=selected_prompt['model'],
                messages=selected_prompt['messages']
            )
            print("\nResponse:")
            print(response.choices[0].message.content)

        else:
            print("Invalid choice. Please select a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
