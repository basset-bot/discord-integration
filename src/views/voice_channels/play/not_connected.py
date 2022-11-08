def load(result):
    return {
        'guild':result['guild'],
        'errors':[
            {
                'type':'not_connected',
                'details':'Not connected to any voice channel in target guild',
            }
        ]
    }, 400