from IPython import get_ipython
from IPython.display import display, YouTubeVideo
from IPython.core.display import Javascript
from functools import wraps
from urllib import parse
import warnings


def parse_youtube_url(url: str) -> str:
    """Get the YouTube video ID from a URL.

    Reference: https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python

    Args:
        url (str): The YouTube URL.

    Returns:
        str: The YouTube video ID.

    Examples:
        Get the video ID from a URL.

        parse_youtube_url("https://www.youtube.com/watch?v=z3SEc70eQYE")
        # "z3SEc70eQYE"

    """
    url_data = parse.urlparse(url)
    query = parse.parse_qs(url_data.query)
    return query["v"][0]


def in_jupyter_notebook() -> bool:
    return get_ipython().__class__.__name__ == "ZMQInteractiveShell"


def but_better(video_id: str, stop_on_completion: bool = True, **youtube_kwargs):
    """Wrap any function with this decorator to play a YouTube video while it runs.

    Args:
        video_id (str): The YouTube video ID.
        stop_on_completion (bool): Whether to stop the video when the function completes.
        **youtube_kwargs: Additional keyword arguments to pass to `IPython.display.YouTubeVideo`.

    Returns:
        function: The decorated function that plays the YouTube video
            while the original function runs.

    Examples:
        Use as a decorator to play a YouTube video while a function runs.

        ```python
        @but_better("z3SEc70eQYE")
        def phillies_hype_song():
            print("Let's go Phillies!")
        ```

        Return a new function from an existing function.

        ```python
        from my_module import my_function

        my_function_but_better = but_better("z3SEc70eQYE")(my_function)
        ```

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
            result = func(*args, **kwargs)
            if not stop_on_completion:
                return result

            stop_video_js = f"""
            var iframe = document.querySelector('iframe[src*="{video_id}"]');
            if (iframe) {{
                var url = new URL(iframe.src);
                url.searchParams.set('autoplay', '0');
                iframe.src = url.toString();
            }}
            """
            display(Javascript(stop_video_js))
            return result

        return wrapper

    return decorator


elevator = but_better("xNjyG8S4_kI")
favorite_customer = but_better("mwgcK4E_RU0")
gasolina = but_better("3tw2P65wv5E")
gotcha = but_better("dQw4w9WgXcQ")
phillies_hype_song = but_better("z3SEc70eQYE")
ten_hour_fireplace = but_better("L_LUpnjgPso")
