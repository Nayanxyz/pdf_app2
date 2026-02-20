from fpdf import FPDF
import pandas as pd                                           #pandas is data analysis library

pdf = FPDF(orientation="P", unit="mm",format="A4")            #P means potrait and unit is millimeters / unit is for diagrams

pdf.set_auto_page_break(auto=False, margin=0)                 #Set auto page break mode True by default and triggering margin

df = pd.read_csv("topics.csv")                                # and other things in pdf

for index, row in df.iterrows():

    pdf.add_page()                                                #to add pages in pdf

    pdf.set_font(family="Times", style="B", size=12 )
    pdf.set_text_color(200,200,0)                                #rgb max 254
    pdf.cell(w=0, h=12 , txt=row["Topic"], align="L", ln=1 , border=0)   #w = width/ h= height/ ln=\n (break line)/border=outline
    for y in range(20,298,10):                                             #max x2(width)=210,height=298 for A4 format  # h = size
        pdf.line(10,y ,200,y)                                      #to add lines , range (from line 20, to line 298, gap =10)

    #set footer
    pdf.ln(267)                                                          # pdf.line = single line below headings
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(0, 0, 0)                                  # rgb max 254
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1, border=0)
                                                                         #row["Topic"] topic is key for all headings in file
    for i in range(row["Pages"]-1):                                      #pages is key for no. of pages in csv file and -1 for removing an extra page
                                                                         # that above add_page method added in pdf
        pdf.add_page()

        pdf.ln(279)                                                      #pdf.ln adds empty break  lines
        pdf.set_font(family="Times", style="I",size=8)
        pdf.set_text_color(0, 0, 0)  # rgb max 254
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R", ln=1, border=0)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)



                                                                         #in console we iterates topics.csv to know its key
pdf.output("output.pdf")                                                 #for that / for index, row df.iterrows():
                                                                         # this iterrows method used for iterates every element
                                                                         # and we get a key for headings in topics.csv file