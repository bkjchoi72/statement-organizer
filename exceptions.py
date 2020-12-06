class CouldNotIdentifyStatementError(ValueError):
    pass


class InvalidConfigFileError(ValueError):
    pass


class ConfigFileNotFoundError(FileNotFoundError):
    pass


class UnknownStatementError(ValueError):
    pass
