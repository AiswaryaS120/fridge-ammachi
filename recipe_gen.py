# recipe_gen.py
# Handles recipe generation using a local GPT-2 model (no API key required).

import os
from transformers import pipeline

# Initialize the text generation pipeline with GPT-2
generator = pipeline('text-generation', model='gpt2')

def get_recipes(items: list[str]) -> str:
    """
    Generates recipe suggestions from a list of ingredients using a local GPT-2 model.

    Args:
        items (list[str]): A list of detected ingredients.

    Returns:
        str: A formatted string containing recipe suggestions.
    """
    if not items:
        return "No ingredients detected to generate recipes."

    # Create a comma-separated string of items for the prompt
    item_string = ", ".join(items)

    # Structured prompt for the model
    prompt = f"""
You are a helpful kitchen assistant. Based on these fridge ingredients: {item_string}, suggest 3 simple recipes. Assume basic staples like oil, salt, pepper, water, rice, flour are available.

Format each recipe exactly like this:

Recipe 1: Curd Rice - A simple and cooling dish
Steps: 1. Cook rice and let it cool. 2. Mix curd with rice. 3. Add salt and serve.

Recipe 2: Milk Shake - A refreshing drink
Steps: 1. Blend milk with ice. 2. Add sugar if needed. 3. Serve chilled.

Recipe 3: Juice Salad - A healthy mix
Steps: 1. Mix juice with vegetables. 2. Add salt and lemon. 3. Serve fresh.
"""

    try:
        print("Generating recipes with local GPT-2 model...")
        # Generate text using GPT-2
        outputs = generator(prompt, max_length=500, num_return_sequences=1, temperature=0.7, do_sample=True)
        generated_text = outputs[0]['generated_text']
        print("Recipes generated successfully.")

        # Extract the generated part after the prompt
        recipes = generated_text[len(prompt):].strip()
        return recipes if recipes else "Could not generate recipes. Try with different ingredients."

    except Exception as e:
        print(f"Error generating recipes: {e}")
        return f"Error: Could not generate recipes. Details: {str(e)}"

