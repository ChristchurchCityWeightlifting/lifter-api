from hashid_field.rest import HashidSerializerCharField
from rest_framework import permissions, serializers
from rest_framework_nested.relations import NestedHyperlinkedIdentityField

from api.models import Athlete, Lift


class LiftSerializer(serializers.ModelSerializer):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    url = NestedHyperlinkedIdentityField(
        parent_lookup_kwargs={
            "competitions_pk": "competition__pk",
        },
        view_name="competition-lifts-detail",
    )
    reference_id = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field="api.Lift.reference_id",
        ),
        read_only=True,
    )
    athlete = serializers.PrimaryKeyRelatedField(
        pk_field=HashidSerializerCharField(
            source_field="api.Athlete.reference_id",
        ),
        read_only=False,
        queryset=Athlete.objects.all(),
    )
    athlete_name = serializers.CharField(
        source="athlete.full_name",
        read_only=True,
    )
    athlete_yearborn = serializers.IntegerField(
        source="athlete.yearborn", read_only=True
    )
    competition = HashidSerializerCharField(
        source="competition.reference_id", read_only=True
    )
    competition_name = serializers.CharField(
        source="competition.competition_name",
        read_only=True,
    )
    competition_date_start = serializers.CharField(
        source="competition.date_start",
        read_only=True,
    )

    class Meta:
        model = Lift
        fields = (
            "url",
            "reference_id",
            "lottery_number",
            "athlete",
            "athlete_name",
            "athlete_yearborn",
            "competition",
            "competition_name",
            "competition_date_start",
            "snatches",
            "snatch_first",
            "snatch_first_weight",
            "snatch_second",
            "snatch_second_weight",
            "snatch_third",
            "snatch_third_weight",
            "best_snatch_weight",
            "cnjs",
            "cnj_first",
            "cnj_first_weight",
            "cnj_second",
            "cnj_second_weight",
            "cnj_third",
            "cnj_third_weight",
            "best_cnj_weight",
            "total_lifted",
            "bodyweight",
            "weight_category",
            "team",
            "session_number",
            "placing",
        )
