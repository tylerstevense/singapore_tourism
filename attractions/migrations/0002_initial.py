# Generated by Django 4.1.2 on 2022-11-01 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("custom_auth", "0001_initial"),
        ("attractions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="outinginvitation",
            name="invitee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invites",
                to="custom_auth.profile",
            ),
        ),
        migrations.AddField(
            model_name="outinginvitation",
            name="outing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="outing_invites",
                to="attractions.outing",
            ),
        ),
        migrations.AddField(
            model_name="outing",
            name="attraction",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="attractions.attraction"
            ),
        ),
        migrations.AddField(
            model_name="outing",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_outings",
                to="custom_auth.profile",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="custom_auth.profile"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="outing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="attractions.outing",
            ),
        ),
        migrations.AddField(
            model_name="attraction",
            name="saved_by",
            field=models.ManyToManyField(
                blank=True, related_name="saved_attractions", to="custom_auth.profile"
            ),
        ),
        migrations.AddField(
            model_name="attraction",
            name="tags",
            field=models.ManyToManyField(
                related_name="attractions", to="attractions.tag"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="outinginvitation",
            unique_together={("invitee", "outing")},
        ),
    ]