from copy import deepcopy
from io import StringIO
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from DirectSorter import DirectSorter
import docx

@dataclass(slots=True)
class DocxCreater(ABC):
    directSorter: DirectSorter = field(default_factory=DirectSorter)
    def copyTestCasesToTestDoc(self):
        """ copies test cases from PH to test doc """
        doc = docx.Document(self.directSorter.pathrunner.path + "/" + "z2.docx")
        doc2 = docx.Document(self.directSorter.pathrunner.path + "/" + "z3.docx")
        all_paras = doc2.paragraphs
        len(all_paras)
        for para in all_paras:
            print(para.text)
            print("-------")
        print("-----333333333333333333-----")
        template = doc2.tables[0]
        tbl = template._tbl
        # Here we do the copy of the table
        new_tbl = deepcopy(tbl)
        print(new_tbl)
        paragraph = doc.add_paragraph()
        # After that, we add the previously copied table
        paragraph._p.addnext(new_tbl)
        doc.save(self.directSorter.pathrunner.path + "/" + "z4.docx")