from jinja2 import Environment, FileSystemLoader

file_lod = FileSystemLoader('templates')
env = Environment(loader= file_lod)
tm = env.get_template("page.htm")
msg = tm.render(dom ain='http://prorp.ua', title="Про Jinja")

print(msg)