# recipe_gen.py
# Handles communication with the Google Gemini API to generate recipes.

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()

def get_recipes(items: list[str]) -> str:
    """
    Generates recipe suggestions from a list of ingredients using the Gemini API.

    Args:
        items (list[str]): A list of detected ingredients.

    Returns:
        str: A formatted string containing recipe suggestions, or an error message.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: Google Gemini API key not found. Please set it in your .env file."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Create a comma-separated string of items for the prompt
        item_string = ", ".join(items)

        # A structured prompt to get reliable, well-foarmatted output from the AI
        prompt = f"""
        You are a helpful and creative kitchen assistant.
        Based on the following list of ingredients found in a fridge, please suggest the top 3 best recipes.

        Ingredients available: {item_string}

        For each recipe, please provide the following information in this exact format:

        **Recipe Title:** [Name of the Recipe]
        **Description:** [A short, appealing one-line description of the dish.]
        **Method:**
        1. [First simple step]
        2. [Second simple step]
        3. [And so on...]

        ---

        Please ensure the recipes primarily use the ingredients provided. You can assume basic pantry staples like oil, salt, pepper, and water are available. Do not suggest recipes with many unavailable ingredients.
        """

        print("Sending prompt to Gemini API...")
        response = model.generate_content(prompt)
        print("Received response from Gemini API.")
        
        return response.text

    except Exception as e:
        print(f"An error occurred while calling the Gemini API: {e}")
        print(f"Error type: {type(e).__name__}")
        print(f"Error details: {str(e)}")
        return f"Error: Could not retrieve recipes at this time. The service might be unavailable or the API key is invalid. Details: {str(e)}"

