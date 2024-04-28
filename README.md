# Your Code But Better

Wrapper for your code to make it nothing but better. 

## Installation

```bash
pip install but-better
```

## Usage

Pass the time during a long running function to watch a youtube video. 
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

Or try out some of the pre-defined videos.

```python
from but_better import (
    ten_hour_fireplace, 
    phillies_hype_song, 
    favorite_customer, 
    gasolina, 
)
```
