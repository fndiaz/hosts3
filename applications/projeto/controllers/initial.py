# coding: utf-8

def home():
	nome = "Fernando"
	response.title = "Titulo home"
	return dict(nome=nome)

def contact():
	return "form"

def about():
	return "sobre"

def user():
	if request.args(0) == 'register':
        	db.auth_user.bio.writable = db.auth_user.bio.readable = False
	return dict(user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)



def show_cliente():
	response.title="Clientes"
	db.args=Cliente.id.readable=False
	grid = SQLFORM.grid(Cliente,
		user_signature=True, searchable=True, 
		paginate=50, deletable=True, editable=True, 
		details=False, ignore_rw = True, maxtextlength=26,  
    	links = [lambda row: A('hosts', _class='btn', 
			_title='ver servidores', 
			_href=URL("initial", "/cliente_host", 
			vars=dict(f=row.id)))]
    	)
	return response.render("initial/show_grid.html", grid=grid)

def show_servidor():
	response.title="Servidores"
	db.args=Servidor.id.readable=False
	grid = SQLFORM.grid(Servidor,
		user_signature=True, searchable=True, 
		paginate=50, deletable=True, editable=True, 
		details=False, ignore_rw = True, maxtextlength=26,  
    	links = [lambda row: A('hosts', _class='btn', 
    		_title='ver servidores', _href=URL("initial", "/servidor_host", vars=dict(f=row.id)))]
		)
	return response.render("initial/show_grid.html", grid=grid)

def show_distro():
	response.title="Distribuições"
	teste = 1
	print teste
	db.args=Distro.id.readable=False
	db.args=Distro.img.readable=False
	grid = SQLFORM.grid(Distro,
		user_signature=True, searchable=True, 
		paginate=50, deletable=True, editable=True, 
		details=False, ignore_rw = True, maxtextlength=26, links_placement='left',  
    	links = [lambda row: A('hosts', 
    		_class='btn', 
    		_title='ver servidores', 
    		_href=URL("initial", "/cliente_host", 
    		vars=dict(f=row.id))), 
    	dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.img) ))))]
		)
	return response.render("initial/show_grid.html", grid=grid)

def cliente_host():
	filtro = request.vars['f']
	cliente = db.executesql('SELECT nome FROM cliente WHERE id = %s;' %str(filtro))
	response.title = cliente[0][0]	
	
	db.hosts.id.readable=False
	query=((db.hosts.id_cliente == filtro))
	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, 
				db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
           'host.id_servidor': 'Servidor',
           'host.id_distro': 'Distro',
          'host.nome': 'Nome',
	   'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, 
						details=False, maxtextlength=23)

	return response.render("initial/show_grid.html", grid=grid)

def servidor_host():
	filtro = request.vars['f']
	servidor = db.executesql('SELECT nome FROM servidor WHERE id = %s;' %str(filtro))
	response.title = servidor[0][0]	

	
	db.hosts.id.readable=False
	query=((db.hosts.id_servidor == filtro))

	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images") )))]

	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, 
				db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
           'host.id_servidor': 'Servidor',
           'host.id_distro': 'Distro',
          'host.nome': 'Nome',
	   'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, 
						details=False, maxtextlength=23, links=links, links_placement='left')

	return response.render("initial/show_grid.html", grid=grid)

def distro_host():
	filtro = request.vars['f']
	distro = db.executesql('SELECT nome FROM distro WHERE id = %s;' %str(filtro))
	response.title = distro[0][0]	
	
	db.hosts.id.readable=False
	query=((db.hosts.id_servidor == filtro))
	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, 
				db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
           'host.id_servidor': 'Servidor',
           'host.id_distro': 'Distro',
          'host.nome': 'Nome',
	   'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, 
						details=False, maxtextlength=23)

	return response.render("initial/show_grid.html", grid=grid)




def exemplo():
#	return "teste"
	return response.render("default/teste.html", nome="fernando", sobrenome="vieira", lista=["item1", "item2", "item3"])

def teste1():
	print "Action index"
	print request.args
	print request.vars 	
	print request.post_vars #somente entradas de formulário
    	print request.get_vars  #somente entradas de url
    	#nome = request.vars['nome']
        mensagem = "Bem Vindo"
        form = "<form action='' method='POST'><input name='nome' id='nome'/><input type='Submit'></form><br>"
        if 'nome' in request.vars:
		form = "<p>Bem vindo %(nome)s</p>" % request.vars + form		
		#mensagem = mensagem + " usuário %(nome)s" % request.vars	#mostrando variavel da url
        	#mensagem = mensagem + " usuário %s" %str(nome)			#mostrando uma variavel local    
	return form

def teste2():
	return "<form><label>Nome</label><input /></form><br><a href='http://www.w3schools.com'>Visit W3Schools</a>"
	#return dict(nome="fernando")
	#return response.render("teste.html", dict(nome="fernando"))

def soma(x, y):
	return x + y

def product():
    grid = SQLFORM(db.product)
    return response.render("initial/show_grid.html", grid=grid)

 
