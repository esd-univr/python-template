import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Language(Enum):
    """
    Supported languages for the greeter class.
    """

    EN = "English"
    ES = "Spanish"
    FR = "French"
    DE = "German"
    IT = "Italian"
    PT = "Portuguese"
    ZH = "Chinese"
    JA = "Japanese"


def get_language(language: str | Language) -> Language:
    """
    Get the corresponding language code from the Language enum.

    :param language: The language code to look up.
    :return: The Language enum corresponding to the language code
    """
    if isinstance(language, Language):
        return language

    # find the language code in the Language enum
    for lang in Language:
        if lang.name == language.upper():
            return lang
    logging.error(f"Unsupported language code: {language}, defaulting to English.")
    return Language.EN


class Greeter:
    """
    A simple greeter class that supports multiple languages.
    """

    GREETINGS = {
        Language.EN: "Hello",
        Language.ES: "Hola",
        Language.FR: "Bonjour",
        Language.DE: "Hallo",
        Language.IT: "Ciao",
        Language.PT: "Olá",
        Language.ZH: "你好",
        Language.JA: "こんにちは",
    }

    def __init__(self, name: str, language: str | Language = Language.EN):
        """
        Initialize the Greeter with a name and an optional language.

        :param name: The name of the person to greet.
        :param language: The language code for the greeting.
        """
        self.name = name
        self.language = get_language(language)

    def greet(self) -> str:
        """
        Return a greeting message in the specified language.

        :return: A greeting string.
        """
        if self.language == Language.IT:
            return f"{self.GREETINGS[self.language]}, Mario Potato!"
        return f"{self.GREETINGS[self.language]}, {self.name}!"
