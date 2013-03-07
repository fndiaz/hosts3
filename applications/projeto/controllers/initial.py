# coding: utf-8

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
			vars=dict(f=row.id, n1='Clientes', p1='show_cliente')))]
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
    		_title='ver servidores', 
    		_href=URL("initial", "/servidor_host", 
    		vars=dict(f=row.id, n1='Servidores', p1='show_servidor')))]
		)
	return response.render("initial/show_grid.html", grid=grid)

@auth.requires_login()
def show_distro():
	response.title="Distribuições"

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
    		vars=dict(f=row.id, n1='Distros', p1='show_distro'))), 
    	dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.img) ))))]
		)
	return response.render("initial/show_grid.html", grid=grid)


@auth.requires_login()
def cliente_host():
	filtro = request.vars['f']
	queryset = db(db.cliente.id == filtro)
	rows = queryset.select()
	cliente = rows[0]
	response.title = cliente.nome
	print cliente

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = cliente.nome

	query = ((db.hosts.id_cliente == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/exemplo", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=cliente.nome, 
    		      			n1='Clientes', p1='show_cliente', p='cliente_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=cliente.nome, 
    		      		n1='Clientes', p1='show_cliente', p='cliente_host')))]
	db.hosts.id.readable=False
	db.distro.img.readable=False
	
	fields = (db.hosts.id, db.hosts.id_servidor, db.hosts.id_distro, db.distro.img, 
			  db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

@auth.requires_login()
def servidor_host():
	filtro = request.vars['f']
	queryset = db(db.servidor.id == filtro)
	rows = queryset.select()
	servidor = rows[0]
	response.title = servidor.nome

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = servidor.nome	

	db.distro.img.readable=False
	db.hosts.id.readable=False
	query = ((db.hosts.id_servidor == filtro) & (db.distro.id == db.hosts.id_distro))

	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/exemplo", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=servidor.nome, 
    		      		n1='Servidores', p1='show_servidor', p='servidor_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=servidor.nome, 
    		      		n1='Servidores', p1='show_servidor', p='servidor_host')))]

	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_distro, db.distro.img, 
				db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

@auth.requires_login()
def distro_host():
	filtro = request.vars['f']
	queryset = db(db.distro.id == filtro)
	rows = queryset.select()
	distro = rows[0]
	response.title = distro.nome

	nome_ant1 = request.vars['n1']
	funcao_ant1 = request.vars['p1']
	nome_atual = distro.nome	
	
	db.hosts.id.readable=False
	db.distro.img.readable=False
	query = ((db.hosts.id_distro == filtro) & (db.distro.id == db.hosts.id_distro))
	links = [dict(header='',body=lambda row: A( IMG(_src=URL("static", "images", args=(row.distro.img)) ))), 
	 lambda row: A('Detalhes', 
    		      _class='btn', 
    		      _title='Detalhes', 
    		      _href=URL("initial", "/exemplo", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=distro.nome, 
    		      		n1='Distros', p1='show_distro', p='distro_host'))),
	 lambda row: A('Editar', 
    		      _class='btn', 
    		      _title='Editar', 
    		      _href=URL("initial", "/edit_host", 
    		      vars=dict(f=row.hosts.id, c=filtro, n=distro.nome, 
    		      		n1='Distros', p1='show_distro', p='distro_host')))]

	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_servidor, db.distro.img, 
			  db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, searchable=False, maxtextlength=23, links=links, 
						links_placement='left', editable=False, create=False)

	return response.render("initial/show_grid2.html", grid=grid, nome_ant1=nome_ant1, 
						funcao_ant1=funcao_ant1, nome_atual=nome_atual)

def exemplo():
	filtro = request.vars['f'] #id_host
	id_cliente = request.vars['c'] #id_cliente
	nome_ant = request.vars['n'] #nome (asterisk ou agronelli ou debian)
	nome_ant1 = request.vars['n1'] #nome (servidores ou clientes ou distros)
	funcao_ant = request.vars['p'] #funcao(host_servidores)
	funcao_ant1 = request.vars['p1'] #funcao(show_servidores)
	

	query = ((db.hosts.id == filtro) & (db.hosts.id_cliente == db.cliente.id)
	 	    & (db.hosts.id_servidor == db.servidor.id) 
	 	    & (db.hosts.id_distro == db.distro.id)) 
	detalhes = db.hosts(query)
	
	
	return response.render("initial/detalhes_host.html", detalhes=detalhes, 
				id_cliente=id_cliente, funcao_ant=funcao_ant, funcao_ant1=funcao_ant1, 
				nome_ant=nome_ant, nome_ant1=nome_ant1, filtro=filtro)

def edit_host():
	id_cliente = request.vars['c']
	nome_ant = request.vars['n']
	nome_ant1 = request.vars['n1']
	funcao_ant = request.vars['p']
	funcao_ant1 = request.vars['p1']

	response.view = 'initial/show_form.html'
	return dict(form=SQLFORM(db.hosts, request.vars['f']).process(), 
				id_cliente=id_cliente, funcao_ant=funcao_ant, funcao_ant1=funcao_ant1, 
					nome_ant=nome_ant, nome_ant1=nome_ant1)


@auth.requires_login()
def interface():
	response.view = 'initial/show_form2.html'
	return dict(form=SQLFORM(db.hosts, request.vars['f']).process())


def interfaceee():
	response.view = 'initial/show_form2.html'
	return dict(form=SQLFORM(db.hosts).process())


def home():
	nome = "Fernando"
	response.title = "Titulo home"
	return dict(nome=nome)

def contact():
	return "form"

def about():
	filtro = request.vars['f']
	query = ((db.hosts.id_servidor == filtro) & (db.distro.id == db.hosts.id_distro))
	fields = (db.hosts.id, db.hosts.id_cliente, db.hosts.id_distro, db.distro.img, 
				db.hosts.ip_chegada, db.hosts.porta_ssh, db.hosts.gateway)
	headers = {'host.id':   'ID',
               'host.id_servidor': 'Servidor',
               'host.id_distro': 'Distro',
               'host.nome': 'Nome',
	           'host.servicos': 'Servicos'}
	grid = SQLFORM.grid(query=query, fields=fields, headers=headers, csv=False,
						details=False, maxtextlength=23, searchable=True, editable=False, create=False)

	return response.render("initial/teste.html", grid=grid,)

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


 
