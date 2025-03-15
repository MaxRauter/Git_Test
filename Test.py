from googletrans import Translator

def greet_in_language():
    """
    Prompts the user to enter a language code, translates the phrase "Hello World" 
    into the specified language, and prints the translated text.
    Uses the `googletrans` library to perform the translation. If the translation 
    fails or the language is not supported, an error message is printed.
    Raises:
        Exception: If the translation fails or the language is not supported.
    """
    lan = input("Enter your language: ").strip().lower()
    translator = Translator()
    greeting = "Hello World"
    
    try:
        translated = translator.translate(greeting, dest=lan)
        print(translated.text)
    except Exception as e:
        print("Language not supported or an error occurred:", e)

greet_in_language()