# Mastermind

Python Rest API using Flask framework for play Mastermind Game.

------
#### POST /game/new
- Create the new Game

Response:

Body:
```
{
    'status': true,
    'data': {
        'game_id': UUID,
    },
    'errors': null
}
```
------

#### POST /codemaker/generate_secret_code
- Generate a new secret code

Request:

Headers:
```
game_id: uuid
```
Body:
```
{
    'secret_code': [
        2, 0, 6, 4
    ]
}
```

Response:

Body:
```
	{
		'status': true,
		'data': null,
		'errors': null
	}
```

------

#### POST /codebreaker/guess
- Check if the code is the same of generated by the codemaker, otherwise return a feedback

Request:

Headers:
```
game_id: uuid
```

Body:
```
{
    'code': [
        2, 0, 6, 4
    ]
}
```

Response:

Body:
```
{
    'status': true,
    'data': {
        'feedback': [
            'black,
            'black',
            null,
            'white'
        ],
        'num_of_attempts': 1
    },
    'errors': null
}
```

------

#### GET /game/{game_id}/history
- Get an attempt history for a given Game

Response:

Body:
```
{
    'status': true,
    'data': {
        'num_of_attempts': 1,
        'attempts': [
            {
                'guessed': false,
                'secret_code': [],
                'attempt_code': [],
                'feedback': [],
                'occurred_on': '11/09/2019 00:00:00'
            }
        ]
    },
    'errors': null
}
```

## TODO
- Testing
- Use Domain Events
- Use ObjectIds in all object ids