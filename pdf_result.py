import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Excel read
df = pd.read_excel("students.xlsx")

styles = getSampleStyleSheet()

for index, row in df.iterrows():
    name = row["Name"]
    total = row["Marks1"] + row["Marks2"] + row["Marks3"]
    avg = total / 3

    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 33:
        grade = "C"
    else:
        grade = "Fail"

    # PDF create
    pdf = SimpleDocTemplate(f"{name}_result.pdf")
    content = []

    content.append(Paragraph(f"Name: {name}", styles["Normal"]))
    content.append(Paragraph(f"Total: {total}", styles["Normal"]))
    content.append(Paragraph(f"Average: {avg}", styles["Normal"]))
    content.append(Paragraph(f"Grade: {grade}", styles["Normal"]))

    pdf.build(content)