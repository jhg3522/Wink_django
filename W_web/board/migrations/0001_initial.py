# Generated by Django 3.0.8 on 2020-08-05 04:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='게시판 이름')),
                ('write_permission', models.BooleanField(default=False, verbose_name='쓰기 권한')),
                ('read_permission', models.BooleanField(default=True, verbose_name='열람 권한')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일')),
                ('read_permission', models.BooleanField(default=True, verbose_name='열람 권한')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User', verbose_name='댓글 소유자')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='게시물 제목')),
                ('content', models.TextField(max_length=5000, verbose_name='게시물 내용')),
                ('m_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성일')),
                ('write_permission', models.BooleanField(default=False, verbose_name='쓰기 권한')),
                ('attachment_img', models.FilePathField(null=True, verbose_name='첨부 사진')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User', verbose_name='게시물 주인')),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='추천 한 날짜')),
                ('comment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Comment', verbose_name='댓글 번호')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User', verbose_name='추천 소유자')),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Document', verbose_name='게시물 번호')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=5000, verbose_name='쪽지 내용')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='보낸 날짜')),
                ('receive_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.User', verbose_name='받는 사람')),
                ('send_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Message', verbose_name='보낸 사람')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Document', verbose_name='게시물 대상'),
        ),
        migrations.AddField(
            model_name='comment',
            name='re_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Comment', verbose_name='대댓글 대상'),
        ),
    ]
