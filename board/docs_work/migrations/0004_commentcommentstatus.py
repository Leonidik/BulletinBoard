# Generated by Django 4.0.5 on 2022-12-12 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs_work', '0003_comment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCommentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_work.commentstatus')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs_work.comment')),
            ],
        ),
    ]
