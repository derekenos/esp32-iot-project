
class ChangeNotificationDict(dict):
    """dict subclass that informs subscribers of changes
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subscribers = []

    def subscribe(self, fn):
        """Subscribe a function to receive change notifications.
        """
        self.subscribers.append(fn)

    def update(self, d):
        # Create a dict that represents only the items that will be modified.
        _d = {k: v for k, v in d.items() if k not in self or self[k] != v}
        if _d:
            # Update self.
            super().update(d)
            # Let all the subscribers know what changed.
            for fn in self.subscribers:
                fn(_d)

    def __setitem__(self, k, v):
        if k not in self or self[k] != v:
            # Update self.
            super().__setitem__(k, v)
            # Let all the subscribers know what changed.
            d = {k: v}
            for fn in self.subscribers:
                fn(d)
