
from flask import Flask, render_template,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from docx import Document
import docx
import xlsxwriter


app = Flask(__name__ )

@app.route('/')
def home():
    return "Hello"

@app.route('/upload')
def upload_file():
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
    Questions_File = request.files['Questions_File']
    Answer_File= request.files['Answer_File']
    Questions_Doc = Document(Questions_File)
    Answer_Doc = Document(Answer_File)

    #Questions_Doc
    Questions = []
    for paragraph in Questions_Doc.paragraphs:
        Questions.append(paragraph.text)

    # Answer_Doc
    Answer = []
    for paragraph1 in Answer_Doc.paragraphs:
        Answer.append(paragraph1.text)

    # 
    Ans =[]
    for character1 in Answer:
        rep = character1.replace("  ","")
        # c=d.replace("\t","")
        Ans.append(rep)
        if '' in Ans:
            Ans.remove('')

    # print(completedtext1)
    # print(Ans)
    Que =[]
    for character in Questions:
        d = character.replace("  ","")
        c=d.replace("\t","")
        Que.append(c)
        if '' in Que:
            Que.remove('')

    final_Questions= [] 
    for i in Que: 
        x=(i.split("("))
        final_Questions.append(x)
        if '' in final_Questions:
            final_Questions.remove('')


    dic = {}        
    for i in final_Questions:
        for j in i:
            if j.startswith("a)"):
                if "option-A" not in dic:
                    dic["option-A"] = []
                dic["option-A"].append(j) 

            elif j.startswith("b)")  or j.startswith("b "):
                if "option-B" not in dic:
                    dic["option-B"] = []
                dic["option-B"].append(j)

            elif j.startswith("c)"):
                if "option-C" not in dic:
                    dic["option-C"] = []
                dic["option-C"].append(j)
            
            elif j.startswith("d)") or j.startswith(("d")):
                if "option-D" not in dic:
                    dic["option-D"] = []
                dic["option-D"].append(j)
                # print(dic["option-D"])
            
            elif j.startswith("e)"):
                if "option-E" not in dic:
                    dic["option-E"] = []
                dic["option-E"].append(j)
            else:
                if "Questions" not in dic:
                    dic["Questions"] = []                
                dic["Questions"].append(j)

                k = dic.values()
                for x in k:
                    for z in x:
                        if z=='':
                            x.remove(z)

    for i in range(len(Ans)):
        if Ans[i]=="(a)":
            Ans[i]=1
        elif Ans[i]=="(b)":
            Ans[i]=2
        elif Ans[i]=="(c)":
            Ans[i]=3
        elif Ans[i]=="(d)":
            Ans[i]=4


    for a in Ans:
        if "Answer" not in dic:
            dic["Answer"] = []
        dic["Answer"].append(a)


    data=[dic]
    workbook = xlsxwriter.Workbook("WithOutImageQuestion.xlsx")
    worksheet = workbook.add_worksheet("firstsheet")


    worksheet.write(0,0,"Questions")
    worksheet.write(0,1,"option-A")
    worksheet.write(0,2,"option-B")
    worksheet.write(0,3,"option-C")
    worksheet.write(0,4,"option-D")
    worksheet.write(0,5,"option-E")
    worksheet.write(0,6,"Answer")


    for index , entry in enumerate(data):
        worksheet.write_column(index+1 ,0,entry["Questions"])
        worksheet.write_column(index+1 ,1,entry['option-A'])
        worksheet.write_column(index+1 ,2,entry['option-B'])
        worksheet.write_column(index+1 ,3,entry['option-C'])
        worksheet.write_column(index+1 ,4,entry['option-D'])
        worksheet.write_column(index+1 ,5,entry['option-E'])
        worksheet.write_column(index+1 ,6,entry['Answer'])

    workbook.close()
    
    return send_from_directory("","WithOutImageQuestion.xlsx",download_name = "Question Answer sheet.xlsx")
		
if __name__ == '__main__':
   app.run(debug = True)