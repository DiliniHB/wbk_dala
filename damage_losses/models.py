from __future__ import unicode_literals

from django.db import models
from settings.models import District, Province
from incidents.models import IncidentReport


class DmfLosCud(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_cud'


class DmfDfaNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.IntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_dfa_num'


class DmfDfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.IntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_dfa_paf'


class DmfDaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_structure'


class DmfDaSupplies(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_supplies'


class DmfDaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_mequipment'


class DmfDaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_da_oassets'


class DmfPdfaNum(models.Model):
    num_pdamaged_facilities = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.BigIntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pdfa_num'


class DmfPdfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.BigIntegerField(blank=True, null=True)
    divisional_hospital = models.BigIntegerField(blank=True, null=True)
    rural_hospital = models.BigIntegerField(blank=True, null=True)
    central_dispensary = models.BigIntegerField(blank=True, null=True)
    pmcus = models.BigIntegerField(blank=True, null=True)
    phccs = models.BigIntegerField(blank=True, null=True)
    mchcs = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pdfa_paf'


class DmfPdaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_structure'


class DmfPdaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_mequipment'


class DmfPdaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_pda_oassets'


class DmfLosFi(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_fi'


class DmfLosHoc(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_hoc'


class DmfLosOue(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    base_hospital = models.FloatField(blank=True, null=True)
    divisional_hospital = models.FloatField(blank=True, null=True)
    rural_hospital = models.FloatField(blank=True, null=True)
    central_dispensary = models.FloatField(blank=True, null=True)
    pmcus = models.FloatField(blank=True, null=True)
    phccs = models.FloatField(blank=True, null=True)
    mchcs = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmf_los_oue'


# table 8
class DshPubLmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport,db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_lmh'


class DshPubMoh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport,  db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_moh'


class DshPubOmf(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'dsh_pub_omf'


class DshPvtFa(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pvt_fa'


class DshTdlOwship(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_tdl_owship'


# table 10
class DsnPubP1Lmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_lmh'


class DsnPubP1Moh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_moh'


class DsnPubP1Omc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_p1_omc'


class DsnPubPnLmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_lmh'


class DsnPubPnMoh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_moh'


class DsnPubPnOmc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pub_pn_omc'


class DsnPvtP1(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pvt_p1'


class DsnPvtPn(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_pvt_pn'


class DsnTdlOwship(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsn_tdl_owship'


#dileepa


#damages and losess
#public
#tab 1
class DmhDfNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_df_num'


class DmhDfPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_df_paf'


#tab 2
class DmhNdatFacStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_structure'


class DmhNdatFacSupplies(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_supplies'


class DmhNdatFacMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_mequipment'


class DmhNdatFacOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_ndat_fac_oassets'


#tab 3
class DmhPdfaNum(models.Model):
    num_des_facilities = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    bs_date = models.CharField(max_length=255, blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_num'


class DmhPdfaPaf(models.Model):
    num_patients_affected = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.BigIntegerField(blank=True, null=True)
    provincial_general_hospital = models.BigIntegerField(blank=True, null=True)
    district_general_hospital = models.BigIntegerField(blank=True, null=True)
    office = models.BigIntegerField(blank=True, null=True)
    other = models.BigIntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_paf'


#tab 4
class DmhPdfaStructure(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_structure'


class DmhPdfaMequipment(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_mequipment'


class DmhPdfaOassets(models.Model):
    asset = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_pdfa_oassets'


#tab 5
class DmhLosFi(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_fi'


class DmhLosCud(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_cud'


class DmhLosHoc(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_hoc'


class DmhLosOue(models.Model):
    type_of_losses = models.CharField(max_length=255, blank=True, null=True)
    teaching_hospital = models.FloatField(blank=True, null=True)
    provincial_general_hospital = models.FloatField(blank=True, null=True)
    district_general_hospital = models.FloatField(blank=True, null=True)
    office = models.FloatField(blank=True, null=True)
    other = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dmh_los_oue'


# health_damagelost_private
# Damage and Loss Assessment of Private Health Facilities
# tab 1
class DapNapTmf(models.Model):
    type_med_fac = models.CharField(max_length=255, blank=True, null=True)
    num_affected_fac = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_nap_tmf'


# tab 2
class DapBefPc1(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_pc1'


class DapBefPcn(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_pcn'


class DapBefOther(models.Model):
    pvt_clinics = models.CharField(max_length=255, blank=True, null=True)
    est_replacement_cost = models.FloatField(blank=True, null=True)
    est_repair_cost = models.FloatField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    est_losses_y1 = models.FloatField(blank=True, null=True)
    est_losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dap_bef_other'


#table 9
class DspPubD1Lmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_lmh'


class DspPubDnLmh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport,  db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_lmh'


class DspPubD1Moh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_moh'



class DspPubDnMoh(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_moh'


class DspPubD1Omc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_omc'


class DspPubDnOmc(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_omc'


class DspPvtD1(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pvt_d1'


class DspPvtDn(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pvt_dn'


class DspTdlOwship(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    district = models.ForeignKey(District, db_column='district', blank=True, null=True)
    created_user = models.IntegerField(blank=True, null=True)
    lmu = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    lmd = models.DateTimeField(blank=True, null=True)
    key = models.BigIntegerField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_tdl_owship'


class DshPubLmhProvince(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_lmh_province'


class DshPubOmfProvince(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pub_omf_province'


class DshPvtFaProvince(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_pvt_fa_province'


class DshTdlOwshipProvince(models.Model):
    ownership = models.CharField(max_length=255, blank=True, null=True)
    damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    province = models.ForeignKey(Province, db_column='province', blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsh_tdl_owship_province'


class DspPubD1LmhNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_lmh_national'


class DspPubD1MohNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_moh_national'


class DspPubD1OmcNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_d1_omc_national'


class DspPubDnLmhNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_lmh_national'


class DspPubDnMohNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_moh_national'


class DspPubDnOmcNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pub_dn_omc_national'


class DspPvtD1National(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pvt_d1_national'


class DspPvtDnNational(models.Model):
    facilities_assets = models.CharField(max_length=255, blank=True, null=True)
    total_num_affected = models.BigIntegerField(blank=True, null=True)
    male = models.BigIntegerField(blank=True, null=True)
    female = models.BigIntegerField(blank=True, null=True)
    total_damages = models.FloatField(blank=True, null=True)
    losses_y1 = models.FloatField(blank=True, null=True)
    losses_y2 = models.FloatField(blank=True, null=True)
    total_losses = models.FloatField(blank=True, null=True)
    incident = models.ForeignKey(IncidentReport, db_column='incident', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dsp_pvt_dn_national'
