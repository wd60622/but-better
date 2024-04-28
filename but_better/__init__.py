from IPython import get_ipython
from IPython.display import display, YouTubeVideo
from functools import wraps
import warnings


def in_jupyter_notebook() -> bool:
    return get_ipython().__class__.__name__ == "ZMQInteractiveShell"


def but_better(video_id: str, **youtube_kwargs):
    """Wrap any function with this decorator to play a YouTube video while it runs.

    Args:
        video (str): The YouTube video ID.
        **youtube_kwargs: Additional keyword arguments to pass to `IPython.display.YouTubeVideo`.

    Returns:
        function: The decorated function.

    Examples:

        @but_better("z3SEc70eQYE")
        def phillies_hype_song():
            print("Let's go Phillies!")


        @but_better("mwgcK4E_RU0")
        def favorite_customer():
            print("You're my favorite customer!")

    """
    if not in_jupyter_notebook():
        warnings.warn("This decorator only works in Jupyter notebooks.", UserWarning)
        return lambda func: func

    if "allow_autoplay" not in youtube_kwargs:
        youtube_kwargs["allow_autoplay"] = True

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            display(YouTubeVideo(video_id, **youtube_kwargs))
            return func(*args, **kwargs)

        return wrapper

    return decorator


phillies_hype_song = but_better("z3SEc70eQYE")
favorite_customer = but_better("mwgcK4E_RU0")
fireplace = but_better("L_LUpnjgPso")
gasolina = but_better("3tw2P65wv5E")
