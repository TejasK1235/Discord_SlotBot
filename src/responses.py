from random import choice,randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered=='':
        return 'You are awfully silent huh'
    elif 'hello' in lowered or 'hi' in lowered:
        return 'Hello I am SlotBot'
    elif 'how are you' in lowered:
        return 'Great, Thanks'
    elif 'bye' in lowered:
        return 'Thanks for playing'
    elif 'goku' in lowered and 'saitama' in lowered:
        return 'Goku is way stronger'
    else:
        return choice([
            "What are you talking about?",
            "Can you rephrase that?",
            "I do not understand"
        ])
    