# CS50 Shirtificate
from fpdf import FPDF


def main():
    NAME = "Jack"
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", style="B", size=36)
    pdf.cell(0, 50, "CS50 Shirtificate", align="C", ln=1)

    pdf.image("shirtificate.png", x=-0.5)

    pdf.set_y(140)
    pdf.set_text_color(255,255,255)
    pdf.set_font("helvetica", style="B", size=24)
    pdf.cell(0, 10, f"{NAME} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
