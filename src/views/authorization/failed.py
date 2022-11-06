def load(result={}):
    return {
        'errors':[
            {
                'type':'authentication',
                'details':'wrong integration token'    
            }
        ]
    }, 401