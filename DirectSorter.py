from copy import deepcopy
from io import StringIO
from Pathrunner import Pathrunner
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import docx
import string
import logging
import os
import asyncio


@dataclass(slots=True)
class DirectSorter(ABC):
    pathrunner: Pathrunner = field(default_factory=Pathrunner)

    def checkCreateDir(self):
        os.mkdir(self.pathrunner.targetpath + "/" + "omg1")

        return

