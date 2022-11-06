from src.views.partials.no_channel_error import load as no_channel_error

def load(result):
    return {
        'request':{
            'channel':result['channel']
        },
        'errors':[
            no_channel_error()
        ]
    }, 404