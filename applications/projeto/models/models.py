Cliente = db.define_table("cliente",
      Field("nome", notnull=True, unique=True),
      Field("email"),
      Field("gtalk"),
      #auth.signature
      format="%(nome)s")

Servidor = db.define_table("servidor",
      Field("nome", notnull=True),
      format="%(nome)s")

Distro = db.define_table("distro",
      Field("nome", notnull=True),
      Field("img", notnull=True),
      Field("imagem", notnull=True),
      format="%(nome)s")

Hosts = db.define_table("hosts",
      Field("id_cliente", db.cliente),
      Field("id_servidor", db.servidor),
      Field("id_distro", db.distro),
      Field("servicos", "text"),
      Field("if1"),
      Field("ip1"),
      Field("masc1"),
      Field("obs1"),
      Field("if2"),
      Field("ip2"),
      Field("masc2"),
      Field("obs2"),
      Field("if3"),
      Field("ip3"),
      Field("masc3"),
      Field("obs3"),
      Field("if4"),
      Field("ip4"),
      Field("masc4"),
      Field("obs4"),
      Field("nome", notnull=True),
      Field("ip_chegada", notnull=True),
      Field("porta_ssh", notnull=True),
      Field("gateway", notnull=True),
      Field("rotas", "text"),
      Field("obs_gerais", "text"),
      format="%(nome)s")

Interface = db.define_table("interface",
      Field("id_hosts", db.hosts),
      Field("nome"),
      Field("ip"),
      format="%(nome)s")




