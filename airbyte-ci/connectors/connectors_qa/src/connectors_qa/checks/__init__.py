# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
from .assets import ENABLED_CHECKS as ASSETS_CHECKS
from .documentation import ENABLED_CHECKS as DOCUMENTATION_CHECKS
from .metadata import ENABLED_CHECKS as METADATA_CORRECTNESS_CHECKS
from .packaging import ENABLED_CHECKS as PACKAGING_CHECKS
from .security import ENABLED_CHECKS as SECURITY_CHECKS
from .testing import ENABLED_CHECKS as TESTING_CHECKS

ENABLED_CHECKS = DOCUMENTATION_CHECKS + METADATA_CORRECTNESS_CHECKS + PACKAGING_CHECKS + ASSETS_CHECKS + SECURITY_CHECKS + TESTING_CHECKS
