# def format_name(f_name, l_name):
#   f = f_name.lower()
#   lef = len(f_name)
#   ff = f[0].upper() + f[1:lef] 
#   l = l_name.lower()
#   lel = len(l_name)
#   ll = l[0].upper() + l[1:lel]
#   return (ff + " "+ll)
# fn = input("Enter your first name. ")
# ln = input("Enter your last name. ")
# print(format_name(fn,ln))

#### Through TITLE function
def format_name(f_name, l_name):
    """Take a first name and last name and format it to title format"""
  f = f_name.title()
  l = l_name.title()
  return f + " " + l
fn = input("Enter your first name. ")
ln = input("Enter your last name. ")
print(format_name(fn,ln))
format_