# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 12:21
from __future__ import unicode_literals
import importlib

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

########################################################################################################################
## For each fieldtranslation we have to assign its module.
## Please, take note that we can do it now because we don't have models with the same name in different modules
## so we are going to fix this error before that situation happens.
def assign_module(apps, schema_editor):
    # Get the current model
    FieldTranslation = apps.get_model('modeltranslation', 'FieldTranslation')

    ## For each fieldtranslation we have to assign its module.
    field_translations = FieldTranslation.objects.all()
    for field_translation in field_translations:
        # For each module with translatable models, we load it
        # and test if the model is inside this module
        # It could be made more efficiently but there are no many developers currently using this application so
        # we don't have to be extremely careful about performance.
        for module_path in settings.TRANSLATABLE_MODEL_MODULES:
            module = importlib.import_module(module_path)
            if hasattr(module, field_translation.model):
                field_translation.module = module_path
                field_translation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('modeltranslation', '0005_auto_20160107_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldtranslation',
            options={'verbose_name': 'model object field translation', 'verbose_name_plural': 'model object field translations'},
        ),
        migrations.AddField(
            model_name='fieldtranslation',
            name='module',
            field=models.CharField(default='', help_text='Module name that contains the model whose field is translated', max_length=128, verbose_name='Module name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='context',
            field=models.TextField(default=None, help_text='Help context that will be helpful for translators.', null=True, verbose_name='Context'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='creation_datetime',
            field=models.DateTimeField(verbose_name='Creation date and time of this translation'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='creator_user',
            field=models.ForeignKey(default=None, help_text='User that created last translation version', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_translation', to=settings.AUTH_USER_MODEL, verbose_name='User translator'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='field',
            field=models.CharField(help_text='Name of the field that is translated', max_length=128, verbose_name='Object field'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='is_fuzzy',
            field=models.BooleanField(default=False, help_text='This translation needs some reviewing.', verbose_name='\xbfNeeds reviewing?'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='lang',
            field=models.CharField(choices=[('es', 'Espa\xf1ol'), ('en', 'English'), ('de', 'Deutsch')], help_text='Language ISO code of this translation', max_length=16, verbose_name='Language Id'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='last_update_datetime',
            field=models.DateTimeField(verbose_name='Last update date and time of this translation'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='model',
            field=models.CharField(help_text='Model name whose field is translated', max_length=128, verbose_name='Model name'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='object_id',
            field=models.PositiveIntegerField(default=1, help_text='Object id whose field is translated', verbose_name='Object id'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='source_md5',
            field=models.CharField(help_text='MD5 checksum of source text', max_length=128, verbose_name='MD5 source text'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='source_text',
            field=models.TextField(help_text='Source text in default language', verbose_name='Source text'),
        ),
        migrations.AlterField(
            model_name='fieldtranslation',
            name='translation',
            field=models.TextField(default=None, help_text='Translation showed to users in website when showing it in choosed language.', null=True, verbose_name='Translation'),
        ),
        migrations.RunPython(assign_module)
    ]
