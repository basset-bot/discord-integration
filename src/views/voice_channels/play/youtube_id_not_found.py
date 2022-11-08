def load(result):
    return {
        'guild':result['guild'],
        'request':{
            'youtube_id':result['youtube_id']
        },
        'errors':[
            {
                'type':'youtube_id_not_found',
                'details':'youtube_id could not be found',
            }
        ]
    }, 404