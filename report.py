import csv
from statistics import mean, median
from fpdf import FPDF

def readData(fpath):
    data=[]
    with open(fpath,newline='') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
         row['Value']=float(row['Value'])
         data.append(row)
    return data  

def analyze(data):
   values=[item['Value'] for item in data] 
   return{
      'count':len(values),
      'mean':round(mean(values),2),
      'median':round(median(values),2),
      'max': max(values),
      'min':min(values)
   }

def generate(data,stats,output):
   pdf=FPDF()
   pdf.add_page()
   pdf.set_font("Arial",size=12)
   pdf.set_font("Arial",style='B',size=16)
   pdf.cell(200, 10, txt="Data Analysis",ln=True,align='C')
   pdf.ln(10)
   pdf.set_font("Arial",size=12)
   pdf.cell(200,10, txt="Statistics:",ln=True)
   for key,value in stats.items():
      pdf.cell(200,10,txt=f"{key.capitalize()}:{value}",ln=True)
   pdf.ln(10)
   pdf.cell(200,10,txt="Data Table:",ln=True)
   pdf.set_font("Arial",size=10)
   for item in data:
      pdf.cell(200,10,txt=f"{item['Date']}_{item['Name']}_{item['Category']}:{item['Value']}",ln=True)
   pdf.output(output)
   print(f"Report generated: {output}")

if __name__=="__main__":
   input_file="sample.csv"
   outputpdf="analysisReport.pdf"
   dataset=readData(input_file)
   statistics=analyze(dataset)
   generate(dataset,statistics,outputpdf)