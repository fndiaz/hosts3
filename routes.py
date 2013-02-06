routers = dict(

    # base router
    BASE=dict(
        default_application='projeto',
    ),

    projeto=dict(
        default_controller='initial',
        default_function='home',
        functions=['home', 'contact', 'about', 'user', 'download', 'account', 
			'register', 'login', 'exemplo', 'teste1', 'teste2', 
			'show_cliente', 'show_servidor', 'show_distro', 
			'cliente_host', 'servidor_host', 'distro_host', 'product']
    )

)
