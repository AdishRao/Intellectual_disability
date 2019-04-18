from fpdf import FPDF
import os
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
        self.rpmv =26
        self.gdtv =20
        self.bstv =90
        self.viv =90
        #Final report text
        self.pdf.set_font("Arial",size=24)
        self.pdf.cell(60, 10,txt=self.text,ln = 50,align="L")
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
        self.pdf.cell(60, 7,txt="Age:"+str(self.age),ln = 1,align="L")
        #School
        self.pdf.set_font("Arial",size=14)
        self.pdf.cell(60, 7,txt="School:"+self.sch,ln = 1,align="L")
        #Bottom Line for the report 
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_line_width(0.5)
        self.pdf.line(0, 40, 500, 40)
        #Report Image
        filepath=os.path.dirname(os.path.abspath(__file__))
        self.path = filepath+'/Images/Report.png'
        self.pdf.image(self.path, x = 15, y = 150, w = 200, h =100)

        #Data list to plot the data
        self.data = [['Name of the test','Expected Score','Score Obtained','Remark']]

        #Adding the scores to data lsit
        #RPM
        self.temp = []
        self.temp.append("RPM")
        self.temp.append(str(self.rpmv))
        self.temp.append(str(self.rpm))
        if self.rpm < self.rpmv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #GDT
        self.temp = []
        self.temp.append("GDT")
        self.temp.append(str(self.gdtv))
        self.temp.append(str(self.gdt))
        if self.gdt < self.gdtv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #BST
        self.temp = []        
        self.temp.append("BST")
        self.temp.append(str(self.bstv))
        self.temp.append(str(round(self.bst,3)))
        if self.bst < self.bstv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)

        #VI
        self.temp = []        
        self.temp.append("VI")
        self.temp.append(str(self.viv))
        self.temp.append(str(round(self.vi,3)))
        if self.vi < self.viv:
            self.temp.append("Intellectual Disability")
        else:
            self.temp.append("Normal Score")
        self.data.append(self.temp)
        
        #Setting table parameters
        self.col_width = self.pdf.w / 4.5
        self.row_height = self.pdf.font_size+2
        self.spacing = 2
        #Drawing the table
        for row in self.data:
            for item in row:
                self.pdf.cell(self.col_width, self.row_height*self.spacing,txt=item, border=1)
            self.pdf.ln(self.row_height*self.spacing)
        self.pdf.output(filepath+"/Reports/"+self.name+".pdf")

#Run this to get a simple demo of the reoprt 
