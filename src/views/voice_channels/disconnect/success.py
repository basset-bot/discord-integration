def load(result):
    return {
        'guild':result['guild'],
        'channel':result['disconnected_channel']
    }, 200