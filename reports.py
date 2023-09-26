#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

dir="supplier-data/descriptions/"



def generate_report(title,body,attachment):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(body,styles["Body Text"])
    
    table_style=[('GRID',(0,0),(-1,-1),1,'colors.black'),
                 ('FONTNAME',(0,0),(-1,0)),'Arial-Bold'),
                 ('ALIGN',(0,0),(-1,-1),'CENTER')]
    new_line=Spacer(1,20)
    report.build(report_title,new_line,report_info)
    
