from dataclasses import dataclass, field
import string
import logging
import os
import asyncio

"""
set logging settings
"""
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

"""
class which runs through a directory and saves information on it
"""
@dataclass(slots=True)
class Pathrunner:
    path: str = ''
    path_files: list[str] = field(default_factory=list)
    root: str = field(default_factory=str)
    directories: list[str] = field(default_factory=list)
    fileExtentions: dict[str] = field(default_factory=dict)
    files: list[str] = field(default_factory=list)


    def getRootFilesDirectories(self):
        """
        get all information on the path and save it in lists
        we create dicts and save it in the class attributes
        """
        root = self.path
        directories = []
        directoryfiles = []

        """
        we use walk and break after first iteration 
        because we do not need to get deeper 
        """

        for r, d, f in os.walk(self.path):
            logging.debug(f'root: {r}')
            logging.debug(f'directores: {d}')
            logging.debug(f'files: {f}')
            self.directories = d.copy()
            self.files = f.copy()
            break



    def runThroughFiles(self):
        # r=root, d=directories, f = files
        for f in self.files:
            return



    def FindDirectory(self, fileExtention):
        return

