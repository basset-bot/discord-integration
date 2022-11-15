def load(result):
    return {
        'guild':result['guild'],
        'youtube_id':result['youtube_id'],
        'details':result['details']
    }, 200