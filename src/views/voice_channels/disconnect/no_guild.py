from src.views.partials.no_guild_error import load as no_guild_error

def load(result):
    return {
        'request':{
            'guild':result['guild']
        },
        'errors':[
            no_guild_error()
        ]
    }, 404