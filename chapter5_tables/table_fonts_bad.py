# table_fonts_bad.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def table_fonts_bad():
    doc = SimpleDocTemplate("table_fonts_bad.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tblstyle = TableStyle([('FONT', (0, 1), (-1, 1), 'Helvetica'),
                           ('FONTSIZE', (0, 1), (-1, 1), 24)
                           ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_fonts_bad()