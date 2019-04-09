from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "to_camel_case"
    FUNCTION_NAMES = {
        "python_3": "to_camel_case",
        "js_node": "toCamelCase"
    }
    ENV_COVERCODE = {
        
    }