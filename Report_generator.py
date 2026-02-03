import pandas as pd
from fpdf import FPDF

data = pd.read_csv("data.csv")

average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Average Marks: {average_marks:.2f}", ln=True)
pdf.cell(0, 10, f"Highest Marks: {highest_marks}", ln=True)
pdf.cell(0, 10, f"Lowest Marks: {lowest_marks}", ln=True)
pdf.ln(10)

pdf.set_font("Arial", "B", 12)
pdf.cell(90, 10, "Name", border=1)
pdf.cell(40, 10, "Marks", border=1)
pdf.ln()

pdf.set_font("Arial", size=12)
for index, row in data.iterrows():
    pdf.cell(90, 10, row["Name"], border=1)
    pdf.cell(40, 10, str(row["Marks"]), border=1)
    pdf.ln()

pdf.output("Student_Report.pdf")

print("Report generated successfully!")