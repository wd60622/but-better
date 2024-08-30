# Your Code But Better

[![PyPI version](https://badge.fury.io/py/but-better.svg)](https://badge.fury.io/py/but-better)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Wrapper for your code to make it nothing but better. 

## Installation

```bash
pip install but-better
```

## Usage

Pass the time during a long running function by watching a YouTube video. 
Pass YouTube video id as the argument to `but_better` and use it as a decorator.

```python
from but_better import but_better

my_favorite_youtube_id: str = ...
youtube_video = but_better(my_favorite_youtube_id)

from their_module import their_function 

their_function_but_better = youtube_video(their_function)
```

If you are writing the function, use the decorator syntax:

```python
@youtube_video
def my_function():
    # Your code here
    pass
```

Struggling to find something to kill the time? Try out a pre-defined video:

```python
from but_better import (
    elevator,
    favorite_customer, 
    gasolina, 
    gotcha,
    phillies_hype_song, 
    ten_hour_fireplace, 
)
```
