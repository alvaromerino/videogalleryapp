import os
from django.conf import settings
from pathlib import Path
from pymediainfo import MediaInfo


def is_video(path):
    file_info = MediaInfo.parse(path)
    for track in file_info.tracks:
        if track.track_type == "Video":
            return True
    return False


def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try:
        lst = sorted(os.listdir(path))
    except OSError:
        pass
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                if is_video(fn):
                    rel_path = str(Path(fn).relative_to(settings.MEDIA_ROOT))
                    url = os.path.join(settings.MEDIA_URL, rel_path)
                    # Replace double slashes to single slashes
                    url = url.replace("//", "/")
                    url = url.replace("\\", "/")
                    tree['children'].append(dict(name=name, src=url))
    return tree
