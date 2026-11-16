from django.test import TestCase
from django.urls import reverse

from .models import ItemCarrito, Producto, Usuario


class CartViewTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nombre="Ana",
            email="ana@example.com",
            password_hash="hash",
            rol="usuario",
            status="activo",
        )
        self.otro_usuario = Usuario.objects.create(
            nombre="Luis",
            email="luis@example.com",
            password_hash="hash",
            rol="usuario",
            status="activo",
        )
        self.producto = Producto.objects.create(
            nombre="Libro Django",
            descripcion="Guía de Django",
            precio="25.00",
            file_name="django.pdf",
            file_hash="hash",
            status="activo",
        )
        session = self.client.session
        session["cart_user_id"] = self.usuario.pk
        session.save()

    def test_add_and_increment_product_in_cart(self):
        url = reverse("core:cart_add", args=[self.producto.pk])

        self.client.post(url)
        self.client.post(url)

        item = ItemCarrito.objects.get(usuario=self.usuario, producto=self.producto)
        self.assertEqual(item.cantidad, 2)

        response = self.client.get(reverse("core:cart"))
        self.assertContains(response, "Libro Django")
        self.assertContains(response, "$50.00")

    def test_update_and_remove_only_current_users_items(self):
        item = ItemCarrito.objects.create(
            usuario=self.otro_usuario,
            producto=self.producto,
        )
        update_url = reverse("core:cart_update", args=[item.pk])
        remove_url = reverse("core:cart_remove", args=[item.pk])

        self.assertEqual(self.client.post(update_url, {"cantidad": 4}).status_code, 404)
        self.assertEqual(self.client.post(remove_url).status_code, 404)
        item.refresh_from_db()
        self.assertEqual(item.cantidad, 1)

    def test_update_rejects_non_positive_quantity(self):
        item = ItemCarrito.objects.create(
            usuario=self.usuario,
            producto=self.producto,
        )

        response = self.client.post(
            reverse("core:cart_update", args=[item.pk]),
            {"cantidad": "0"},
        )

        self.assertEqual(response.status_code, 400)
        item.refresh_from_db()
        self.assertEqual(item.cantidad, 1)
