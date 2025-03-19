from googletrans import Translator
from datetime import datetime

def greet_in_language():
    """
    Prompts the user to enter a language code, translates the phrase "Hello World" 
    into the specified language, and prints the translated text.
    Additionally, the user is given the option to save the translation to a file.
    """
    lan = input("Enter your language code: ").strip().lower()
    translator = Translator()
    greeting = "Hello World"
    
    try:
        translated = translator.translate(greeting, dest=lan)
        print(f"Translated Text: {translated.text}")
        
        save_option = input("Would you like to save this translation? (yes/no): ").strip().lower()
        if save_option in ["yes", "y"]:
            save_translation(greeting, translated.text, lan)
            print("Translation saved successfully!")
        
    except Exception as e:
        print("Language not supported or an error occurred:", e)

def save_translation(original, translated, language):
    """Saves the translation to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("translations.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\nOriginal: {original}\nTranslated: {translated} ({language})")

if __name__ == "__main__":
    greet_in_language()
