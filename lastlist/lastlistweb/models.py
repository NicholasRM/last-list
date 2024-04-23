# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.TextField()
    state = models.TextField()

    class Meta:
        managed = False
        db_table = 'city'


class Contains(models.Model):
    list = models.OneToOneField('List', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING)
    is_replacement = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contains'
        unique_together = (('list', 'item'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.ForeignKey('Quantity', models.DO_NOTHING)
    price = models.ForeignKey('Price', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'item'


class List(models.Model):
    list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    name = models.CharField(max_length=30)
    date_created = models.DateField()

    class Meta:
        managed = False
        db_table = 'list'


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'price'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    brand = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'product'


class ProductRating(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    score = models.PositiveIntegerField()
    date_recorded = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_rating'
        unique_together = (('user', 'product'),)


class Quantity(models.Model):
    quantity_id = models.AutoField(primary_key=True)
    measurement = models.IntegerField()
    unit = models.CharField(max_length=20)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quantity'


class Stock(models.Model):
    vendor = models.OneToOneField('Vendor', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'stock'
        unique_together = (('vendor', 'item'),)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=12)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    password_hash = models.CharField(max_length=32)
    email = models.CharField(max_length=40)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    name = models.TextField()
    street_number = models.PositiveIntegerField()
    street_name = models.TextField()
    city = models.ForeignKey(City, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vendor'


class VendorRating(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    vendor = models.ForeignKey(Vendor, models.DO_NOTHING)
    score = models.PositiveIntegerField()
    date_recorded = models.DateField()

    class Meta:
        managed = False
        db_table = 'vendor_rating'
        unique_together = (('user', 'vendor'),)