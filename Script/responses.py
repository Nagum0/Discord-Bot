import random

def get_response(message: str) -> any:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Heeeeeeeeeeeeeeeeey'

    if p_message == '!help':
        return "`Astolfo can't help you :(`"
    
    if p_message == "fuck me astolfo":
        return "YAAAAAAAAAAAAAAAAAAAAAAAS QUEEEEEEEEEEEEEEEEN!"
    
    if p_message == "kawaii":
        return "image:C:\\Users\\csabe\\OneDrive\\Programming\\Discord Bot\\Pictures\\bot_pfp.jpg"
    
    if p_message == "astolfo how was your day?":
        return "Amazing! Master ****** me :)"