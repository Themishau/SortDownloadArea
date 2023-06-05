from Pathrunner import Pathrunner
from dataclasses import dataclass, field
import docx
import string
import logging
import os
import asyncio


@dataclass(slots=True)
class DirectSorter:
    pathrunner: Pathrunner = field(default_factory=Pathrunner)

    def checkCreateDir(self):
        os.mkdir(self.pathrunner.targetpath + "/" + "omg1")

        return

    def readDocx(self):
        doc = docx.Document(self.pathrunner.path + "/" + "レジュメ - Kopie.docx")
        all_paras = doc.paragraphs
        len(all_paras)
        for para in all_paras:
            print(para.text)
            print("-------")