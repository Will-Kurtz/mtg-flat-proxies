class Debug:
    is_debug_enabled = False
    @classmethod
    def set_debug_enabled(cls, enabled: bool):
        cls.is_debug_enabled = enabled
    @classmethod
    def log(cls, text):
        if cls.is_debug_enabled:
            print(str(text))