from yaml import safe_load


config_file = "configuration.yaml"
exclusions_key = "exclusions"
configuration: dict = None

def _load_configuration() -> dict:
    with open(config_file, 'r') as f:
        config: dict = safe_load(f)
    global configuration
    configuration = config  # save to global var so we only have to lookup data once
    return config


def _get_configuration() -> dict:
    # Use saved data if already looked up, else start new lookup
    return configuration if configuration is not None else _load_configuration()


def get_names() -> list:
    names = _get_configuration().keys()
    names = list(set(names))  # Temp cast to 'set' to remove duplicates
    return names


def get_exclusions(name: str) -> list[str]:
    config = _get_configuration()
    exclusions = config[name][exclusions_key]
    exclusions.append(name)
    exclusions = list(set(exclusions))  # Temp cast to 'set' to remove duplicates
    return exclusions