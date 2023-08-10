from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


#creating table element
def create_custom_table(table_data, count_detail, elements):

    # Define table style
    topic_count = count_detail[0]
    assignment_count = count_detail[1]
    resource_count = count_detail[2]

    plan_table_style = TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),

        #plan title
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),

        #topic section
        ("BACKGROUND", (0, 1), (0, topic_count + 1), colors.lightsteelblue),
        ("BACKGROUND", (1, 1), (-1, 1), colors.lightgrey),

        #assignment section
        ("BACKGROUND", (0, topic_count + 1 + 1), (0, topic_count + assignment_count + 1 + 1), colors.lightgoldenrodyellow),
        ("BACKGROUND", (1, topic_count + 1 + 1), (-1, topic_count + 1 + 1), colors.lightgrey),
        #resource section
        ("BACKGROUND", (0, topic_count + assignment_count + 1 + 1 + 1), (0, topic_count + assignment_count + resource_count + 1 + 1 + 1), colors.lightskyblue),
        ("BACKGROUND", (1, topic_count + assignment_count + 1 + 1 + 1), (-1, topic_count + assignment_count + 1 + 1 + 1), colors.lightgrey),
        
        #add lines
        ("LINEABOVE", (0, 0), (-1, 0), 1, colors.black),
        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
        ("LINEBELOW", (0, -1), (-1, -1), 1, colors.black),
        ("LINEBELOW", (0, topic_count + 1), (-1, topic_count + 1), 1, colors.black),
        ("LINEBELOW", (0, topic_count + assignment_count + 1 + 1), (-1, topic_count + assignment_count + 1 + 1), 1, colors.black),

        ("LINEBEFORE", (0, 0), (0, -1), 1, colors.black),
        ("LINEAFTER", (-1, 0), (-1, -1), 1, colors.black), 
        ("LINEAFTER", (0, 1), (0, -1), 1, colors.black), 
        ("LINEAFTER", (1, 1), (1, -1), 1, colors.black),
    ])

    # Create the table with the data
    table = Table(table_data, colWidths = [85, 175, 325])

    # Apply table style
    table.setStyle(plan_table_style)

    # Add table to the elements list
    elements.append(table)


#converting each week dictionary into list with count
def convert_list(dictionary):
    plan_data = []
    plan_data.append(["Plan: " + dictionary["plan_name"], "", ""])

    #for course
    topic_count = len(dictionary["plantopic_set"])
    plan_data.append(["COURSE", "Chapter", "Topic"])
    for topic in dictionary["plantopic_set"]:
        plan_data.append(["", str(topic["chapter"]),  topic["topic"]["topic_name"]])
        
    #for assignment
    assignment_count = len(dictionary["planassignment_set"])
    plan_data.append(["ASSIGNMENTS", "Chapter", "Assignment"])
    for assignment in dictionary["planassignment_set"]:
        plan_data.append(["", str(assignment["chapter"]),  assignment["assignment"]["assign_name"]])

    #for resource
    resource_count = len(dictionary["planresource_set"])
    plan_data.append(["RESOURCE", "Chapter", "Resource"])
    for resource in dictionary["planresource_set"]:
        plan_data.append(["", str(resource["chapter"]),  resource["resource"]["res_name"]])

    return [plan_data, [topic_count, assignment_count, resource_count]]


#making plan with looping each week
def make_plan_table(full_plan, person_name, subject, section_year):
    
    #path
    pdf_name = f"../media/plan_pdf/{person_name} {subject} {section_year}"
    pdf_file_path = f"./{pdf_name}.pdf"

    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
    elements = []

    #creating different styles for paragraph text
    paragraph_styles = getSampleStyleSheet()
    paragraph_styles.add(ParagraphStyle(name='Normal_CENTER',
                          parent=paragraph_styles['Normal'],
                          alignment=TA_CENTER,
                          fontSize=12,
                          fontName='Times-Roman',
                          textColor=colors.black,
                           leading=15
                          )
                        )

    #Create the multi-line heading with defined style
    heading_lines = [
        "Tribhuwan University Pulchowk Campus",
        person_name,
        f"Weekly Plan of {subject} {section_year}",
        "\u00A0",
    ]
    for line in heading_lines:
        heading_paragraph = Paragraph(line, paragraph_styles["Normal_CENTER"])
        elements.append(heading_paragraph)

    
    #Create multiple tables for plan
    for dictionary in full_plan:
        list_plan = convert_list(dictionary)[0]
        count_detail = convert_list(dictionary)[1]
        create_custom_table(list_plan, count_detail, elements)
        elements.append(Paragraph("\u00A0", paragraph_styles["Normal_CENTER"]))
    

    # Build the PDF file with the table
    doc.build(elements)

    return True


#main 
#person_name  = "Samip Neupane"
#subject = "COA"
#section_year = "BCT-3rd year"
""" full_plan = [
{
    "id": 1,
    "plan_name": "week 1",
    "sectionyear": 1,

    "plantopic_set": [
        {
            "chapter": 1,
        
            "topic": {
                "id": 1,
                "topic_name": "Memory"
            }
        },
        {
            "chapter": 1,
            "topic": {
                "id": 2,
                "topic_name": "Time complexity"
            }
        }
    ],
    "planassignment_set": [
        {
            "chapter": 1,
            "assignment": {
                "id": 1,
                "assign_name": "Assignment 1"
            }
        }
    ],
    "planresource_set": [
        {
            "chapter": 1,
            "resource": {
                "id": 1,
                "res_name": "Class Notes"
            }
        }
    ]
},

{
    "id": 1,
    "plan_name": "week 2",
    "sectionyear": 1,
    "plantopic_set": [
        {
            "chapter": 7,
            "topic": {
                "id": 1,
                "topic_name": "Memory and its types"
            }
        },
        {
            "chapter": 69,
            "topic": {
                "id": 2,
                "topic_name": "Time complexity, time is very very complex dude...."
            }
        }
    ],
    "planassignment_set": [
        {
            "chapter": 420,
            "assignment": {
                "id": 36,
                "assign_name": "budale dherai assignment diyo"
            }
        },
        {
            "chapter": 69696,
            "assignment": {
                "id": 44,
                "assign_name": "feri assignment diyo"
            }
        }
    ],
    "planresource_set": [
        {
            "chapter": 78,
            "resource": {
                "id": 1,
                "res_name": "Class Notes hya feri note lekhayo"
            }
        },
        {
            "chapter": 44,
            "resource": {
                "id": 9,
                "res_name": "ghanti lagna lagyo, still note"
            }
        }
    ]
}

]
"""

#make_plan_table(full_plan, person_name, subject, section_year)
#return -> True
