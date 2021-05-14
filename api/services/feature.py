import requests
from urllib.parse import urlparse
from api.services.crud import retrieve_player

def get_stat_from_fornite(nickname):

    """ Get player stat
    param (str): nickname
    return (dict |string) external api response
    """
    
    url = 'https://fortnite-api.com/v1/stats/br/v2?name='+nickname
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    if response.status_code == 403:
        return response.text

    if response.status_code == 404:
        return response.text
   

def get_stat_from_clash_royale(player_tag:str):

    """ Get player tag statistic 
    param (str): player tag
    return (dict |string) external api response
    """
    
    # encode the # from the player tag
    player_tag = requests.utils.quote(player_tag)

    # clash royale url endpoint that can be save on environment variable
    url = 'https://api.clashroyale.com/v1/players/'+player_tag
    
    # retrieve access token that can also be save on environment variable
    access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRkMjk4ZDk2LWY2ZTktNDRjNS04ODE5LTY3ZDFhZjZhNjY4MCIsImlhdCI6MTYyMDg5Mzk4NSwic3ViIjoiZGV2ZWxvcGVyL2Q0N2Y0ODc0LWNjNTQtOTI1ZC0zOWJiLWE1ZDZiOTQwMmZhOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI3Ny4xOTUuNTEuODIiXSwidHlwZSI6ImNsaWVudCJ9XX0.dgFl5YrWmaI-YO-cVhy8ZoxV7d3RlUW_yHyUMOwAQSO8PPnraYyQ8JdH2T01ZRnyW9Rr1VH4y52DAdXYQqOzqg'
    
    # response object
    response = requests.get(url, headers={'Content-Type':'application/json','Authorization': 'Bearer '+access_token})

    if response.status_code == 200:
        return response.json()

    if response.status_code == 404:
        return 'PlayerTag {} does not found '.format(nickname)

    if response.status_code == 403:
        return response.text
    else:
        return 'Something wrong (Status Code :'+response.status_code+')'


def retrieve_player_stat(nickname):

    """ Retrieve player stat from external API 
    fornite and clash royale
    param (str) : BetOnYou player nickname
    return (object) : player stats object
    """
    
    stats = [] 
    player = retrieve_player(nickname)

    if player == None:
        return 'nickname not found :'+nickname
    else:

        fornite_nickname = player['fornite_nickname']
        player_tag = player['clash_royal_player_tag']

        fornite_stats = { 'game': 'fornite', 'stats': get_stat_from_fornite(nickname) }
        stats.append(fornite_stats)
        clash_royal_stats = { 'game': 'clash_royal', 'stats': get_stat_from_clash_royale(player_tag) }
        stats.append(clash_royal_stats)
        
        return stats