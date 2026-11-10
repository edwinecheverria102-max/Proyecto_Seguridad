from django.db import models


class Usuario(models.Model):
    email = models.EmailField(max_length=255)
    password_hash = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'usuarios'


class Pedido(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id', related_name='pedidos')
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Pedidos'


class SecurityEvent(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id', related_name='security_events')
    event = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    resultado = models.CharField(max_length=255)
    orien = models.CharField(max_length=255)

    class Meta:
        db_table = 'SECURITY_EVENTS'


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    file_name = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'productos'


class Payment(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='Pedidos_id', related_name='payments')
    transaction_reference = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PAYMENTS'


class OrderItem(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='Pedidos_id', related_name='order_items')
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='producto_id', related_name='order_items')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ORDER_ITEMS'


class Download(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id', related_name='downloads')
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='Pedidos_id', related_name='downloads')
    produoducto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='produoducto', related_name='download_records')
    fingerprint = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'DOWNLOADS'
