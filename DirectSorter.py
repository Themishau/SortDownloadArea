from Pathrunner import Pathrunner
from dataclasses import dataclass, field
import string
import logging
import os
import asyncio


@dataclass(slots=True)
class DirectSorter:
    pathrunner: Pathrunner = field(default_factory=Pathrunner)

