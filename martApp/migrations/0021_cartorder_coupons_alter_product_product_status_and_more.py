# Generated by Django 5.1.4 on 2025-01-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('martApp', '0020_coupon_alter_cartorder_product_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='martApp.coupon'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('in_review', 'In Review'), ('disabled', 'Disabled'), ('published', 'Published'), ('draft', 'Draft')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (1, '⭐☆☆☆☆'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐★☆☆'), (3, '⭐⭐⭐★☆')], default=None),
        ),
    ]
