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
	return response.render("initial/user.html", user=auth())

def register():
	return auth.register()

def login():
        return auth.login()

def account():
    return dict(register=auth.register(),
                login=auth.login())
	
def download():
	return response.download(request, db)


@auth.requires_login()
def show_cliente():
	response.title="Clientes"
	db.args=Cliente.id.readable=False
	grid = SQLFORM.grid(Cliente,
		user_signature=True, searchable=True, csv=False, 
		paginate=50, details=False, 
		ignore_rw = True, maxtextlength=26,
		create=auth.has_membership("admin"),
		editable=auth.has_membership("admin"),
		deletable=auth.has_membership("admin"),  
    	links = [lambda row: A('hosts', _class='btn', 
			_title='ver servidores', 
			_href=URL("initial", "/cliente_host", 
			vars=dict(f=row.id)))]
    	)
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def show_servidor():
	response.title="Servidores"
	db.args=Servidor.id.readable=False
	grid = SQLFORM.grid(Servidor,
		user_signature=True, searchable=True, csv=False,
		paginate=50, details=False, 
		ignore_rw = True, maxtextlength=26,
		create=auth.has_membership("admin"),
		editable=auth.has_membership("admin"),
		deletable=auth.has_membership("admin"),  
    	links = [lambda row: A('hosts', _class='btn', 
    		_title='ver servidores', _href=URL("initial", "/servidor_host", vars=dict(f=row.id)))]
		)
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def show_distro():
	response.title="Distribuições"
	teste = 1
	print teste
	db.args=Distro.id.readable=False
	db.args=Distro.img.readable=False
	grid = SQLFORM.grid(Distro,
		user_signature=True, searchable=True, csv=False,
		paginate=50, details=False, ignore_rw = True, 
		maxtextlength=26, links_placement='left',
		create=auth.has_membership("admin"),
		editable=auth.has_membership("admin"),
		deletable=auth.has_membership("admin"),  
    	links = [lambda row: A('hosts', 
    		_class='btn', 
    		_title='ver servidores', 
    		_href=URL("initial", "/distro_host", 
    		vars=dict(f=row.id))), 
    	dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.img) ))))]
		)
	return response.render("initial/show_grid.html", grid=grid)



@auth.requires_login()
def cliente_host():
	filtro = request.vars['f']
	cliente = db.executesql('SELECT nome FROM cliente WHERE id = %s;' %str(filtro))
	response.title = cliente[0][0]	
	

	query = ((db.hosts.id_cliente == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/exemplo", 
    		      vars=dict(f=row.hosts.id))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      args=(row.hosts.id)))]
	db.hosts.id.readable=False
	db.distro.img.readable=False
	db.distro.id.readable=False
	
	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, db.distro.img, db.distro.id,
			  db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, csv=False,
						details=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False)

	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def servidor_host():
	filtro = request.vars['f']
	servidor = db.executesql('SELECT nome FROM servidor WHERE id = %s;' %str(filtro))
	response.title = servidor[0][0]	

	db.distro.img.readable=False
	db.hosts.id.readable=False
	query = ((db.hosts.id_servidor == filtro) & (db.distro.id == db.hosts.id_distro))
	#query=((db.hosts.id_servidor == filtro))
	#query= db().select(db.hosts.ALL, db.distro.ALL,
	#	left=db.hosts.on(db.hosts.id_servidor == filtro)) # recupera dados select
	print query

	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) )))]

	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, db.distro.img, 
				db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, maxtextlength=23, links=links, links_placement='left')

	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def distro_host():
	filtro = request.vars['f']
	distro = db.executesql('SELECT nome FROM distro WHERE id = %s;' %str(filtro))
	response.title = distro[0][0]	
	
	db.hosts.id.readable=False
	db.distro.img.readable=True
	query = ((db.hosts.id_distro == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) )))]

	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, db.distro.img, 
			  db.hosts.servicos, db.hosts.nome)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, maxtextlength=23, links=links, links_placement='left')

	return response.render("initial/show_grid.html", grid=grid)

def exemplo():
	filtro = request.vars['f']
	#detalhes = db.hosts(db.hosts.id == filtro)
	#response.title = detalhes[0][0]

	query = ((db.hosts.id == filtro) & (db.hosts.id_cliente == db.cliente.id)
	 	    & (db.hosts.id_servidor == db.servidor.id) 
	 	    & (db.hosts.id_distro == db.distro.id)) 
	detalhes = db.hosts(query)

	query2 =  ((db.interface.id_hosts == filtro))
	rows = db.interface(query2)
	print rows

	fruits = ['banana', 'apple',  'mango']
	for fruit in fruits:        
   		print 'Current fruit :', fruit


	if detalhes.hosts.gateway == None:
		print "ok"
	else:
		print "false"
	
	return response.render("initial/detalhes_host.html", detalhes=detalhes)

def edit_host():
	response.view = 'initial/show_form.html'
	return dict(form=SQLFORM(db.hosts, request.args(0, cast=int)).process())


def interface():
	response.view = 'initial/show_form.html'
	return dict(form=SQLFORM(db.interface).process())



def exemploo():
#	return "teste"
	return response.render("default/teste.html", nome="fernando", 
		sobrenome="vieira", lista=["item1", "item2", "item3"])

def teste11():
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


 
