import pickle
import glob
import types

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)
 
 
def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data="""
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer="""</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)
 
 
 
def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)

class Cake():
    numberOfCake = 0
    bakery_offer = []
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        elif kind not in self.known_kinds:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.numberOfCake += 1
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '': 
            self.__text = text
        else:
            self.__text = ''
            print('chyba działa')


    def show_info(self):
        print('Name product: {}'.format(self.name.upper()))
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))

        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print("\t{}".format(a))

        if len(self.filling) > 0:
            print("Filling: \n\t{}".format(self.filling))

        print('Gluten free: {}'.format(self.__gluten_free))
        print('Text on the cake: {}'.format(self.__text))
        print('-'*30)


    def set_filling(self, filling):
        self.filling = filling


    def add_additives(self, additives):
        self.additives.extend(additives)


    def __get_text(self):
        return self.__text


    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    text = property(__get_text, __set_text, None, 'Text on the cake')


    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog_name):
        return glob.glob(catalog_name + '\*.bakery')

cake01 = Cake('Apple_pie', 'cake', 'apple', ['cinnamon'], 'apple', True, 'Happy day')
cake02 = Cake('Biscuit', 'biscuit', 'biscuit', [], '', True, 'Happy day')
cake03 = Cake('Brioche', 'bun', 'brioche', [], '', True, 'Happy day')
cake04 = Cake('Brownie', 'cake', 'chocolate', ['chocolate'], 'chocolate', True, 'Happy day')
cake05 = Cake('Candy', 'candy', 'fruits', [], 'fruits', True, 'Happy day')
cake06 = Cake('Cheesecake', 'cake', 'cheese', ['chocolate'], '', True, 'Happy day')
cake07 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream', True, 'Happy day')
cake08 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], '', True, 'Happy day')
cake09 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, 'Happy day')
cake10 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, 'Happy day')

cake07.set_filling('vanilla cream')
cake09.add_additives(['cocoa powder', 'coconuts'])

print('Today in our offer:\n')
for cake in Cake.bakery_offer:
    cake.show_info()

cake01.text = 'Happy birthday!'
cake02.text = '18'
 
for c in Cake.bakery_offer:
    c.show_info()

cake01.save_to_file(r'C:\Users\dzd07\Desktop\Python\cake01.bakery')
cake02.save_to_file(r'C:\Users\dzd07\Desktop\Python\cake02.bakery')

'''cake03.__gluten_free = False
print(dir(cake03))
cake03._Cake__gluten_free = False
cake03.show_info()

print('Is cake01 of type Cake? (isinstance)', isinstance(cake01, Cake))
print('Is cake01 of type Cake? (type)', type(cake01) is Cake)
print('vars cake01', vars(cake01))
print('vars Cake?', vars(Cake))
print('dir cake01', dir(cake01))
print('dir Cake?', dir(cake10))

print('Cake in menu: {}'.format(Cake.numberOfCake))

print('Id of class is: {}'.format(id(Cake)))
print('Id of instances are: {}, {}'.format(id(cake01), id(cake02)))
print('Check if object belongs to class:', isinstance(cake03, Cake))
print('Check if object belongs to class using type:', type(cake03) is Cake)
print('Check class of an object using  __class__:', cake03.__class__)

print('List of instance attributes with value:', vars(cake01))
print('List of class attributes with value:', vars(Cake))

print('List of instance attributes with value:', dir(cake01))
print('List of class attributes with value:', dir(Cake))'''

cake011 = Cake.read_from_file(r'C:\Users\dzd07\Desktop\Python\cake01.bakery')
cake011.show_info()

print(Cake.get_bakery_files(r'C:\Users\dzd07\Desktop\Python'))

#static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, r'C:\Users\dzd07\Desktop\Python\cake01.html')
 
#class method:
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html(r'C:\Users\dzd07\Desktop\Python\all_cakes.html')
 
'''#instance method:
for c in Cake.bakery_offer:
    c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
    c.export_this_cake_to_html(r'C:\Users\dzd07\Desktop\Python\{}.html'.format(c.name.replace(' ','_')))
'''