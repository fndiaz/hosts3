Cliente = db.define_table("cliente",
      Field("nome", notnull=True, unique=True),
      Field("email", unique=True),
      #auth.signature
      format="%(nome)s")

Servidor = db.define_table("servidor",
      Field("nome"),
      format="%(nome)s")

Distro = db.define_table("distro",
      Field("nome"),
      Field("img"),
      format="%(nome)s")

Hosts = db.define_table("hosts",
      Field("id_cliente", db.cliente),
      Field("id_servidor", db.servidor),
      Field("id_distro", db.distro),
      Field("nome"),
      Field("servicos")
      )
