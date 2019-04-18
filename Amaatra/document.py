from fpdf import FPDF

class Report:
    def __init__(self):
        self.pdf = FPDF() 
    def genrep(self,name,age,sch,rpm,gdt,bst,vi):
        self.pdf.add_page()
        self.text = 'Final report'
        self.name = name
        self.rpm  = rpm
        self.gdt = gdt
        self.bst = bst
        self.vi = vi
        self.age = age
        self.sch = sch

        #Setting the threshold values for each test
        self.rpmv  = 0
        self.gdtv =0
        self.bstv =0
        self.viv =0
        #Final report text
        self.pdf.set_font("Arial",size=24)
        self.pdf.cell(60, 10,txt=text,ln = 50,align="L")
        #First Sep line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 20, 500, 20)
        #Vertical line
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(10, 0, 10, 1000)
        
        #Displaying student details
        #Name
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60,7,txt="Name:"+self.name,ln = 1,align="L")
        #Age
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="Age:"+self.age,ln = 1,align="L")
        #School
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="School:"+self.sch,ln = 1,align="L")
        #Bottom Line for the report 
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 40, 500, 40)
        #Report Image
        self.path = 'Images/Report.png'
        self.pdf.image(path, x = 15, y = 150, w = 200, h =100)

        #Data list to plot the data
        self.data = [['Name of the test','Expected Score','Score Obtained','Remark']]

        #Adding the scores to data lsit
        #RPM
        self.temp = []
        self.temp.append("RPM")
        self.temp.append(self.rpmv)
        self.temp.append(self.rpm)
        if self.rpm < self.rpmv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #GDT
        self.temp = []
        self.temp.append("GDT")
        self.temp.append(self.gdtv)
        self.temp.append(self.gdt)
        if self.gdt < self.gdtv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #BST
        self.temp = []        
        self.temp.append("BST")
        self.temp.append(self.bstv)
        self.temp.append(self.bst)
        if self.bst < self.bstv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #VI
        self.temp = []        
        self.temp.append("VI")
        self.temp.append(self.viv)
        self.temp.append(self.vi)
        if self.vi < self.viv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #Setting table parameters
        self.col_width = pdf.w / 4.5
        self.row_height = pdf.font_size+2
        self.spacing = 2
        #Drawing the table
        for row in self.data:
            for item in row:
                pdf.cell(self.col_width, self.row_height*self.spacing,txt=item, border=1)
            pdf.ln(row_height*spacing)
        self.pdf.output("Reports/"+self.name+".pdf")

#Run this to get a simple demo of the reoprt 


pdf = FPDF()
pdf.add_page()
text = 'Final report' 
pdf.set_font("Arial",size=24)
pdf.cell(60, 10,txt=text,ln = 50,align="L")

pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.5)
pdf.line(0, 20, 500, 20)

pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.5)
pdf.line(7, 0, 7, 1000)


pdf.set_font("Arial",size=14)
pdf.cell(60,7,txt="Name:Abhi",ln = 1,align="L")
pdf.set_font("Arial",size=14)
pdf.cell(60, 7,txt="Age:6",ln = 1,align="L")

pdf.set_font("Arial",size=14)
pdf.cell(60, 7,txt="School:SSRVM",ln = 1,align="L")

pdf.set_draw_color(0, 0, 0)
pdf.set_line_width(0.5)
pdf.line(0, 40, 500, 40)

#Report Image
pdf.set_font("Arial",size=14)
pdf.cell(60, 7,txt="",ln = 1,align="L")
path = 'Images/Report.png'
pdf.image(path, x = 15, y = 150, w = 200, h =100)
col_width = pdf.w / 4.5
row_height = pdf.font_size+2
spacing = 2
data = [['Name of the test','Expected Score','Score Obtained','Remark'],['RPM','60','40','ID'],['BST','75','90','Not ID'],['GDT','50','40','MILD ID'],['VI','100','60','ID']]
for row in data:
    for item in row:
        pdf.cell(col_width, row_height*spacing,txt=item, border=1)
    pdf.ln(row_height*spacing)

pdf.output("Reports/simple_demo.pdf")

