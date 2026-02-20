from fpdf import FPDF
import pandas as pd                                           #pandas is data analysis library

pdf = FPDF(orientation="P", unit="mm",format="A4")            #P means potrait and unit is millimeters / unit is for diagrams

df = pd.read_csv("topics.csv")                                # and other things in pdf

for index, row in df.iterrows():

    pdf.add_page()                                                #to add pages in pdf

    pdf.set_font(family="Times", style="B", size=12 )
    pdf.set_text_color(200,200,0)                              #rgb max 254
    pdf.cell(w=0, h=12 , txt=row["Topic"], align="L", ln=1 , border=0)   #w = width/ h= height/ ln=\n (break line)/border=outline
    pdf.line(10,21 ,200,21)                               #max x2=210 for A4 format  # h = size
                                                                         #row["Topic"] topic is key for all headings in file


                                                               #in console we iterates topics.csv to know its key
pdf.output("output.pdf")                                      #for that / for index, row df.iterrows():  this itterows method used for iterates every element
                                                              # and we get a key for headings in topics.csv file