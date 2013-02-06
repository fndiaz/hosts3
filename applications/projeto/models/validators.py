 ##Cliente
Cliente.nome.requires =IS_NOT_EMPTY(error_message=
						T("valor não pode ser nulo"))
Cliente.email.requires =IS_EMAIL(error_message=
						T("formato de e-mail inválido"))

##Servidor
Servidor.nome.requires =IS_NOT_EMPTY(error_message=
						T("valor não pode ser nulo"))

##Distro
Distro.nome.requires =IS_NOT_EMPTY(error_message=
						T("valor não pode ser nulo"))