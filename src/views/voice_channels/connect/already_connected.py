def load(result):
    return {
        'channel':result['channel'],
        'errors':[
            {
                'type':'already_connected',
                'details':'Already connected to a voice channel in target guild',
                'connected_channel':result['connected_channel']
            }
        ]
    }, 400