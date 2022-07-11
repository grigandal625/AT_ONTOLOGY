# Generated by Django 4.0.6 on 2022-07-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontology_model', '0002_alter_elementtype_options_alter_relationtype_options_and_more'),
        ('ontology', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='element',
            options={'verbose_name': 'Элемент', 'verbose_name_plural': 'Элементы'},
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файлы'},
        ),
        migrations.AlterModelOptions(
            name='relation',
            options={'verbose_name': 'Связь', 'verbose_name_plural': 'Связи'},
        ),
        migrations.AddField(
            model_name='relation',
            name='child',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='input', to='ontology.element', verbose_name='Дочерний элемент'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relation',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='output', to='ontology.element', verbose_name='Родительский элемент'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relation',
            name='reflexivity',
            field=models.IntegerField(blank=True, choices=[(None, 'Не указано'), (0, 'По умолчанию'), (1, 'Reflexive'), (2, 'Antireflexive')], default=0, null=True, verbose_name='Антирефлексивность'),
        ),
        migrations.AddField(
            model_name='relation',
            name='symmetry',
            field=models.IntegerField(blank=True, choices=[(None, 'Не указано'), (0, 'По умолчанию'), (1, 'Symmetric'), (2, 'Antisymmetric')], default=0, null=True, verbose_name='Симметричность'),
        ),
        migrations.AddField(
            model_name='relation',
            name='transitivity',
            field=models.IntegerField(default=0, verbose_name='Транзитивность'),
        ),
        migrations.AlterField(
            model_name='element',
            name='data',
            field=models.JSONField(blank=True, null=True, verbose_name='Описание элемента'),
        ),
        migrations.AlterField(
            model_name='element',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='element',
            name='files',
            field=models.ManyToManyField(to='ontology.file', verbose_name='Файлы'),
        ),
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='element',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ontology_model.elementtype', verbose_name='Тип элемента'),
        ),
        migrations.AlterField(
            model_name='file',
            name='content',
            field=models.FileField(upload_to='', verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ontology_model.relationtype', verbose_name='Тип связи'),
        ),
    ]
