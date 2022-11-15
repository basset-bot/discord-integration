def load(result):
    return {
        'guild':result['guild'],
        'request':{
            'youtube_id':result['youtube_id']
        },
        'errors':[
            {
                'type':'client_error',
                'details':'Client is already playing. If you want for the client to wait for the current audio to finish, set wait_voice_client_stop to 1',
            }
        ]
    }, 400