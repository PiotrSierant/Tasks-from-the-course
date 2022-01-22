import time


class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print("<TABLE>")
        print(" <TR>")
        print("     <TH>Number</TH><TH>Description</TH>")
        print(" </TR>")
        return self

    def __exit__(self, a, b, c):
        print("</TABLE>")


with HtmlCM() as html:
    print(''' <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>
''')
