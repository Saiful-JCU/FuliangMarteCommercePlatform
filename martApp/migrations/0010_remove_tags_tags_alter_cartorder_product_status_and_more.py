# Generated by Django 5.1.4 on 2025-01-16 14:06

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('martApp', '0009_product_tags_alter_cartorder_product_status_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='tags',
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('process', 'Processing'), ('delivered', 'Delivered')], default='Processing', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('rejected', 'Rejected'), ('published', 'Published'), ('disabled', 'Disabled'), ('in_review', 'In Review'), ('draft', 'Draft')], default='in_review', max_length=10),
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (3, '⭐⭐⭐★☆'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐★☆☆'), (1, '⭐☆☆☆☆')], default=None),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
