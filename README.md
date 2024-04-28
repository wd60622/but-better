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


from my_module import my_function 

my_function_but_better = youtube_video(my_function)
```

If you are writing the function, you can use the decorator syntax.

```python
@youtube_video
def your_function():
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
