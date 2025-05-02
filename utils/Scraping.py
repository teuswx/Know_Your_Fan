from urllib.parse import urlparse

redesSociais = {
    'x': {
        'mateushp4': True,
        'lucas01': True,
        'Tiago89': None
    },
    'twitch': {
        'mateushp02': None,
        'lucas01': True,
        'Tiago89': None
    }
}

def verifica_interacao(x, twitch):
 
    url_x = urlparse(x)
    url_twitch = urlparse(twitch)
    tag_name_x = url_x.path.replace('/', '') 
    tag_name_twitch = url_twitch.path.replace('/', '')
    print(tag_name_x)

    if tag_name_x in redesSociais['x'] and tag_name_twitch in redesSociais['twitch']:
        if redesSociais['x'][tag_name_x] and redesSociais['twitch'][tag_name_twitch]:
            return 'Este usuário segue a Furia no X e na Twitch'
        elif redesSociais['x'][tag_name_x] and not redesSociais['twitch'][tag_name_twitch]:
            return 'Este usuário segue a Furia no X, mas não segue na Twitch'
        elif not redesSociais['x'][tag_name_x] and redesSociais['twitch'][tag_name_twitch]:
            return 'Este usuário não segue a Furia no X, mas segue na Twitch'
        else:
            return 'Este usuário não segue a Furia no X e na Twitch'
    else:
        return 'Usuário não encontrado em uma ou ambas as redes sociais'