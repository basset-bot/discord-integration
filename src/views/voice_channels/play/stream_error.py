def load(result):
    return {
        'guild':result['guild'],
        'request':{
            'youtube_id':result['youtube_id']
        },
        'errors':[
            {
                'type':'stream_error',
                'details':'Error ocurred when fetching stream',
                'stage':result['stage'],
                'exception':result['exception']
            }
        ]
    }, 404