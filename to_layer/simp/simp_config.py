# can be used to configure a simp problem
class SIMPConfig:
    volfrac = 0.44
    p = 3.0
    eta = 0.5
    filter = 'sensitivity'
    rmin = 1.5
    max_main_iterations = 50

    @classmethod
    def create_dict(cls):
        d = {key: value for key, value in cls.__dict__.items()
                if not str(key).startswith('__') and callable(value) is False}
        d.pop('create_dict')
        return d
