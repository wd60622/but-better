# Your Code But Better

Wrapper for your code to make it nothing but better. 

## Installation

```bash
pip install but-better
```

## Usage

Wrap your function with `but_better` and pass the youtube video id as the argument. 

```python 
from your_module import your_function

from but_better import but_better

# Last bit of any youtube video url
youtube_id = "dQw4w9WgXcQ"
your_function_but_better = but_better(youtube_id)(your_function)
```

Use the wrapped function as you would normally. 

```python
your_function_but_better()
```


