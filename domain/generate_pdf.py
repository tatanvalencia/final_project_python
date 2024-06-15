from fpdf import FPDF

def generate_pdf(phishing_emails, file_name='phishing_report.pdf'):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, txt='Reporte de correos electrónicos sospechosos de Phishing.', ln=True, align='C')
    pdf.ln(10)
    for email in phishing_emails:
        pdf.set_font('Arial', size=10)
        from_ = email['from'].encode('latin-1', 'ignore').decode('latin-1')
        subject = email['subject'].encode('latin-1', 'ignore').decode('latin-1')
        content = email['content'][:200].encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, txt=f'De: {from_}', align='L')
        pdf.multi_cell(0, 10, txt=f'Asunto: {subject}', align='L')
        pdf.multi_cell(0, 10, txt=f'Fecha: {email['date']}', align='L')
        pdf.multi_cell(0, 10, txt=f'Contenido: {content}...', align='L')
    pdf.output(file_name)
    print(f'Reporte generado exitosamente {file_name}')