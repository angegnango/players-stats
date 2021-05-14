from api.models.player import Player

def all():

    """ Fetch all players
    return (list) : list of players
    """

    return [ player for player in Player.objects]

def create(payload):

    """ Create player
    param (dict) : player dict object
    return (dict) player created 
    """

    player = Player(firstname = payload['firstname'],lastname=payload['lastname'],email = payload['email'], nickname = payload['nickname'],fornite_nickname = payload['fornite_nickname'],clash_royal_player_tag = payload['clash_royal_player_tag'])
    
    try:
        player.save()
    except Exception as error:
        return error
    return player

def retrieve_player(nickname):

    """ Retrieve player by nickname 
    param (str) : BetOnYou player nickname
    return (object | None) 
    """

    player = Player.objects.get_or_404(nickname=nickname)
    if player:
        return player
    else:
        return None

def update(nickname, payload):

    """ Update player information 
    param1 (str) : BetOnYou player nickname
    param2 (dict) : dict object of information we want to update 
    return (object | str) 
    """

    player = Player.objects.get_or_404(nickname=nickname)

    if player:
        player.update(firstname = payload['firstname'],lastname=payload['lastname'],email = payload['email'], nickname = payload['nickname'],fornite_nickname = payload['fornite_nickname'],clash_royal_player_tag = payload['clash_royal_player_tag'])
        return player
    else:
        return 'Player not found'

def store_stats(nickname, payload):

    """ Store players stats from external API 
    param1 (str) : BetOnYou player nickname 
    param2 (object) : stats object retrieve from feature service 
    """

    player = Player.objects.get_or_404(nickname=nickname)

    if player:
        player.update(stats = payload)
    else:
        return 'Player not found'


def destroy(nickname):

    """ Delete player 
    param (str) : BetOnYou player nickname
    """

    player = Player.objects.get_or_404(nickname=nickname)
    player.delete()